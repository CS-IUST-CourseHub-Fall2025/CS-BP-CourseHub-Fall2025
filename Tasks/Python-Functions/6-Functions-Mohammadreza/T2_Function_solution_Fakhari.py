import math

def fibonacci(n):
    if n > 2:
        return fibonacci(n-1)+fibonacci(n-2)
    elif n == 1:
        return 0
    else:
        return 1

def maghloob(a):
    tenpow = 1
    counter = 0
    while tenpow <= a:
        counter += 1
        tenpow *= 10
    
    for i in range(counter // 2):
        b = 10 ** (i+1)
        c = 10 ** (counter - i)
        num1 = (a % b) // (b // 10)
        num2 = (a % c) // (c // 10)
        a = a + (num1 - num2) * c // 10 + (num2 - num1) * b // 10
    
    print(a, end=" ")

def main():
    n = int(input())
    for i in range(1, n+1):
        k = fibonacci(i)
        maghloob(k)

if __name__ == "__main__":
    main()