#!/bin/bash
# Bash script to make a request to a URL and display the response body
curl -sL 0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -H "Origin: School"
