#!/bin/bash

for i in $(seq -f "%02g" 1 25)
do
    GOFILE="./day_$i/go/main.go"
    PYFILE="./day_$i/python/main.py"
    if test -f "$GOFILE"  || test -f "$PYFILE"
    then
        echo "#### Day $i ####"
        if test -f "$GOFILE"
        then
            echo "Go: "
            go run $GOFILE
        fi

        if test -f "$PYFILE";
        then
            echo "Python: "
            python3 $PYFILE
        fi
        printf "\n"
    fi
done
