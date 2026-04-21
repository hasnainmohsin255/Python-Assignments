rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

print("Enter first matrix:")
A = []
for i in range(rows):
    A.append(list(map(int, input().split())))

print("Enter second matrix:")
B = []
for i in range(rows):
    B.append(list(map(int, input().split())))

result = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("Result:")
for r in result:
    print(r)