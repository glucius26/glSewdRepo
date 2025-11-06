product = 1
count = 1
total = 0
num = int(input("Enter Number: "))
while count <= num:
    product = count * product
    count += 1

print(f"Factorial of 5 is: {product}")