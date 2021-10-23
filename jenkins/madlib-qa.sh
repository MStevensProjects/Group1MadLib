#!/bin/bash
LINE = curl -s madlibs.thegoldenducks.click | grep "<h1>" | sed 's/<.*>\(.*\)<\/.*>/\1/'
echo "$LINE"
TEXT="Thanksgiving Dinner Madlib"
if LINE -eq "$TEXT";then
        echo "H1 found: '$TEXT'"
        exit 0
        else
                echo "Error, not found: '$TEXT'"
                exit 1
fi
