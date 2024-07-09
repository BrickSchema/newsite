#!/bin/bash

mkdir -p content/static/schema

# for each .ttl file in static/schema/<version>/Brick.ttl, create a
# blank .md file in content/static/schema/<version>/Brick.md

for file in static/schema/*/Brick.ttl; do
  version=$(dirname $file | xargs basename)
  echo "Creating content/schema/$version/Brick.md"
  mkdir -p content/schema/$version
  # create an alias for the .ttl file
  cat <<EOF > content/schema/$version/Brick.md
<html>
<meta http-equiv="content-type" content="text/turtle; charset=UTF-8">
<meta http-equiv="refresh" content="0; url=../../$file">
</html>
EOF

done
