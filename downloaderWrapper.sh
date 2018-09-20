#!/bin/bash

# Read the line
while IFS='' read -r line || [[ -n "$line" ]]; do
    # Execute the line
    bash "$line"
# File to read from
done < "toDownload.txt"
