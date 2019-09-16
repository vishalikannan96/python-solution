#Implement a function that satisfies the specification. Use a try-except block.
try:
   vcet1=[1,2,3,4,7]
   vcet2=[2,4,5,0,8]
   for i in range(len(vcet1)):
       d=vcet1[i]/vcet2[i]
except Exception:
    print("divide by zero exception")
else:
    print(d)


