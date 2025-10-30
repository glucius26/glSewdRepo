import random
Nnum = 0
flag = True
Wtracker = 0
Ltracker = 0

while flag == True:
    Cnum = random.randint(1, 100)
    print(f"Current Number: {Cnum}")
    Nnum = random.randint(1, 100)
    guess = str(input("Will the next number be (h)igher or (l)ower? "))
    if guess == "h":
        if Nnum > Cnum:
            print("You Win!")
            Wtracker += 1
        else: 
            print("You Lose!")
            Ltracker +=1
    elif guess == "l":
        if Nnum > Cnum:
            print("You Lose!")
            Ltracker +=1
        else:
            print("You Win!")
            Wtracker += 1
    print(Nnum)
    print(f"Score: {Wtracker} wins, {Ltracker} losses")