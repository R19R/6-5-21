'''1. panagram - we need to pass the string or sentence. It should have a to z'''

import string


alpha = string.ascii_lowercase

sentence = input("Enter a sentence: ")

counter = 0

for ch in alpha:
    if ch not in sentence.lower():
        counter += 1


if counter == 0:
    print("Sentence is Pangram")
else:
    print("Not a pangram")