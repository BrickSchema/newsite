#!/bin/bash

# Iterate over all .ttl files in the current directory
find static/schema -type f -name '*.ttl' | while read -r file; do
  # Get the base name without the .ttl extension
  base="${file%.ttl}"
  
  # Copy the file to a new file without the .ttl suffix
  cp "$file" "$base"
done
