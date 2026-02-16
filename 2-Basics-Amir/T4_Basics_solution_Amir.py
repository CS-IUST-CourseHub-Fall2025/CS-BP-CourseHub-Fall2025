a = float(input())
b = float(input())
c = float(input())

delta = b**2 - 4*a*c
x1 = (-b + delta**0.5) / (2*a)
x2 = (-b - delta**0.5) / (2*a)
print(f"First root: {round(min(x1, x2), 2)}")
print(f"Second root: {round(max(x1, x2), 2)}")