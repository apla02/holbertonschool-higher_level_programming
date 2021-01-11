#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the
email as a parameter, and displays the body of
the response (decoded in utf-8
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html_page = response.read()
            html_utf8 = html_page.decode('utf-8')
            print(html_utf8)
    except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
