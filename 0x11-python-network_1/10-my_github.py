#!/usr/bin/python3
"""
Python script that takes your Github credentials
(username and password) and uses the Github API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    passw = sys.argv[2]
    response = requests.get(url, auth=(username, passw))
    try:
        print(response.json().get("id"))
    except:
        pass
