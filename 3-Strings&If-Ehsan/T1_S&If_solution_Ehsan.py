before, after = input().split()

if (len(after) != len(before)):
    print("IMPOSSIBLE")
    exit()

f1 = before.find('>')
b1 = before.find('<')
f2 = after.find('>')
b2 = after.find('<')

if (f1 != -1 and f2 != -1 and f2 < f1):
    print("IMPOSSIBLE")
    exit()

if (b1 != -1 and b2 != -1 and b2 > b1):
    print("IMPOSSIBLE")
    exit()

if (f1 != -1 and b1 != -1 and f2 != -1 and b2 != -1):
    if (f1 < b1 and f2 > b2):
        print("IMPOSSIBLE")
        exit()

print("POSSIBLE")
    
