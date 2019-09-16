#Python provides a built-in function called len that returns the length of a string,
#so the value of len('Cigna') is 5. Write a function named right_justify that takes a string named s
# as a parameter and prints the string with enough leading spaces so that the last letter of the string
# is in column 70 of the display


def right_justify(str1):
    print(65*" "+str1)
    print(str1.rjust(65, " ")) #rjust() used for add space at the start of the string
str2=str(input())
right_justify(str2)