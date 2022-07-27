from random import choice
words = ["apple", "book", "cat", "dog", "egg", "fan", "goat", "ink", "jug", "kite"]

for i in range(len(words)):
    s = choice(words)
    unique_words = []
    for letter in s:
        if letter not in unique_words:
            unique_words.append(letter)

    if len(s) != len(unique_words):
        s = choice(words)
    else:
        print(s)
        break
