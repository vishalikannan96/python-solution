#Write a function called is_sorted that takes a list as a parameter and returns True if the list is
# sorted in ascending order and False otherwise. You can assume (as a precondition) that the elements of
# the list can be compared with the relational operators <, >, etc. For example, is_sorted([1,2,2]) should
# return True and is_sorted(['b','a']) should return False.

def is_sorted(list1):
    if list1==sorted(list1):
        return True
    else:
        return False
    
def is_sorted_fun(list1):
    count=0
    for i in range(len(list1) - 1):
        if list1[i] <= list1[i + 1]:
            count += 1
    if len(list1) == (count + 1):
        return True
    else:
        return False
list1=[]
for i in range(1,6):
    num=input("Enter value:")
    list1.append(num)
print(list1)
print(is_sorted(list1))
print(is_sorted_fun(list1))

