#!/usr/bin/python3

"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests

def top_ten(subreddit):
    # Reddit API endpoint for getting the top posts of a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent to avoid potential issues
    headers = {'User-Agent': 'CustomUserAgent'}

    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        try:
            # Parse the JSON response
            posts_data = response.json()

            # Extract and print the titles of the first 10 posts
            for index, post in enumerate(posts_data['data']['children'][:10], 1):
                title = post['data']['title']
                print(f"{index}. {title}")
        except (KeyError, ValueError) as e:
            print(f"Error parsing JSON: {e}")
    elif response.status_code == 404:
        # Subreddit not found, print None
        print("None")
    else:
        # Handle other error cases
        print(f"Error: {response.status_code}")

