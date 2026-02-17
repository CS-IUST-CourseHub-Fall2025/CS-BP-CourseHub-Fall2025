def bmm(a: int, b: int) -> int:
    o = 1
    c, d = a, b
    for i in range(1, min(a, b) + 1):
        if c % i == 0 and d % i == 0:
            o *= i
            c //= i
            d //= i
    return o

def kmm(a: int, b: int) -> int:
    return (a * b) // bmm(a, b)

def main() -> None:
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        result = 2 * (kmm(a, b) - bmm(a, b))
        print(result)

if __name__ == "__main__":
    main()