
# find the root of the equation  root of a polynomial f(x) = anxn + an−1xn−1 + ... + a1x + a0 using Bisection method

x_l = -1
x_u = -2
epsilon_s = -2
x_true = -1
coefficients = []
maxitr = 0


def func(x):
    i = 0
    fun = 0
    while i <= n:
        fun = fun + coefficients[i] * (x**i)
        i = i+1
    return fun


def bisection(a, b):
    epsilon_a = 9999
    count = 0
    x_r = -1
    while (count < maxitr) and (epsilon_a >= epsilon_s):
        x_r = float((a+b)/2)
        epsilon_a = float(abs((b - a)/(a + b)))
        epsilon_t = float(abs((x_true - x_r)/x_true))
        print(" x_l = ", a, " x_u = ", b, " x_r = ", x_r, " epsilon_a = ", epsilon_a, " epsilon_t = ", epsilon_t)
        if (func(a) * func(x_r)) < 0:
            b = x_r
        elif (func(a) * func(x_r)) > 0:
            a = x_r
        elif func(a)*func(x_r) == 0:
            return x_r
        count = count + 1
    return x_r


def main():

    # Taking inputs
    global n
    n = int(input("Highest degree of F(X) : "))

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

    global coefficients
    coefficients = []
    print("a list of floats : ")
    for i in range(n+1):
        data = int(input())
        coefficients.append(data)

    ans = bisection(x_l, x_u)
    print("The estimated root is = ", ans)


if __name__ == '__main__':
    main()
