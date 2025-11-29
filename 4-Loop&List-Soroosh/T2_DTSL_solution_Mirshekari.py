import math

def main():
    # خواندن همه ورودی‌ها در یک خط و جدا کردن آنها
    input_line = input().split()
    n = int(input_line[0])
    size = int(input_line[1])
    c = input_line[2]
    
    count = int(math.log10(n))
    
    for digit_index in range(count, -1, -1):
        temp = n
        temp_index = digit_index
        while temp_index > 0:
            temp //= 10
            temp_index -= 1
        digit = str(temp % 10)
        
        if digit == '0':
            for i in range(1, size + 1):
                if i == 1 or i == size:
                    print(c * size)
                else:
                    print(c + ' ' * (size - 2) + c)
        elif digit == '1':
            for i in range(1, size + 1):
                print(' ' * (size - 1) + c)
        elif digit == '2':
            for i in range(1, size + 1):
                if i == 1 or i == (size // 2) + 1 or i == size:
                    print(c * size)
                elif i > 1 and i < (size // 2) + 1:
                    print(' ' * (size - 1) + c)
                else:
                    print(c + ' ' * (size - 1))
        elif digit == '3':
            for i in range(1, size + 1):
                if i == 1 or i == (size // 2) + 1 or i == size:
                    print(c * size)
                else:
                    print(' ' * (size - 1) + c)
        elif digit == '4':
            for i in range(1, size + 1):
                if i <= (size // 2):
                    print(c + ' ' * (size - 2) + c)
                elif i == (size // 2) + 1:
                    print(c * size)
                else:
                    print(' ' * (size - 1) + c)
        elif digit == '5':
            for i in range(1, size + 1):
                if i == 1 or i == (size // 2) + 1 or i == size:
                    print(c * size)
                elif i > 1 and i < (size // 2) + 1:
                    print(c + ' ' * (size - 1))
                else:
                    print(' ' * (size - 1) + c)
        elif digit == '6':
            for i in range(1, size + 1):
                if i == 1 or i == (size // 2) + 1 or i == size:
                    print(c * size)
                elif i > 1 and i < (size // 2) + 1:
                    print(c + ' ' * (size - 1))
                else:
                    print(c + ' ' * (size - 2) + c)
        elif digit == '7':
            for i in range(1, size + 1):
                if i == 1:
                    print(c * size)
                else:
                    print(' ' * (size - 1) + c)
        elif digit == '8':
            for i in range(1, size + 1):
                if i == 1 or i == (size // 2) + 1 or i == size:
                    print(c * size)
                else:
                    print(c + ' ' * (size - 2) + c)
        elif digit == '9':
            for i in range(1, size + 1):
                if i == 1 or i == (size // 2) + 1 or i == size:
                    print(c * size)
                elif i > 1 and i < (size // 2) + 1:
                    print(c + ' ' * (size - 2) + c)
                else:
                    print(' ' * (size - 1) + c)
        print()

if __name__ == "__main__":
    main()