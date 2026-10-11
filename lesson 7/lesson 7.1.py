def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"
assert say_hi("Lena", 23) == "Hi. My name is Lena and I'm 23 years old", 'Test1'
assert say_hi("John", 25) == "Hi. My name is John and I'm 25 years old", 'Test2'
print('OK')

print(say_hi("Lena", 23))
print(say_hi("John", 25))
