num = int(input("Choose a number:"))
product = 1
for i in range(1, num + 1):
    product = product * i
    print(i)
print(f"The factorial of {num} is {product}")