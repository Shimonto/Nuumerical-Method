n = int(input("Enter Number of equations : "))

print("Enter Coefficient Matrix : ")
A = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(float(input()))
    A.append(b)

print("Input constant value :")
B = []
for i in range(n):
    B.append(float(input()))

print("Initial values : ")
Xo = []
for i in range(n):
    Xo.append(float(input()))

maxitr = int(input("Enter Maximum iterations : "))

count = 1
sum = 0
z = []
while count <= maxitr:
    print("\nIteration ", count, " :")
    for i in range(n):
        for j in range(0, i-1):
            sum = sum + A[i][j] * Xo[j]
        for j in range(i+1, n):
            sum = sum + A[i][j] * Xo[j]
        xi = float((B[i] - sum)/A[i][i])
        z.append(xi)
        print("X%d: "% i, "%.4f"% xi)
        sum = 0
    for p in range(0, n):
        Xo[p] = z[p]
    z.clear()
    count = count + 1
    sum = 0