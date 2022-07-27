#The code for pig latin is to add "ay" to the first letter in every word
import re

sentence = input("Type a sentence: ")

s = re.split('\s', sentence)
translation = []

for i in range(len(s)):
    w = s[i][0]
    t = str(s[i][1:])+' ' +w+'ay'
    translation.append(t)

translation_in_pig_latin = ' '.join(translation)
print("Translation in Pig Latin is: \n", translation_in_pig_latin)
