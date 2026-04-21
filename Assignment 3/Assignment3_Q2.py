lst = input("Enter elements: ").split()

rev = []
i = len(lst) - 1

while i >= 0:
    rev.append(lst[i])
    i = i - 1

print("Reversed list:", rev)