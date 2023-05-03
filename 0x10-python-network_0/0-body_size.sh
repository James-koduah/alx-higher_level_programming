#!/bin/bash
# Display the size of a body of response from a url


curl -sI $1 | grep 'Content-Length' | cut -d " " -f2
