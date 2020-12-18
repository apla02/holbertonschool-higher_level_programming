#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
# curl -sI "$1"  -X options| grep -i allow | awk '{OFS= " "} {print $2, $3, $4}'
curl -sI 0.0.0.0:5000 -X allow |grep -i Allow |cut -d " " -f 2-                                                               
