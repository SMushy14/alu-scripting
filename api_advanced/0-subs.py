#!/usr/bin/python3
"""Function to query subscribers on a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers on a given subreddit"""
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "RedditSubscriberChecker/1.0 (by u/S_mushy14)"
    }
    response = requests.get(URL, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    if response.status_code != 200:
        print("Error: received status code", response.status_code)
        return 0
    try:
        results = response.json().get("data")
        return results.get("subscribers", 0)
    except ValueError:
        print("Error: received invalid JSON")
        return 0

# Test cases
if __name__ == "__main__":
    import sys
    subreddit = sys.argv[1]
    print(number_of_subscribers(subreddit))
