text = input("Enter text: ")

words = text.split(" ")
newWords = []

i = 0
for word in words:
    newWord = ""
    for letter in word:
        if i % 2 == 0:
            newWord += letter.upper()
        else:
            newWord += letter.lower()
        i += 1
    newWords.append(newWord)

print(" ".join(newWords))