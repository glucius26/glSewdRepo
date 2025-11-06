name1 = str(input("First item: "))
price1 = float(input("Price: "))

name2 = str(input("Second item: "))
price2 = float(input("Price: "))

name3 = str(input("Third item: "))
price3 = float(input("Price: "))

tax1 = price1 * 0.06
tax2 = price2 * 0.06
tax3 = price3 * 0.06

print(f"{name1} costs ${price1} with tax ${round(tax1, 2)}")
print(f"{name2} costs ${price2} with tax ${round(tax2, 2)}")
print(f"{name3} costs ${price3} with tax ${round(tax3, 2)}")