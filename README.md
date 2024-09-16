# CUNY Fall 2024

This repository contains code and exercises from `Uncovering AI Bias: Investigative Strategies for Reporters` and `Secure AI for News Investigations` taught by John Templon at CUNY during the fall of 2024. It will be regularly updated during that time period.

## Code Examples

### Reddit Parser

The `reddit-example.py` file uses the `praw` package to process titles from a user's Reddit hot list and figure out the average polarity and subjectivity of the top N posts along with the average polarity and subjectivity of the shown subreddits. The script requires: `praw`, `textblob`, and `pandas` be installed in order to run. You will also need a Reddit script along with all of the envrionmental variables at the top.

It is recommended you change the `user-agent` on line 10 to a string unique to your personal Reddit app. Otherwise it's possible that you'll run into rate limits if too many people run the code using the string originally included in the script.