#Write a function isIn() that accepts two strings as arguments and returns True if either string occurs
# anywhere in the other, and False otherwise. Hint: you might want to use the built-in str operation in.

def isIn(a,b):
    if str1 in str2 or str2 in str1:
      return True
    else:
      return False
str1=str(input())
str2=str(input())
x=isIn(str1,str2)
if x is True:
    print("true")
else:
    print("false")

