collection = []
quantity = int(input("How many triangles?"))
for i in range(1, quantity + 1):
    base = int(input("Enter Base:"))
    height = int(input("Enter Height:"))
    area = 0.5 * base * height
    collection.append(area)
total = sum(collection)
print(f"Total area of all triangles: {total}")