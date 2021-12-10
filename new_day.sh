#!/bin/bash

YEAR=$(date +%Y)
DAY=$(date +%-d)
INPUT_URL="https://adventofcode.com/$YEAR/day/$DAY/input"

DAY_PADDED=$(date +%d)
DIR="day_$DAY_PADDED"
TEMP_INPUT="temp-input.txt"
COOKIE="`cat cookie.txt | tr -d '\n'`"

cp -r "day_xx" "$DIR"
sed -i '' "s/day_xx/$DIR/g" $DIR/main.py

curl "https://adventofcode.com/2021/day/$DAY/input" --compressed \
  -H "Cookie: session=${COOKIE}" \
  -o "${TEMP_INPUT}"

cp ${TEMP_INPUT} $DIR/input.txt
rm ${TEMP_INPUT}
