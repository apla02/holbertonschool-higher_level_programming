#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q
If no argument is given, set q=""

"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    data = {"q": letter}
    response = requests.post(url, data)
    try:
        json_response = response.json()
        if len(json_response) >= 1:
            print("[{}] {}".format(
                json_response["id"], json_response["name"]))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
