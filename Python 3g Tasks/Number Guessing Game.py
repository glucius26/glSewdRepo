import random
n = random.randint(1, 50)
flag = True

print("I'm thinking of a number between 1 and 50...")

g = int(input("Enter Guess"))
gc = 1

if g != n:
        gc += 1
        if g > n:
            print("too high")
        elif g < n:
            print("too low")
else:
    flag = False

while flag == True:
    if g != n:
        g = int(input("Enter Guess"))
        gc += 1
        if g > n:
            print("too high")
        elif g < n:
            print("too low")
    else:
        flag = False

print(f"Correct! You got it in {gc} guesses!")
