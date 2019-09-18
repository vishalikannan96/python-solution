#One way of computing square roots is Newton’s method. Suppose that you want to know the square root of a.
# If you start with almost any estimate, x, you can compute a better estimate with the following
# formula: y = (x + a/x)/2

'''def newton_srquareroot(n):
    x=n
    for i in range(1,500):
        x=(x+(n/x))*0.5
    return x
num=int(input())
print(newton_srquareroot(num))'''

import math
import tabulate
def newton_squareroot(n):
    x=n
    for i in range(1,500):
        x=(x+(n/x))*0.5
    return x
def math_squareroot(n):
    y=math.sqrt(n)
    return y
print("{:^21}|{:^22}|{:^22}|{:^22}".format("number","newton's law","math_sqrt","difference"))
print("--------------------------------------------------------------------------------------------")
for i in range(1,10):
    new_sqrt=newton_squareroot(i)
    math_sqrt=math_squareroot(i)
    difference=abs(new_sqrt-math_sqrt)
    print("{:>20} | {:>20} | {:>20} | {:>20}".format(i,new_sqrt,math_sqrt,difference))
