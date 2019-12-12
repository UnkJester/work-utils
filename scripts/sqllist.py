#! python3
# sqllist.py - Add the single quotes and comma after every entry, all surrounded by parentheses.

##
#  To use, copy several rows of values that you want to SELECT on in a list.
#   This script will adjust those values and format the input on your clipboard.
##
import pyperclip
text = pyperclip.paste()

# Separate lines and add parentheses
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '\'' + lines[i] + '\','
result = '(' + '\n'.join(lines)
result = result[:-1]                          # remove the last comma 
result += ')'

pyperclip.copy(result)

print('\nThe text in your clipboard has been successfully reformatted for a SELECT * IN statement.\n')
