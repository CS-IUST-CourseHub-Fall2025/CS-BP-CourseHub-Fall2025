def remove_zeros(num: int) -> int:
    result = 0
    product = 1
    
    while num > 0:
        digit = num % 10
        if digit != 0:
            result += digit * product
            product *= 10
        num //= 10
    
    return result

def after_removing_zeros(a: int, b: int, c: int) -> bool:
    a_with_no_zeros = remove_zeros(a)
    b_with_no_zeros = remove_zeros(b)
    c_with_no_zeros = remove_zeros(c)
    
    return (a_with_no_zeros + b_with_no_zeros) == c_with_no_zeros

def main() -> None:
    a, b = map(int, input().split())
    c = a + b
    
    if after_removing_zeros(a, b, c):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()