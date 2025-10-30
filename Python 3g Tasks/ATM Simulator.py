balance = 0

while True:
    print("ATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Choice: "))
    
    if choice == 1:
        print(f"Your Balance: {balance}")
    elif choice == 2:
        add = int(input("Deposit Amount: "))
        balance += add
    elif choice == 3:
        sub = int(input("Withdraw Amount: "))
        balance -= sub
    elif choice == 4:
        break

print("Thank you for using our ATM!")