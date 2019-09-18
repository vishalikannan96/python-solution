#Write a program that computes the decimal equivalent of the binary number 10011?


def decimal_convertion(num1):
    sum=0
    power=0
    while(num1!=0):
        rem=num1%10
        ##print(rem)
        sum=sum+(rem*(2**power))
        num1=num1//10
        power+=1
    print(sum)

num=int(input())
decimal_convertion(num)
