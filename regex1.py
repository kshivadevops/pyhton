import re

text = "my name is shiva"
pattern = "shiva"

search = re.search(pattern,text)
if search:
   print("pattern found:", search.group())
else:
   print("pattern is not found")






