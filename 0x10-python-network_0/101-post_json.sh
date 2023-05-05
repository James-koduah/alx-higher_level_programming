#!/bin/bash
# Post a json file to a server
curl -s -X POST -H "Content-Type: application/json" -d @$2 $1
