"""Implement a function that meets the specification below. Use a try-except block.
def sumDigits(s):
	Assumes s is a string
	#Returns the sum of the decimal digits in s
	#For example, if s is 'a2b3c' it returns 5"""
import re
def sumDigits(s):
    sum=0
    try:
        if re.findall('[0-9]',s):
            s=list(s)
            for i in s:
                if i.isdigit():
                    sum=sum+int(i)
            print(sum)
        else:
            raise ValueError
    except ValueError:
        print("Plz enter valid string")
s=str(input())
sumDigits(s)