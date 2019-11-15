import requests
import argparse
import sys
from wordcloud import WordCloud

# Set argument to receive thread ID
parser = argparse.ArgumentParser(description="Create word cloud from Reddit comments.")
parser.add_argument("-id", help="provides the id for the reddit thread")
args = parser.parse_args()
thread_id = args.id

# Set the Pushshift API link
BASE_URL = "http://api.pushshift.io/reddit/search/comment/?fields=body&limit=25000&link_id="
final_url = f"{BASE_URL}{thread_id}"

# Get thread comment data
try: 
    r = requests.get(final_url).json()
    data_arr = r["data"]
except:
    print("Error.  No thread with that ID.")
    sys.exit(0)

# Create one huge string for all comments in thread
comment_string = " ".join(comment["body"] for comment in data_arr)

# Generate word cloud and save the image
wc = WordCloud(height=1080, width=1920, 
               background_color="white").generate(comment_string)
image = wc.to_file("reddit_wordcloud.png")