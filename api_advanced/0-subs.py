#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the number of subscribers
    for a given subreddit."""

if (type(subreddit) is not str):
        return(0)

    url_api = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    json_obj = requests.get(url, headers={'User-Agent': 'My User Agent 1.0'})
    if json_obj.status_code != 404:
        dict_obj = json_obj.json()
        return dict_obj.get('data').get('subscribers')
    else:
        return (0)
