#!/bin/bash
# Post a json file to a server
curl -X POST -H "Content-Type: application/json" -d @$2 $1
