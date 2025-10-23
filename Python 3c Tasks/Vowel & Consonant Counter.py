v = 0
c = 0
o = 0

word = str(input("Enter Word:"))

for character in word:
    if character.isalpha:
        word = word.lower()
        if character in "aeiou":
            v = v + 1
        elif character in ",./;'[]\=-_+{}|:?><!)@(#*&$^%) ":
            o = 0 + 1
        else:
            c = c + 1

print(f"Vowels:{v}")
print(f"consonants:{c}")