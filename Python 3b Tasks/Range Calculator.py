lower= int(input("lower bound:"))
upper = int(input("upper bound:"))
total = lower
for i in range(lower, upper):
    total += i
total += lower
print(f"The sum of numbers from {lower} to {upper} is {total}")