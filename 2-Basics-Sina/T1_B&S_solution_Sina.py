s = input()
s = s.lower()

if len(s) == 0:
    print("no")
if len(s) % 2 == 1:
    mid = len(s) // 2
    if s[0] == s[mid] == s[-1]:
        print("yes")
    else:
        print("no")
else:
    mid1 = len(s) // 2 - 1
    mid2 = len(s) // 2
    if s[0] == s[mid1] == s[mid2] == s[-1]:
        print("yes")
    else:
        print("no")
