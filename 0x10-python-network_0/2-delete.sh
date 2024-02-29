#!/bin/bash
# Send a delete request using curl to a URL
curl -s -X DELETE "$1" | grep -oP "(?<=\r\n\r\n).*"
