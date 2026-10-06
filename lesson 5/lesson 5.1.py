import string
import keyword

name = input()
valid = True

if name[0].isdigit():
    valid = False
for letter in name:
    if letter.isupper( ):
        valid = False
    if letter in string.punctuation and letter !='_':
        valid = False
    if letter.isspace( ):
        valid = False
    if name in keyword.kwlist:
        valid = False
    if '__' in name:
        valid = False

print(valid)



