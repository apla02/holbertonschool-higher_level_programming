#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the body of the response.
If the HTTP status code is greater than or equal to 400, print: Error code:
followed by the value of the HTTP status code
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    code_error = response.status_code
    if code_error >= 400:
        print("Error code: {}".format(code_error))
    else:
        print(response.text)
