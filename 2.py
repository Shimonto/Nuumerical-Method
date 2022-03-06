
n = int(input("Enter Number of equations : "))
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
Es = float(input("Enter Error Tolerance: "))
count = 1
Ea = 999
sum = 0
while count <= maxitr and Ea >= Es:
    print("\nIteration ", count, " :")
    for i in range(0, n):
        for j in range(0, i):
            sum = sum + A[i][j] * Xo[j]
        for j in range(i+1, n):
            sum = sum + A[i][j] * Xo[j]
        xi = float((B[i] - sum)/A[i][i])
        Ea = abs(float((xi-Xo[i]))/xi)
        print("X%d: "% count, "%.4f"% xi, " Ea:%.4f"% Ea)
        Xo[i] = xi
        sum = 0
    count = count + 1
    sum = 0
