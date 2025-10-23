word = str(input("Please enter word:"))
counter = 0
for character in word:
    if character == "a":
        counter += 1

print(f"The word {word} has {counter} lowercase a's")