orderCost = float(input("How much was your order?"))
qO = str(input("Do you want express shipping(yes or no)?"))
checkO = 0.00

if qO == "yes":
    checkO = 10.00
elif qO == "YES":
    checkO = 10.00
elif qO == "Yes":
    checkO = 10.00
elif qO == "YEs":
    checkO = 10.00
elif qO == "YeS":
    checkO = 10.00
elif qO == "yES":
    checkO = 10.00
elif qO == "yEs":
    checkO = 10.00
elif qO == "yeS":
    checkO = 10.00
elif qO == "No":
    checkO == 0.00
elif qO == "no":
    checkO == 0.00
elif qO == "nO":
    checkO == 0.00
elif qO == "NO":
    checkO = 0.00
else:
    print("Invalid Response, defaulting to no. Restart the program if this is wrong.")
    
if orderCost < 50:
    shipping = 8.99
elif orderCost < 100:
    shipping = 4.99
else:
    shipping = 0.00


qT = str(input("Is this shipping international?(yes or no)"))

if qT == "yes":
    shipping = shipping * 2
elif qT == "YES":
    shipping = shipping * 2
elif qT == "Yes":
    shipping = shipping * 2
elif qT == "YEs":
    shipping = shipping * 2
elif qT == "YeS":
    shipping = shipping * 2
elif qT == "yES":
    shipping = shipping * 2
elif qT == "yEs":
    shipping = shipping * 2
elif qT == "yeS":
    shipping = shipping * 2
elif qT == "No":
    shipping = shipping
elif qT == "no":
    shipping = shipping
elif qT == "nO":
    shipping = shipping
elif qT == "NO":
    shipping = shipping
else:
    print("Invalid Response, defaulting to no. Restart the program if this is wrong.")
# print("DEBUG", shipping)

finalCalc = orderCost + checkO + shipping



# print("DEBUG", orderCost)
# print("DEBUG", checkO)
# print("DEBUG", shipping)

print("Original cost:", orderCost)
print("Shipping cost(multiplied by 2 for international):", shipping)
if checkO == 10:
    print("Express shipping fee: 10.00")
print("Your final total is:", finalCalc)
