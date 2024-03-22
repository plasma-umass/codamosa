#!/bin/bash
# Called by eval_codamosa.py to run tests and measure coverage.

# copy package to make it writable
cp -R /package .
cd package

# install dependencies
pip install -r package.txt #|| exit 1

# install timeout plugin
pip install pytest-timeout

PKG=$1
JSON=$2
OPTS=$3

CMD="python3 -m slipcover --source $PKG --branch --json --out /output/$JSON -m pytest --rootdir . -c /dev/null -p no:cacheprovider --timeout 120 $OPTS /tests"
echo $CMD
eval $CMD
