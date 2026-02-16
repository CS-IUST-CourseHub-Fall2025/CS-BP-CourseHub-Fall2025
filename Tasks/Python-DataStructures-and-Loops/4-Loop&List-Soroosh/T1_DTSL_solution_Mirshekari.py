import math

def main():
    # خواندن ورودی در یک خط و جدا کردن مقادیر
    input_values = input().split()
    x = float(input_values[0])
    n = int(input_values[1])
    answer = 0.0
    
    for i in range(1, n + 1):
        temp = (i * 2) - 1
        numerator = temp * (temp + 1) * (2 * temp + 1) / 6.0
        
        denominator = 0.0
        for j in range(1, i + 1):
            denominator += j * math.pow(x, j)
            
        result = (numerator / denominator) * math.pow(-1, i + 1)
        answer += result
        
    print("{:.5f}".format(answer))

if __name__ == "__main__":
    main()