units = int(input("Enter units: "))

if units <= 100:
    bill = 0
elif units <= 200:
    bill = units * 5
else:
    bill = units * 10

print("Total bill =", bill)