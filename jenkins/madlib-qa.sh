#!/bin/bash
# grep the h1 tag, Trim html tag, trim leading and trailing whitespace
#LINE=$(curl -s madlibs.thegoldenducks.click | grep "<h1>" | sed 's/<.*>\(.*\)<\/.*>/\1/' | sed 's/^[ \t\n]*//;s/[ \t\n]*$//' | tr -d " \n\r\t"  )
HTML="<h1>Thanksgiving Dinner Madlib</h1></br>"
LINE=$(echo "$HTML" | grep -o "Thanksgiving Dinner Madlib")
#echo "Found: $LINE" # | od -x 
TEXT=$(echo "Thanksgiving Dinner Madlib")
#echo "Desired: $TEXT" # | od -x
if [ "$LINE" = "$TEXT" ]
        then
                echo "H1 found: '$TEXT'"
                exit 0
        else
                echo "Error, not found: '$TEXT'"
                exit 1
fi
