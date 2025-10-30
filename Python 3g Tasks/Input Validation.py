while True:
    grade = int(input("Enter a grade from 0 - 100:"))
    if grade >= 0 and grade <= 100:
        print(f"You entered {grade}")
        break
    else:
        print("Invalid! Try again.")