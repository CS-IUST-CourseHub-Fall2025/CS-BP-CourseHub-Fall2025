x1 = float(input())
x2 = float(input())
x3 = float(input())
x4 = float(input())
x5 = float(input())

f1 = int(input())
f2 = int(input())
f3 = int(input())
f4 = int(input())
f5 = int(input())

f_sum = f1 + f2 + f3 +f4 +f5

mean = ((x1 * f1) + (x2 * f2) + (x3 * f3) + (x4 * f4) + (x5 * f5)) / f_sum

var = (f1 * ((x1 - mean)**2) + f2 * ((x2 - mean)**2) + f3 * ((x3 - mean)**2) + f4 * ((x4 - mean)**2) + f5 * ((x5 - mean)**2)) / f_sum

print(round(var,2))
print(var > 1000)


