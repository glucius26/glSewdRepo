quantity = int(input("How mant free throws?"))
score = 0
for i in range(1, quantity + 1):
    scoreQ = str(input("Was the shot made?(y/n)"))
    if scoreQ == "y":
        score = score + 1
    else:
        score = score + 0
print(f"final score: {score} out of {quantity}")