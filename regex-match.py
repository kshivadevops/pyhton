import re

text = "my name is shiva"
pattern = "name"

match = re.match(pattern,text)
if match:
   print("match found:", match.group())
else:
   print("no match")






