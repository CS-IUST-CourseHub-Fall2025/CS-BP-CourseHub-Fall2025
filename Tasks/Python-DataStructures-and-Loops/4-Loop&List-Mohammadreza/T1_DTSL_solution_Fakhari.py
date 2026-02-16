def main():
    target = int(input())
    holder = target
    inverse = 0
    while holder > 0:
        inverse = inverse * 10 + holder % 10
        holder //= 10
    if target == inverse:
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")

if __name__ == "__main__":
    main()