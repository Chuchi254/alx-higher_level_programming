#!/bin/bash
# This script takes in a URL, send a POST request with specified variables, and displays the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
