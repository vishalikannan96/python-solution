#A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called
# is_power that takes parameters a and b and returns True if a is a power of b. Note: you will have
# to think about the base case.

def is_power(a,b):
    power=a/b
    i=1
    if a%b==0:
        for i in range(1,a):
            if b**i==a:
                return True
        else:
            return False
    else:
        return False
num1=int(input())
num2=int(input())
print(is_power(num1,num2))


