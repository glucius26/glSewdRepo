flag = True
tav = 0
i = 0

while flag == True:
    num = int(input("Enter a number (-1 to stop)"))
    if num != -1:
        tav += num
        i += 1
    else:
        flag = False

tav = tav / i

print(f"Average: {tav}")