def take_gold(list):
    if list[0] >= list[-1]:
        return (list[1:], list[0])

    else:
        return (list[: (len(list) - 1) :], list[-1])


n = int(input())
players = [0] * n
queue = list(map(int, input().split()))
turn = 0

while queue:
    (queue, taken_gold) = take_gold(queue)
    players[turn] += taken_gold
    turn = (turn + 1) % n

print(players)
