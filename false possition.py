# find the root of the equation  root of a polynomial f(x) = anxn + an−1xn−1 + ... + a1x + a0 using Bisection method
import math

x_l = -1
x_u = -2
epsilon_s = -2
x_true = -1
coefficients = []
maxitr = 0


def func(x):
    fun = float(math.cos(x) - x)
    return fun


def falseposition(a, b):
    epsilon_a = 9999
    count = 1
    x_r = -1
    while (count <= maxitr) and (epsilon_a >= epsilon_s):
        x_r = float(b - ((func(b) * (a - b)) / (func(a) - func(b))))
        epsilon_a = float(abs((b - a) / (a + b)))
        epsilon_t = float(abs((x_true - x_r) / x_true))
        print(" iteration ", count, ":  x_l = ", a, " x_u = ", b, " x_r = ", x_r, " epsilon_a = ", epsilon_a, " epsilon_t = ", epsilon_t)
        if (func(a) * func(x_r)) < 0:
            b = x_r
        elif (func(a) * func(x_r)) > 0:
            a = x_r
        elif func(a) * func(x_r) == 0:
            return x_r
        count = count + 1
    return x_r


def main():

    global x_l
    x_l = float(input("initial lower bound : "))

    global x_u
    x_u = float(input("initial upper bound : "))

    global maxitr
    maxitr = int(input("max no of iterations allowed : "))

    global epsilon_s
    epsilon_s = float(input("error tolerance :"))

    global x_true
    x_true = float(input("true value : "))

    root = falseposition(x_l, x_u)
    print("The estimated root is = ", root)


if __name__ == '__main__':
    main()
