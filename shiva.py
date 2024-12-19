import re
text = "shiva is very handsone boy"
pattern = r"good"
search = re.search(pattern, text)
if search:
  print("pattern found:", search.group())
else:
  print("pattern is not found")
 