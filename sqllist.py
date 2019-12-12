#! python3
# sqllist.py - Add the single quotes and comma after every entry, all surrounded by parentheses.

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
