sentence = input("Enter sentence: ")
word = input("Enter word to delete: ")

words = sentence.split()
new_sentence = ""

for w in words:
    if w != word:
        new_sentence = new_sentence + w + " "

print("New sentence:", new_sentence)