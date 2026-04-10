a = int(input("Enter age of person 1: "))
b = int(input("Enter age of person 2: "))
c = int(input("Enter age of person 3: "))

# Oldest
if a >= b and a >= c:
    oldest = a
elif b >= a and b >= c:
    oldest = b
else:
    oldest = c

# Youngest
if a <= b and a <= c:
    youngest = a
elif b <= a and b <= c:
    youngest = b
else:
    youngest = c

print("Oldest =", oldest)
print("Youngest =", youngest)