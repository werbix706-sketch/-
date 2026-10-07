import string

text = input()
words = []

for word in text.split():
    new_word =''

    for letter in word:
        if letter not in string.punctuation:
            new_word = new_word + letter

    word = word.capitalize()
    words.append(word)

hashtag = "".join(words)
hashtag = '#' + hashtag

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
