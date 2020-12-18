#!/bin/bash
# script Bash script that takes in a URL, sends a GET
# request to the URL, and displays the body of the response
# script take -X GET by default, s to silent mode, L follow redirects
curl -sL "$1"
