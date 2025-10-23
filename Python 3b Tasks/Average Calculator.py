quantity = int(input("How many numbers to process?"))
database = []
for i in range(1, quantity + 1):
    database.append(int(input(f"Enter Number {i}:")))
total = sum(database) / quantity
print(f"The average is {total}")