#Write a program that asks the user to input 10 integers, and then prints the largest odd number that
# was entered. If no odd number was entered, it should print a message to that effect.

list1=[]
list2=[]
max1 = 0
for i in range(1,11):
    x=int(input())
    if x % 2 != 0:
        list1.append(x)
print(list1)
#sum = max(list1)
#print(sum)
for i in list1:
    if i>max1:
        max1=i
if max1>0:
    print(max1)
else:
    print("no odd large num")