#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit.
"""

from requests import get

def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)

    # Check for a successful request (status code 200)
    if response.status_code == 200:
        try:
            # Parse the JSON response
            results = response.json()
            return results.get('data').get('subscribers')
        except (KeyError, ValueError) as e:
            print(f"Error parsing JSON: {e}")
            return 0
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found.")
        return 0
    else:
        print(f"Error: {response.status_code}")
        return 0

