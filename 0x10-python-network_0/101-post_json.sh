#!/bin/bash
# using curl with post to json
curl -X POST -H "Content-Type: application/json" -d "$1" "@$2"
