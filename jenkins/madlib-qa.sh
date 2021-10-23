#!/bin/bash
LINE=$(curl -s madlibs.thegoldenducks.click | grep "<h1>" | sed 's/<.*>\(.*\)<\/.*>/\1/') | tr -d '\t' | tr | tr -s [:space:]
echo "$LINE"
TEXT="Thankgiving Dinner Madlib"
echo "$TEXT"
if [ "$LINE" == "$TEXT" ]
        then
                echo "H1 found: '$TEXT'"
                exit 0
        else
                echo "Error, not found: '$TEXT'"
                exit 1
fi
