data = input()
n, new_data = data.split(':')
n = int(n)

a, b, c = map(float, new_data.split(','))

if round(c - b, 10) == round(b - a, 10):
    d = b - a
    a_n = a + (n - 1) * d
    total = (a + a_n) * n / 2
else:
    r = b / a
    total = a * (r ** n - 1) / (r - 1)

print("{:.2f}".format(total))