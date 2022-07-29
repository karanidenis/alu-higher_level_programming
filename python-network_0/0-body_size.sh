#!/bin/bash
# use curl to display size of the body of response
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f 2