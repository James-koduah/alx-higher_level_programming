#!/bin/bash
# send a GET request to a server and a variable and dislpay the response
curl -s $1 -X GET -H "X-School-User-Id: 98"
