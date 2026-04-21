lst = input("Enter elements: ").split()

first = lst[0]

i = 0
while i < len(lst) - 1:
    lst[i] = lst[i + 1]
    i = i + 1

lst[len(lst) - 1] = first

print("Rotated list:", lst)