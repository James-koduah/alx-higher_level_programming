#!/bin/bash
# Display only the status code response of a web server
curl -s -o /dev/null -w "%{http_code}" $1
