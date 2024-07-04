#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument
# and displays the body of the response. The contents of a file passed as the
# second argument are sent in the body of the request.

curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
