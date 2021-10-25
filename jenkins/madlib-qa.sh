#!/bin/bash
# Old grep
# grep the h1 tag, Trim html tag, trim leading and trailing whitespace
#LINE=$(curl -s madlibs.thegoldenducks.click | grep "<h1>" | sed 's/<.*>\(.*\)<\/.*>/\1/' | sed 's/^[ \t\n]*//;s/[ \t\n]*$//' | tr -d " \n\r\t"  )

# Test setup
#HTML="<h1>Thanksgiving Dinner Madlib</h1></br>"
#LINE=$(echo "$HTML" | grep -o "Thanksgiving Dinner Madlib")

# New grep
LINE=$(curl -s "http://3.209.236.73" | grep "<h1>" )
echo "Found: $LINE" # | od -x 
LINE=$(echo "$LINE" | grep -o "Thanksgiving Dinner MadLib" )
echo "Grepped: $LINE"
TEXT=$(echo "Thanksgiving Dinner MadLib")
echo "Desired: $TEXT" # | od -x
if [ "$LINE" = "$TEXT" ]
        then
                echo "Success: '$TEXT'"
                exit 0
        else
                echo "Error, not found: '$TEXT'"
                exit 1
fi
