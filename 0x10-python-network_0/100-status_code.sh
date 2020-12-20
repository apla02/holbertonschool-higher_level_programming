#!/bin/bash
# only status code, no pipes or redirections
curl -o /dev/null -s -w "%{http_code}\n" "$1"
