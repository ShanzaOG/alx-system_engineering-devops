#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:47:53 2020

@author: Shanza Allan
"""


from json import loads
from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit and returns the number
    of subscribers for a given subreddit.

    If no results  the function should return 0.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) '
        'Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }


    response = get(url, headers=headers)
    
    try:
        reddits = response.json()
        subscribers = reddits.get('data', {}).get('subscribers', 0)
        return int(subscribers)
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
