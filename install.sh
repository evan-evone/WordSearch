#!/usr/bin/env bash

location="$1"

if [ "$location" == "" ]; then
  location='/usr/local/bin'
fi

if [ -f "$location/wordsearch" ]; then
  rm "$location/wordsearch"
fi

ln -s $(pwd)/python/master.py $location/wordsearch
