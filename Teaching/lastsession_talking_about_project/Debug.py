total = 0

def sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print("start")
print("in loop one")
total += sum(1,2,3,4)
print(total)
print("in loop two")
total += sum(5,6,7,8,9)
print(total)
print("End")
    