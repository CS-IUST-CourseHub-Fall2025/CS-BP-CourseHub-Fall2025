def take_gold(list):
    if len(list) < 1:
        return
    print(list)
    if list[0] >= list[-1]:
        take_gold(list[1:])
    else:
        take_gold(list[: (len(list) - 1) :])


queue = list(map(int, input().split()))
ans = take_gold(queue)
