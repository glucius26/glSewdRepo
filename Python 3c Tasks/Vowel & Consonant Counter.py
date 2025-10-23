v = 0
c = 0

word = str(input("Enter Word:"))

for character in word:
    if character.isalpha == true:
        word = word.lower()
        if character in "aeiou":
            v = v + 1
        else:
            c = c + 1

print(f"Vowels:{v}")
print(f"consonants:{c}")