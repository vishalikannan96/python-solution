#A palindrome is a word that is spelled the same backward and forward, like "Malayalam" and "Noon" .
# Recursively, a word is a palindrome if the first and last letters are the same and the middle is a
# palindrome. Write a function called is_palindrome that takes a string argument and returns True if it is
# a palindrome and False otherwise. Remember that you can use the built-in function len to check the length
# of a string.Use the function definition

def is_Palindrome(s):
   if len(s) <= 1 :
      return True
   if s[0] == s[len(s) - 1] :
      return is_Palindrome(s[1:len(s)-1])
   else :
      return False
s=str(input())
s1=""
for i in s:
    if i.isalpha():
        s1+=i
s2=s1.lower()
print(is_Palindrome(s1))
