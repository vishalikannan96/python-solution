#Write a function named using_only() that takes a word and a string of letters, and that returns True
# if the word contains only letters in the list. Can you make a sentence using only the letters acefhlo?
# Other than "Hoe alfalfa?"

def using_only(word,str_list):
    for char in word:
        if char not in str_list:
            return False
        else:
            return True

word=input('Enter word:')
sentence='acefhlo'
str_list=list(sentence)
print(using_only(word,str_list))

