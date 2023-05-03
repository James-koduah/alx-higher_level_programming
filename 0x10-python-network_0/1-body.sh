#!/bin/bash
# Send a GET request to a server and return body if status is 200
curl -sfL $1 -X GET
