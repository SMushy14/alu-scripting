#!/usr/bin/python3
"""Function to query subscribers on a given subreddit"""
import requests

def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/dev/api/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my-user-agent/0.0.1'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
        response.raise_for_status() # Raises HTTPError for bad responses (4xx and 5xx)
        
        data = response.json()
        
        # Ensure 'data' key exists in the JSON response
        if 'data' in data:
            return data['data'].get('subscribers', 0) # Default to 0 if 'subscribers' key is missing
        else:
            return 0
    except requests.RequestException:
        return 0
