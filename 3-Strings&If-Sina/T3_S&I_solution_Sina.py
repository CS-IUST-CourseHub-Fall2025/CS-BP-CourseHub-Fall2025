num = input().strip()
check_sum = int(num[-1])

x = 10
total = 0
for ch in num:
    total += int(ch) * x
    x -= 1

total -= check_sum
remainder = total % 11

if (check_sum == remainder and remainder in (0, 1)) or (11 - remainder == check_sum):
    print("yes")
else:
    print("no")
