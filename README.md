# CUNY Fall 2024

This repository contains code and exercises from `Uncovering AI Bias: Investigative Strategies for Reporters` and `Secure AI for News Investigations` taught by John Templon at CUNY during the fall of 2024. It will be regularly updated during that time period.

## Code Examples

### Reddit Parser

The `reddit-example.py` file uses the `praw` package to process titles from a user's Reddit hot list and figure out the average polarity and subjectivity of the top N posts along with the average polarity and subjectivity of the shown subreddits. The script requires: `praw`, `textblob`, and `pandas` be installed in order to run. You will also need a Reddit script along with all of the envrionmental variables at the top.

It is recommended you change the `user-agent` on line 10 to a string unique to your personal Reddit app. Otherwise it's possible that you'll run into rate limits if too many people run the code using the string originally included in the script.

### Facebook Quantified Selfie

The `quantified-selfie.ipynb` file is a Jupyter Notebook that uses personal data downloaded from Facebook to investigate what the service knows about the user. The notebook walks through a number of the files included in the data dump. (Note: The notebook assumes you downloaded the data in JSON format.) In order to use the file you'll need to add a path to the Facebook dump in the `FACEBOOK_PATH` variable.

### Blockchain Explorer

The `blockchain-explore.ipynb` file is a Jupyter Notebook that allows you to explore the transactions for a group of Bitcoin wallet addresses. The notebook is currently set up to explore a set of addresses associated with a federal indictment, but it can be used to explore any content you're interested in. It requires you install the `blockchain` package along with Pandas prior to execution.

### OpenAI Interaction

The `openai-interaction.ipynb` file is a Jupyter Notebook that sets up some basic interaction with the OpenAI API. It requires you install the `openai` package prior to execution. You will also need an environmental variable for your `OPENAI_API_KEY`, which can be found in your user profile.

### Citi Bike Basics

The `CitiBikeBasics.ipynb` file is a Jupyter Notebook that does some basic analysis of Citi Bike data. This notebook requires the `pandas` package to run. You will need to download the `202409-citibike-tripdata.zip` file from Citi Bike's [data repository](https://s3.amazonaws.com/tripdata/index.html) and unzip it into the same directory as the Notebook for it to run properly. (You do not need to unzip the CSVs in the zip.)

### Citi Bike Real-Time

The `CitiBikeRealTime.ipynb` file is a Jupyter Notebook that does analysis of Citi Bike's [real-time data portal](https://gbfs.citibikenyc.com/gbfs/2.3/gbfs.json). This notebook requires the `pandas` and `requests` libraries in order to run. If you have them installed it will pull and analyze data for the system in real-time.


### Citi Bike K-Means

The `CitiBikeKMeans.ipynb` file is a Jupyter Notebook that implements a K-Means clustering algorithm for Citi Bike stations using the Citi Bike trip data. You'll need the same data as the Citi Bike Basics notebook. In addition, in order to do the mapping you'll need `geopandas` and `matplotlib` installed. You'll also need a GeoJSON version of NYC, which you can [download here](https://github.com/codeforgermany/click_that_hood/blob/main/public/data/new-york-city-boroughs.geojson) (and other places). In order to do the K-Means clustering you'll need to install `scikit-learn`.

### Spy Planes Random Forest

The `spy-planes-random-forest.ipynb` file is a Jupyter Notebook that implements the Random Forest model in Python based on Peter Aldhous's [original R code](https://github.com/BuzzFeedNews/2017-08-spy-plane-finder/blob/master/index.Rmd). The notebook requires `pandas`, `numpy`, `scikit-learn` and `matplotlib`. If you have them installed and the data from the original GitHub repository accessible to the notebook, it will create a Random Forest model with some explanations and visualizations. The "Your Turn" section at the end is left intentionally blank as the beginning of an individual in-class exercise.

### Image Breakdown Example

The `image-breakdown-example.ipynb` file is a Jupyter Notebook designed to show how images can be converted to data. You'll need to give it an example image so it can find the RGB layers and the metadata. The notebook requires `PIL`.

### Face Recognition

The `face-recognition.ipynb` file is a Jupyter Notebook that does basic facial recognition tasks using the [`face-recognition`](https://github.com/ageitgey/face_recognition) library. There is some setup for this library, including pre-installing `cmake` and `dlib`. See the **Installation** header in the GitHub repository for more information. The notebook also requires `PIL`, which should be installed as part of the library installation. You'll also need any number of photos of yourself. To make the notebook work:

1. Direct it at the best image as the `me_image`
2. Attempt to find faces on the others
3. Use the last part of the notebook to debug any "issues" finding faces

### Satellite Analysis Basics

The `satellite-analysis-basics.ipynb` file is a Jupyter Notebook that contains the compontent pieces for doing YOLO object detection with oriented bounding boxes on Umbra's [open data catalog](https://registry.opendata.aws/umbra-open-data/) of satellite images. You will need the following libraries: `boto3`, `ultralytics`, `pandas` and `PIL`. The notebook contains code for finding the images in s3, processing them with YOLO, and making those results more interpretable.

### Text Analysis

The `text-analysis.ipynb` file is a Jupyter Notebook that contains the component pieces for building a KMeans classifier that handles articles from the New York Times. You will need the `gensim` and `pandas` libraries to run the notebook. In addition, there is some exploration of the Google Word2Vec model, which requires an additional download.

### Yelp Reviews

The `yelp-reviews.ipynb` file is a Jupyter Notebook that contains the code necessary to create a sentiment classifier of Yelp reviews based on example data. In order to use the Yelp data you'll need a new CSV that includes the "sentiment" for a number of the reviews as an additional column. The notebook requires `textblob` and `pandas`. There is an additional one-time download inside of the notebook for an NLTK corpora.

### Data Masking

The `data-masking.ipynb` file is a Jupyter Notebook that contains an exercise around masking data.

### OpenAI Examples

The `openai-examples.ipynb` file is a Jupyter Notebook that contains three examples for interacting with the OpenAI API. It requires you install the `openai` package prior to execution. You will also need an environmental variable for your `OPENAI_API_KEY`, which can be found in your user profile. In addition, you'll need the libraries that have already been installed for other notebooks. The notebook also requires the `office-furniture.jpg` image if you want to analyze that one, otherwise you can pick a different image for the Vision examples.