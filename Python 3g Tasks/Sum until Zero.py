flag = True
tSum = 0

while flag == True:
    num = int(input("Enter a number (0 to stop)"))
    if num != 0:
        tSum += num
    else:
        flag = False

print(f"Total Sum: {tSum}")