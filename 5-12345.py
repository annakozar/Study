# In any language you would like, print the numbers from 1 to a given integer. For example for input: 5, the output is: 12345

li = []
def countdown(n):
    if n == 0:
        return             # Terminate recursion
    else:
        countdown(n - 1)   # Recursive call
        li.append(n)



countdown(5)
print(*li)