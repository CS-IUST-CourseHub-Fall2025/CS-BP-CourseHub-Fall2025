num = input().strip()
check_sum = int(num[-1])

total = (
    int(num[0]) * 10
    + int(num[1]) * 9
    + int(num[2]) * 8
    + int(num[3]) * 7
    + int(num[4]) * 6
    + int(num[5]) * 5
    + int(num[6]) * 4
    + int(num[7]) * 3
    + int(num[8]) * 2
)
remainder = total % 11

if (check_sum == remainder and remainder in (0, 1)) or (11 - remainder == check_sum):
    print("yes")
else:
    print("no")
