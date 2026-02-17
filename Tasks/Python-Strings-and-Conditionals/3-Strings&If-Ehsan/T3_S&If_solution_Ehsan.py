a = int(input())
v0 = int(input())
x0 = int(input())
xd = int(input())
hour, minute, second = map(int, input().split(":"))

starting_time = hour * 3600 + minute * 60 + second

if (a != 0):
    A = 1/2 * a
    B = v0
    C = x0 - xd
    delta = (B ** 2) - (4 * A * C) 
    t1 = ((-B) - (delta ** 0.5)) / (2 * A)
    t2 = ((-B) + (delta ** 0.5)) / (2 * A)

    if (delta < 0):
        print("IMPOSSIBLE")
        exit()
    elif ((t1 < 0) and (t2 < 0)):
        ending_time = starting_time + max(t1, t2)
    else:
        if ((t1 < 0) or (t2 < 0)):
            ending_time = starting_time + max(t1, t2)
        else:
            ending_time = starting_time + min(t1, t2)
else:
    t = (xd - x0) / v0
    ending_time = starting_time + t

h = int(ending_time // 3600) % 24
m = int((ending_time % 3600) // 60)
s = int(ending_time % 60)


print(f"{h:02d}:{m:02d}:{s:02d}")

