#Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical
# order (double letters are ok). How many abecedarian words are there? (i.e) "Abhor" or "Aux" or "Aadil"
# should return "True" Banana should return "False"

'''def is_abecedarian(word):
    word=list(word)
    if word==sorted(word):
        return True
    else:
        return False'''

def is_abecedarian_fun(word):
    count=0
    print(word)
    list1=list(word)
    for i in range(len(list1)-1):
        if list1[i]<=list1[i+1]:
            count+=1
    if len(list1)==(count+1):
        return True
    else:
        return False
word=[]
for i in (1,4):
    x=input('Enter word:')
    word.append(x)
print(word)
for words in word:
    print(is_abecedarian_fun(words))

#print(is_abecedarian(word))



