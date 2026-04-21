sentence = input("Enter sentence: ")

words = sentence.split()
result = ""

for w in words:
    result = result + w.capitalize() + " "

print("New sentence:", result)