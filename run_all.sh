#!/bin/bash

for i in $(seq -f "%02g" 1 25)
do
    FILE="./day_$i/main.go"
    if test -f "$FILE"; then
        echo "#### Day $i ####"
        go run $FILE
        printf "\n"
    fi
done
