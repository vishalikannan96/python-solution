#Write a function called eval_loop that iteratively prompts the user, takes the resulting input and
# evaluates it using eval, and prints the result. It should continue until the user enters 'done', and
# then return the value of the last expression it evaluated.

def eval_loop(string1):
    res=''
    if string1=="done":
        return False
    else:
        res=eval(string1)
        return res
list1=[]
while True:
    string1=str(input())
    result=eval_loop(string1)
    if result != False:
        print(result)
        list1.append(result)
    else:
        print(list1[len(list1)-1])