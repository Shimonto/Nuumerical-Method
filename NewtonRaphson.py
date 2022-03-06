import math

f = open("Input of NewtonRaphson.txt", "r")
z = open("newtonRaphsonAnswer.txt", "w")
k = float(f.readline())
w = float(f.readline())
xi = float(f.readline())
Es = float(f.readline())
maxitr = int(f.readline())
count = 1
Ea = 9999
xc = 0
while (count <= maxitr) and (Ea >= Es):
        p = float(8 * math.exp(-1 * k * xi)*math.cos(w*xi))
        q = float((-8 * k * math.exp(-1*k*xi)*math.cos(w*xi)) - (8*w*math.exp(-1*k*xi)*math.sin(w*xi)))
        xc = (xi - (p / q))
        Ea = abs(float(((xc - xi) / xc)))

        print("iteration ", count, " :  Xi :", xi, " Xi+1 : ", xc, ' Ea :', Ea)
        z.write("iteration %d" % count)
        z.write(" :  Xi : %.16f" % xi)
        z.write(" Xi+1 : %.16f" % xc)
        z.write(" Ea : %.16f \n" % Ea)
        xi = xc
        count = count+1
print("Value of root : ", xc)
z.write(" \nValue of Root : %.16f" % xc)
z.close()
f.close()