quantity = int(input("Enter quantity: "))
cost = quantity * 100

if cost > 1000:
    cost = cost - (cost * 0.10)

print("Total cost =", cost)