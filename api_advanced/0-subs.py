#!/usr/bin/python3
"""Function to query subscribers on a given subreddit"""
import requests

def number_of_subscribers(subreddit):
    """Return number of subscribers on a given subreddit"""
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit),
    headers = {
        "User-Agent": "My_user_agent"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
