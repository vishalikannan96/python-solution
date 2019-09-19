#Write a function called rotate_word() that takes a string and an integer as parameters, and that returns
# a new string that contains the letters from the original string "rotated" by the given amount.
# For example, "cheer" rotated by 7 is "jolly" and "melon" rotated by -10 is "cubed". You might want to
# use the built-in functions ord, which converts a character to a numeric code, and chr, which converts
# numeric codes to characters.

def rotate(s,num,low,high):
    str1=" "
    for i in s:
        if num>0:
            x=ord(i)+num
            if x>high:
                y=low+(x-high)
                str1+=chr(y-1)
            else:
                str1+=chr(x)
        else:
            x=ord(i)-abs(num)
            if x<low:
                y=high-(low-x)
                str1+=chr(y+1)
            else:
                str1+=chr(x)
    print(str1)
num=int(input())
string1=str(input())
if string1.isupper():
    rotate(string1,num,65,90)
else:
    rotate(string1, num,97,122)