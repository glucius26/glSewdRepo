import random

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
money = 1000

while money > 0:
    print(f"You have ${money}")
    try:
        bet = int(input("Bet how much money? "))
        
        # Check if the bet is valid
        if bet <= 0 or bet > money:
            print("Invalid bet. Please bet a positive amount no more than your current money.")
            continue  # Skips the rest of the loop and starts over

    except ValueError:
        print("Invalid input. Please enter a number.")
        continue  # Skips the rest of the loop and starts over

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

print("Game over! You've run out of money.")
