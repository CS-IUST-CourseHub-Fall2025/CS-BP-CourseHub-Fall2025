n = int(input())
k = int(input())
people = [None] * n

for i in range(n):
    people[i] = i + 1

death_order = [None] * n
counter = 0

for i in range(n):
    counter = (counter + k - 1) % (n - i)
    death_order[i] = people[counter]
    del people[counter]

print(death_order)
print(f"Ainollah died in: {death_order.index(1) + 1}")