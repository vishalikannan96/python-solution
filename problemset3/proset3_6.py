#Modify your program to prompt the user to enter a string of forbidden letters and then print the number
# of words that don’t contain any of them. Can you find a combination of 5 forbidden letters that excludes
# the smallest number of words?

def avoid(list1,forbidden_str):
    for char in list1:
        count=0
        for letter in forbidden_str:
            if letter in char:
                count+=1
        if count==0:
            print(char)
string=str(input('Enter string:'))
list1=string.split(" ")
forbidden_str=str(input('Enter forbidden string:'))
avoid(list1,forbidden_str)