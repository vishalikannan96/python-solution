#Let s be a string that contains a sequence of decimal numbers separated by commas, e.g.,
# s = '1.23,2.4,3.123'. Write a program that prints the sum of the numbers in s.

flag=0
s=str(input())
s1=s.split(",")
print(type(s1))
for i in s1:
    flag=flag+float(i)
print(flag)




