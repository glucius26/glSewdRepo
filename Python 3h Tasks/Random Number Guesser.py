import random

num = int(input("Think of a number between 1 and 100..."))
flag = True
guess = random.randint(1, 100)
count = 0

while flag == True:
    print(f"My guess is {guess}.")
    count += 1
    correction = str(input("higher, lower, or correct?"))
    if correction == "higher":
        guess = random.randint(guess, 100)
    elif correction == "lower":
        guess = random.randint(1, guess)
    else:
        flag = False

print("I got it in {count} guesses!")