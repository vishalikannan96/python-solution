#Write a function called has_no_e that returns True if the given word doesn’t have the letter "e" in it.

def has_no_e(s):
    if "e" in s:
        return True
    else:
        return False
print(has_no_e(str(input())))
