#!/bin/bash
# using curl with post to json
curl -s -H "Content-Type: application/json" "$1" -d "@$2"
