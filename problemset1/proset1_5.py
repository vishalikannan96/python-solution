#Write a program that asks the user to enter an integer and prints two integers, root and pwr, such
# that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no such pair of integers
# exists, it should print a message to that effect.
num=int(input())
for i in range(1,6):
    a = (num**(1/i))
    if round(a)==a:
        print(a,i)
