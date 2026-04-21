lst = input("Enter numbers: ").split()

largest = lst[0]

for num in lst:
    if num > largest:
        largest = num

print("Largest number is:", largest)