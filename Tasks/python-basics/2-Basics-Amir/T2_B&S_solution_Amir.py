data = input().split()
res = ''
for sub_str in data:
    if len(sub_str) >= 5:
        res += f"{sub_str[::-1]} "
    else:
        res += f"{sub_str} "

print(res.strip())