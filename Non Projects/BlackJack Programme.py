#Pseudocode:

#Get starting money
#While money > 0:
#   Ask for bet
#   generate 2 random number for the player
#   generate 2 random numbers for the dealer
#   print your amount
#   print dealer's amount
#   if player amount exceeds 21
#       print "You bust!"
#       subtract bet amount from starting money
#   elif dealer amount exceeds 21
#       print "You win!"
#       add bet amount to starting money
#   else:
#       generate another random number for the player
#       generate another random number for the dealer
#       print your amount
#       print dealer's amount

#repeat steps until third card is drawn, then the game will conclude
#reuturn to entering betting amount

#If money <= 0
#   print("You are out of money! Game lost!")

import random

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
money = 1000

while money > 0:
    print(f"You have ${money}")
    try:
        bet = int(input("Bet how much money? "))
        
        if bet <= 0 or bet > money:
            print("Invalid bet. Please bet a positive amount no more than your current money.")
            continue

    except ValueError:
        print("Invalid input. Please enter a number.")
        continue  

    pCardOne = random.choice(list1)
    pCardTwo = random.choice(list1)
    pRoundOne = pCardOne + pCardTwo
    print(f"You have a(n) {pRoundOne}.")

    dCardOne = random.choice(list1)
    dCardTwo = random.choice(list1)
    dRoundOne = dCardOne + dCardTwo
    print(f"The dealer has a(n) {dRoundOne}.")

    if pRoundOne > 21:
        print("You Bust!")
        money = money - bet
        print(f"You now have ${money}.")
    elif dRoundOne > 21:
        print("You Win!")
        money = money + bet
        print(f"You now have ${money}.")
    elif dRoundOne == 21:
        print("You Lose!")
        money = money - bet
        print(f"You now have ${money}.")
    else:
        decision = str(input("Hit or Stand?(h/s)"))
        if decision == ("s"):
                    dCardTwo = random.choice(list1)
                    dRoundTwo = dRoundOne + dCardTwo
                    print(f"The dealer has a(n) {dRoundTwo}.")

                    if dRoundThree > 21:
                        print("You win!")
                        print(f"You now have ${money}.")
                    elif 21 - pRoundOne > 21 - dRoundTwo:
                        print("You Bust!")
                        money = money - bet
                        print(f"You now have ${money}.")
                    elif 21 - pRoundOne < 21 - dRoundTwo:
                        print("You Win!")
                        money = money + bet
                        print(f"You now have ${money}.")
                    elif pRoundOne == dRoundTwo:
                        print("You Tie!")
                        print(f"You now have ${money}.")
                    elif dRoundThree > 21:
                        print("You win!")
                        print(f"You now have ${money}.")

        elif decision == ("h"):    
            pCardThree = random.choice(list1)
            pRoundTwo = pRoundOne + pCardThree
            print(f"You have a(n) {pRoundTwo}.")
            dCardThree = random.choice(list1)
            dRoundTwo = dRoundOne + dCardThree
            print(f"The dealer has a(n) {dRoundTwo}.")
            
            if pRoundTwo > 21:
                print("You Bust!")
                money = money - bet
                print(f"You now have ${money}.")
            elif dRoundTwo > 21:
                print("You Win!")
                money = money + bet
                print(f"You now have ${money}.")
            elif dRoundTwo == 21:
                print("You Lose!")
                money = money - bet
                print(f"You now have ${money}.")
            elif pRoundTwo == dRoundTwo:
                print("You Tie!")
                print(f"You now have ${money}.")
            else:
                decision = str(input("Hit or Stand?(h/s)"))
                if decision == ("s"):
                    dCardThree = random.choice(list1)
                    dRoundThree = dRoundTwo + dCardThree
                    print(f"The dealer has a(n) {dRoundThree}.")

                    if dRoundThree > 21:
                        print("You win!")
                        print(f"You now have ${money}.")
                    elif 21 - pRoundTwo > 21 - dRoundThree:
                        print("You Bust!")
                        money = money - bet
                        print(f"You now have ${money}.")
                    elif 21 - pRoundTwo < 21 - dRoundThree:
                        print("You Win!")
                        money = money + bet
                        print(f"You now have ${money}.")
                    elif pRoundTwo == dRoundThree:
                        print("You Tie!")
                        print(f"You now have ${money}.")
        
                elif decision == ("h"):    
                    pCardThree = random.choice(list1)
                    pRoundThree = pRoundTwo + pCardThree
                    print(f"You have a(n) {pRoundThree}.")
                    dCardThree = random.choice(list1)
                    dRoundThree = dRoundTwo + dCardThree
                    print(f"The dealer has a(n) {dRoundThree}.")

                    if pRoundThree > 21:
                        print("You Bust!")
                        money = money - bet
                        print(f"You now have ${money}.")
                    elif dRoundThree > 21:
                        print("You Win!")
                        money = money + bet
                        print(f"You now have ${money}.")
                    elif dRoundThree == 21:
                        print("You Lose!")
                        money = money - bet
                        print(f"You now have ${money}.")
                    elif pRoundThree == dRoundThree:
                        print("You Tie!")
                        print(f"You now have ${money}.")
                    elif 21 - pRoundThree > 21 - dRoundThree:
                        print("You Bust!")
                        money = money - bet
                        print(f"You now have ${money}.")
                    elif 21 - pRoundThree < 21 - dRoundThree:
                        print("You Win!")
                        money = money + bet
                        print(f"You now have ${money}.")
                    else:
                        print("You tie!")



print("Game over! You've run out of money.")
