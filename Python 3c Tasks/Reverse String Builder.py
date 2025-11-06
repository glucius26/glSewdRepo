reversedStr = ""

word = str(input("Enter Word: "))

for i in word:
    reversedStr = i + reversedStr
print(f"{reversedStr}")