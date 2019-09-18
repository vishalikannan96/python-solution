#Observe the following function definitions. They Calculate the Factorial as per the Mathematical
# definition 1! = 1 (n + 1)! = (n + 1) * n! Implement factI(n) as an Iterative Implementation & factR(n)
# as a Recursive Implementation


def factI(num):
    fact=1
    if num==0:
        return 1
    else:
        for index in range(1,num+1):
            fact=fact*index
    return fact
def factR(num):
    if num==0:
        return 1
    else:
        return num*factR(num-1)
num=int(input())
print(factI(num))
print(factR(num))