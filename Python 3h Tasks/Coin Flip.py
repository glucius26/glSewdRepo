import random
flag = True
count = 0
heads = 0
tails = 0
midway = []

print("Flipping a coin 20 times...")

while flag == True:
    flip = random.randint(0,1)
    count += 1
    if flip == 0:
        heads += 1
        midway.append("H")
    else:
        tails += 1
        midway.append("T")
    if count == 20:
        flag = False

for value in midway:
    print(value, end=" ")
print()
print(f"Heads: {heads}")
print(f"Tails: {tails}")