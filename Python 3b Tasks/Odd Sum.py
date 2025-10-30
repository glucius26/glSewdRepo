num = int(input("insert number:"))
total = 0
for i in range(1, num + 1, 2):
    total += i
print(f"The sum of odd numbers from 1 to {num} is {total}")