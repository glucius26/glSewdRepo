import random
flag = True
collection = []
count = 1

while flag == True:
    num = random.randint(1, 49)
    if num not in collection:
        collection.append(num)
    count += 1
    if count == 8:
        flag = False
print("Your lottery numbers: ", end="")

for value in collection:
    print(f"{value} ", end="")