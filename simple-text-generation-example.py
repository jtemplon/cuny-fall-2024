import requests
from datetime import datetime

USGS_LINK = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"

r = requests.get(USGS_LINK)

data = r.json()

# make sure there are earthquakes in the past hour
eq_count = data.get('metadata', {}).get('count', 0)

text_pieces = []
if eq_count > 0:
    most_recent_eq = data.get('features', [])[0].get('properties', {})
    magnitude = most_recent_eq.get('mag', 0)
    place = most_recent_eq.get('place')
    timestamp = most_recent_eq.get('time')
    time = datetime.fromtimestamp(timestamp / 1000).strftime('%c')
    if magnitude > 4.5:
        text_pieces.append(f"There was a significant earthquake at {place} on {time}.")
    elif magnitude >= 2.5:
        text_pieces.append(f"There was a major earthquake at {place} on {time}.")
    elif magnitude >= 1:
        text_pieces.append(f"There was a minor earthquake at {place} on {time}.")
    else:
        text_pieces.append(f"There was a tremor at {place} on {time}.")
    text_pieces.append(f"It was of magnitude {magnitude:.1f}.")
    text = " ".join(text_pieces)
    print(text)