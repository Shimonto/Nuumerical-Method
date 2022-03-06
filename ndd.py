import numpy
import matplotlib.pyplot as pt

X = []
size = int(input("Size of array : "))
print("Enter Data for X : ")
for i in range(size):
    X.append(float(input()))
X = numpy.array(X)


Fx = []
print("Enter Data for Fx : ")
for i in range(size):
    Fx.append(float(input()))
Fx = numpy.array(Fx)


order = numpy.shape(Fx)[0]
coeff = numpy.zeros([order, order])
coeff[::, 0] = Fx
for i in range(1, order):
    for j in range(order-i):
        coeff[j][i] = (coeff[j+1][i-1] - coeff[j][i-1]) / (X[j+i] - X[j])
B = coeff[0]


poly = numpy.polynomial.Polynomial([0.])
n = B.shape[0]
for i in range(n):
    p = numpy.polynomial.Polynomial([1.])
    for j in range(i):
        q = numpy.polynomial.Polynomial([-X[j], 1])
        p = numpy.polymul(p, q)
    p = p * B[i]
    poly = numpy.polyadd(poly, p)
eq = numpy.flip(poly[0].coef, axis=0)
print(eq)


x = numpy.linspace(min(X), max(X))
y = numpy.polyval(eq, x)
pt.plot(x, y)
pt.show()

#input 1.8 5 6 8.2 9.2 12 5.4375 7.3516 16.415 4 21.24 8

