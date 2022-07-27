from random import shuffle
import re
sent = input("Enter a sentence: ")
sentence = sent.split()
finito = shuffle(sentence)

w = ' '.join(sentence)
y = w[0].upper() + w[1:]
print(y)
