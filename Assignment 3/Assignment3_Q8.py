rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

matrix = []

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(rows):
    sum = 0
    for j in range(cols):
        sum = sum + matrix[i][j]
    print("Sum of row", i+1, "=", sum)