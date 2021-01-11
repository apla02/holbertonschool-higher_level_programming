#!/usr/bin/python3
"""
Python script that takes your Github credentials
(username and password) and uses the Github API to display your id
"""
import requests
import sys


if __name__ == "__main__":

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner_name, repo_name)
    response = requests.get(url)
    response_json = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(response_json[i].get(
                'sha'), response_json[i].get(
                    'commit').get('author').get('name')))
    except:
        pass
