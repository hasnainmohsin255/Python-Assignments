rows = int(input("Enter rows of first matrix: "))
cols = int(input("Enter columns of first matrix: "))
cols2 = int(input("Enter columns of second matrix: "))

print("Enter first matrix:")
A = []
for i in range(rows):
    A.append(list(map(int, input().split())))

print("Enter second matrix:")
B = []
for i in range(cols):
    B.append(list(map(int, input().split())))

result = []

for i in range(rows):
    row = []
    for j in range(cols2):
        sum = 0
        for k in range(cols):
            sum = sum + A[i][k] * B[k][j]
        row.append(sum)
    result.append(row)

print("Result:")
for r in result:
    print(r)