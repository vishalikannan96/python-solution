#A string slice can take a third index that specifies the "step size;" that is, the number of spaces
# between successive characters. A step size of 2 means every other character; 3 means every third, etc.
#A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string.
# Use this idiom to write a one-line version of is_palindrome

def is_palindrome(string):
    cp_string=string[::-1]
    if cp_string==string:
        return True
    else:
        return False
print(is_palindrome(str(input())))