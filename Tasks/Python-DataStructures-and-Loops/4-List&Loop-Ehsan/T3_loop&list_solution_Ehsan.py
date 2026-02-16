s = input()
lst = list(s)

while(True):
    counter = 0
    i = 0
    while i < len(lst)-1:
        if (lst[i] == lst[i+1]):
            lst.pop(i)
            lst.pop(i)
            counter += 1
        else:
            i += 1
        
    if (counter == 0):
        break

print(''.join(lst))


#second solution
def CleanString(s):

    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return ''.join(stack)

