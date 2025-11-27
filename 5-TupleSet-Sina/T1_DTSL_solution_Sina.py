s = input()
s = s[::-1]

for i in range(len(s) + 1):
    print(s[:-i] + s[-i] * i)
