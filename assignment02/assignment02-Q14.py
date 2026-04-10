age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
married = input("Marital status (Y/N): ")

if gender == 'F':
    print("Work in urban areas only")
elif gender == 'M':
    if 20 <= age <= 40:
        print("Work anywhere")
    elif 40 < age <= 60:
        print("Work in urban areas only")
    else:
        print("ERROR")