def main():
    n = int(input())
    temp_n = n
    b = 0
    count = 0
    counter = 1

    while n > 0:
        b += n % 10
        n = n // 10

    i = temp_n
    j = 0
    while True:
        i += 1
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1

        if count == 2 and counter == b:
            print(i)
            break
        elif count == 2:
            counter += 1

if __name__ == "__main__":
    main()