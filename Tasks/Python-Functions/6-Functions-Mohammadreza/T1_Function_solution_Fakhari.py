import math

def fibonacci(n):
    if n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)
    elif n == 1:
        return 0
    else:
        return 1

def maghloob(a):
    if a == 0:  
        print("0 ", end="")
        return
        
    tenpow = 1
    counter = 0
    while tenpow <= a:
        counter += 1
        tenpow *= 10
    
    digits = []
    temp = a
    for _ in range(counter):
        digits.append(temp % 10)
        temp //= 10
    digits.reverse() 
    
    for i in range(counter // 2):
        digits[i], digits[counter - 1 - i] = digits[counter - 1 - i], digits[i]
    
    reversed_num = 0
    for digit in digits:
        reversed_num = reversed_num * 10 + digit
    
    print(f"{reversed_num} ", end="")

def main():
    n = int(input())
    for i in range(1, n + 1):
        k = fibonacci(i)
        maghloob(k)
    print()  

if __name__ == "__main__":
    main()