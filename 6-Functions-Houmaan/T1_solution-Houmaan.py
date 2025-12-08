import math

def is_odd(n):
    if n % 2 == 0:
        return False
    else:
        return True

def is_prime(n):
    if n < 2:
        return False
    r = int(math.sqrt(n))
    for i in range(2, r + 1):
        if n % i == 0:
            return False
    return True

def prime_divisors_amount(n):
    result = 0
    for i in range(2, n + 1):
        if n % i == 0:
            if is_prime(i):
                result += 1
    return result

def is_bodd(n):
    if is_odd(n):
        pda = prime_divisors_amount(n)

        for i in range(2, n + 1):
            if n % i == 0:
                if is_prime(i):
                    if pda == i:
                        return True
    return False

def all_bodds(n):
    result = 0
    for i in range(3, n + 1):
        if is_bodd(i):
            result += i
    return result


inp = input()
if inp.strip():
    n = int(inp)
    
    total_sum = all_bodds(n)

    if total_sum == 0:
        print("NOT FOUND!")
    else:
        number = total_sum
        reverse = 0
        while number != 0:
            digit = number % 10
            reverse = (reverse * 10) + digit
            number //= 10
        
        print(reverse)
