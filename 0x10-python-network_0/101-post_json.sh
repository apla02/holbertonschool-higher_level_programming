#!/bin/bash
# using curl with post to json file
curl -X POST -H "Content-Type: application/json" -d "$2" @"$1"
