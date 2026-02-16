s = list(input().split())
check = list(input().split(" "))
ok = True
scnt = 0
cnt = 0
for c in s:
    if c == "Asteroid":
        continue
    scnt += 1
if scnt != len(check):
    print(False)
else:
    for c in s:
        if c == "Asteroid":
            continue
        if c[0] != check[cnt][0]:
            ok = False
            break
        cnt += 1
    print(ok)
