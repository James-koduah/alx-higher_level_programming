#!/bin/bash
# send a POST request to a server with some variables
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
