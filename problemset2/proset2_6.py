# Implement a function that satisfies the specification. Use a try-except block.
# def findAnEven(l):
# def findAnEven(l):
# Assumes l is a list of integers
# Returns the first even number in l
# Raises ValueError if l does not contain an even number

def findAnEven(l):
    try:
        for i in l:
            if i % 2 == 0:
                return i
        else:
            raise ValueError

    except ValueError:
        print('Plz enter valid input')

l = []
for index in range(1,5):
    x=int(input())
    l.append(x)
print(findAnEven(l))
