#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """function that fetches number_of_subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        response = requests.get(URL, headers=HEADERS, allow_redirects=False)
        return response.json().get("data").get("subscribers")

    except Exception:
        return 0
