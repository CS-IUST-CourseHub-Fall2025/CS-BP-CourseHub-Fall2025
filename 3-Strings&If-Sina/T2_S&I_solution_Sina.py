a = input()
s = input()

if a.find(s[0]) + a.find(s[2]) + a.find(s[4]) >= a.find(s[1]) + a.find(s[3]):
    print("yes")
else:
    print("no")
