#Write a program that examines three variables—x, y, and z— and prints the largest odd number among them.
#If none of them   are odd, it should print a message to that effect.
x=int(input())
y=int(input())
z=int(input())
list1=[]
max=0
if x%2!=0:
    list1.append(x)
if y%2!=0:
    list1.append(y)
if z%2!=0:
    list1.append(z)
for i in list1:
    if i>max:
        max=i
if max>0:
    print(max)
else:
    print("no odd large num")
