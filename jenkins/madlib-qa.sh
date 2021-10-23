#!/bin/bash
# grep the h1 tag, Trim html tag, trim leading and trailing whitespace
LINE=$(curl -s madlibs.thegoldenducks.click | grep "<h1>" | sed 's/<.*>\(.*\)<\/.*>/\1/' | sed 's/^[ \t]*//;s/[ \t]*$//')
#sed -n '/>/,/</p'
echo "$LINE"
TEXT="Thankgiving Dinner Madlib"
echo "$TEXT"
if [ "$TEXT" = "Thankgiving Dinner Madlib" ]
        then
                echo "H1 found: '$TEXT'"
                exit 0
        else
                echo "Error, not found: '$TEXT'"
                exit 1
fi
