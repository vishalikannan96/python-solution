#Write both a nonrecursive and recursive function that displays the rows of asterisks given below,
#            **
#	        ****
#          ******
#        **********
#       ************
#      **************



def partten(n):
    j=2
    for i in range(n,0,-1):
        print(i*" ",j*"*")
        j+=2
partten(7)

j=2
def partten(n):
    global j
    print(n*" ",j*"*")
    if j<14:
        j+=2
        partten(n-1)
partten(7)




