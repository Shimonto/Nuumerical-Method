import sympy
from sympy import symbols
from numpy import linspace
from sympy import lambdify
import matplotlib.pyplot as p


X = []
Fx = []

size = int(input("Size of array : "))
print("Enter Data for X : ")
for i in range(size):
    X.append(float(input()))

print("Enter Data for Fx : ")
for i in range(size):
    Fx.append(float(input()))


def fun(x, y):
    X = sympy.symbols('X')
    eq = 0
    for i in range(len(x)):
        t = 1
        for j in range(len(x)):
            if j != i:
                t = t * ((X-x[j])/(x[i]-x[j]))
        eq = eq + (t*y[i])
    return eq

#x = [1.8,5,6,8.2,9.2,12]
#y = [5.4375,7.3516,16.415,4,21.24,8]


equation = fun(X, Fx)
print(equation)


symbol = symbols('X')
func = lambdify(symbol, equation)
xn = linspace(min(X), max(X))
yn = func(xn)
print(yn)
p.plot(xn, yn)
p.show()

#from sympy import plot
#plot(b,(a,1,13))
#mpl.show()
