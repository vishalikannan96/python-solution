#Write a function named avoids that takes a word and a string of forbidden letters, and that returns
# True if the word doesn’t use any of the forbidden letters.

def avoid(string,forbidden_str):
    for i in string:
        if forbidden_str in string:
            return True
    else:
        return False
string=str(input('Enter string:'))
forbidden_str=str(input('Enter forbidden string:'))
print(avoid(string,forbidden_str))