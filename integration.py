import math

def integrate(a, b, div, lamda, R, r): #integrates and computes an approximate value for the integral (2*lambda*R*(r - R*cos(theta)) d.theta)/(R^2 + r^2 + 2*R*r*cos(theta))^(3/2)
    width = (b-a)/div
    sum = 0
    for i in range(div):
        sum = sum + width*((2*lamda*R*(r - R*math.cos(i*width)) )/(R**2 + r**2 - 2*R*r*math.cos((i+0.001)*width))**(3/2))
    return sum


lamda = int(input('Enter the value of lambda: '))
R = int(input('Enter the value of R: '))
div = int(input('Enter the number of divisions you want your program to calculate the integration for, Remember, more the divisions more is the running time!!: '))





f = open("datapoints-integrals.txt", "w")
for i in range(10000):
	f.write(str(2*i*R/10000))
	f.write(" ")
	f.write(str(integrate(0,math.pi,div,lamda,R,(i+0.001)*R*2/10000)))
	f.write('\n')
f.close()
