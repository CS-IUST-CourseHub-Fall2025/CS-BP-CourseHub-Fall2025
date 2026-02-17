import math

def decimal(s):
    decimal_val = 0
    flag = 0
    
    if s[0] == '-':
        # Remove the minus sign
        s = s[1:]
        flag = 1
    
    if len(s) == 3:
        for i in range(3):
            if ord(s[i]) > 64:
                s_val = ord(s[i]) - 55
            else:
                s_val = ord(s[i]) - 48
            decimal_val += s_val * (16 ** (2 - i))
        if flag == 1:
            decimal_val = 0 - decimal_val
        return decimal_val
    elif len(s) == 2:
        for i in range(2):
            if ord(s[i]) > 64:
                s_val = ord(s[i]) - 55
            else:
                s_val = ord(s[i]) - 48
            decimal_val += s_val * (16 ** (1 - i))
        if flag == 1:
            decimal_val = 0 - decimal_val
        return decimal_val
    else:
        for i in range(1):
            if ord(s[i]) > 64:
                s_val = ord(s[i]) - 55
            else:
                s_val = ord(s[i]) - 48
            decimal_val += s_val * (16 ** 0)
        if flag == 1:
            decimal_val = 0 - decimal_val
        return decimal_val

def hex_func(a):
    s = ""
    if a < 0:
        s = s + '-'
        a = 0 - a
    
    n = 1
    counter = 0
    while n <= a:
        n *= 16
        counter += 1
    
    m = counter
    while counter > 0:
        number = a // (16 ** (counter - 1))
        a = a - number * (16 ** (counter - 1))
        if number <= 9:
            b = chr(number + 48)
            s = s + b
        else:
            b = chr(number + 55)
            s = s + b
        counter -= 1
    
    return s

def f(x):
    result = math.ceil(
        math.sin(math.cosh(math.pow(x, 1/3))) + 
        math.exp(math.atan(x)) - 
        math.log2(abs(x)) + 
        math.pow(x**2, 1/3)
    )
    return result

def g(x):
    result = math.floor(
        math.pow(f(x * x), 0.75) + 
        1 / (x + 10)
    )
    return result

def main():
    s = input()
    x = decimal(s)
    resultf = f(x)
    resultg = g(x)
    hexf = hex_func(resultf)
    hexg = hex_func(resultg)
    print(f"{hexf}\n{hexg}")

if __name__ == "__main__":
    main()