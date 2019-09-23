#Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function
# called is_anagram that takes two strings and returns True if they are anagrams.
def is_anagram(str1,str2):
    str1=list(sorted(str1))
    str2=list(sorted(str2))
    if str1==str2:
        return True
    else:
        return False
str1=str(input('Enter string1:'))
str2=str(input('Enter string2:'))
print(is_anagram(str1,str2))