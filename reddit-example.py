from textblob import TextBlob
import praw
import os
import pandas as pd

reddit = praw.Reddit(
    client_id=os.environ['REDDIT_CLIENT_ID'],
    client_secret=os.environ['REDDIT_CLIENT_SECRET'],
    password=os.environ['REDDIT_PASSWORD'],
    user_agent="john-top-sentiment-analyzer", #can be any string you want
    username=os.environ['REDDIT_USERNAME'],
)

print(reddit)

# Output score for the first item on the frontpage as a test
for submission in reddit.front.hot(limit=1):
    # print(submission.__dict__)
    print(submission.subreddit.display_name)
    print(submission.title)
    blob = TextBlob(submission.title)
    # this reveals polarity and subjectivity
    # polarity is -1 to 1 (negative vs. positive)
    # subjectivity is 0 to 1 (1 indicates more personal opinion)
    print(blob.sentiment)

# Let's find sentiment for all the titles on my frontpage!
# initialize vars
total_polarity = 0
positive_posts = 0
negative_posts = 0
total_subjectivity = 0
most_negative = 1 # why can these initialize at 0
most_positive = -1
most_negative_title = ''
most_positive_title = ''

# loop through
number_of_posts = 100
subreddit_dict = {} # for tracking average sentiment for subreddit
for submission in reddit.front.hot(limit=number_of_posts):
    blob = TextBlob(submission.title)
    # totaling polarity
    total_polarity += blob.polarity
    if blob.polarity < 0:
        negative_posts += 1
    # why can't we use an else here?
    elif blob.polarity > 0:
        positive_posts += 1
    # figuring out maxes
    if blob.polarity > most_positive:
        most_positive = blob.polarity
        most_positive_title = submission.title
    if blob.polarity < most_negative:
        most_negative = blob.polarity
        most_negative_title = submission.title
    #totaling subjectivity
    total_subjectivity += blob.subjectivity
    # average subreddit polarity
    if submission.subreddit.display_name in subreddit_dict:
        subreddit_dict[submission.subreddit.display_name]["polarity"] += blob.polarity
        subreddit_dict[submission.subreddit.display_name]["posts"] += 1
        subreddit_dict[submission.subreddit.display_name]["avg_polarity"] = (
            subreddit_dict[submission.subreddit.display_name]["polarity"] / subreddit_dict[submission.subreddit.display_name]["posts"]
        )
    else:
        subreddit_dict[submission.subreddit.display_name] = {}
        subreddit_dict[submission.subreddit.display_name]["polarity"] = blob.polarity
        subreddit_dict[submission.subreddit.display_name]["posts"] = 1
        subreddit_dict[submission.subreddit.display_name]["avg_polarity"] = blob.polarity

# Calculate averages
average_polarity = total_polarity / number_of_posts
average_subjectivity = total_subjectivity / number_of_posts

print(subreddit_dict)

# Print results
print(f'There were {positive_posts} positive posts and {negative_posts} negative posts.')
print(f'The average polarity was {average_polarity:.2f}')
print(f'The average subjectivity was {average_subjectivity:.2f}')
print(f'The most positive title was {most_positive_title} with a score of {most_positive:.2f}')
print(f'The most negative title was {most_negative_title} with a score of {most_negative:.2f}')

# strategy using Pandas to find "subreddit" attributes
submissions = reddit.front.hot(limit=number_of_posts)
submissions_dict = [ { 
    "subreddit": s.subreddit.display_name,
    "title": s.title,
    "num_comments": s.num_comments
} for s in submissions ] 
df = pd.DataFrame.from_dict(submissions_dict)

def get_polarity_subjectivity(title):
    blob = TextBlob(title)
    return blob.polarity, blob.subjectivity

df["polarity"], df["subjectivity"] = zip(*df["title"].apply(lambda x: get_polarity_subjectivity(x)))
print(df.head())

print("Polarity Scores")
print(df.groupby("subreddit")["polarity"].mean().sort_values(ascending=False))
print("Subjectivity Scores")
print(df.groupby("subreddit")["subjectivity"].mean().sort_values(ascending=False))
print("Average Comments")
print(df.groupby("subreddit")["num_comments"].mean().sort_values(ascending=False))
