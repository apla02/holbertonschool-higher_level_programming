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
    response = request.get(url, auth=(username, passw))
    json_response = response.json()
    try:
        print(json_response.get("id"))
    except:
        print("None")
