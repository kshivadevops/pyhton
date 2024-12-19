import re

text = "my name is shiva"
pattern = "name"
replacement = "nickname"

new_text = re.sub(pattern,replacement,text)
print("modified", new_text)






