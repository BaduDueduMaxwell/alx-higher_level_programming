#!/bin/bash
# This script that sends a JSON POST request to a URL
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
