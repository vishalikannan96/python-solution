#Write a function called eval_loop that iteratively prompts the user, takes the resulting input and
# evaluates it using eval, and prints the result. It should continue until the user enters 'done', and
# then return the value of the last expression it evaluated.

def eval_loop(val1):
    return eval(val1)
res=''
while True:
    string1=input()
    if string1=="done":
        break
    else:
        res=eval(string1)
        print(res)
print(res)