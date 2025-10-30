import random
flag = True
count = 1
result = []
print("Rolling a die 10 Times:")

while flag == True:
    dice = random.randint(1,6)
    count += 1
    result.append(dice)
    if count == 11:
        flag = False

print(result)