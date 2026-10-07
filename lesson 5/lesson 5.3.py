import string

text = input()
words = []

for word in text.split():
    new_word =''

    for letter in word:
        if letter not in string.punctuation:
            new_word = new_word + letter

    new_word = new_word.capitalize()
    words.append(new_word)

hashtag = "".join(words)
hashtag = '#' + hashtag

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
