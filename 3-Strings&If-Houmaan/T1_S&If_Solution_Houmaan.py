a = int(input())
b = int(input())

h = 0
m = 0

if a == 0:
    h = 0
elif a == 1:
    h = 11
elif a == 2:
    h = 10
elif a == 3:
    h = 9
elif a == 4:
    h = 8
elif a == 5:
    h = 7
elif a == 6:
    h = 6
elif a == 7:
    h = 5
elif a == 8:
    h = 4
elif a == 9:
    h = 3
elif a == 10:
    h = 2
elif a == 11:
    h = 1

if b == 0:
    m = 0
else:
    m = 60 - b

print(f"{h:02d}:{m:02d}")
