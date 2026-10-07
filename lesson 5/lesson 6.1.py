import string
from unittest import result

text = input()
first = text[0]
last = text[2]
start = string.ascii_letters.find(first)
end = string.ascii_letters.find(last)
result = string.ascii_letters[start:end + 1]
print(result)

