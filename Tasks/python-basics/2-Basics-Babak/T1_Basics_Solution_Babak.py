a = int(input("لطفاً عدد اول (a) را وارد کنید: "))
b = float(input("لطفاً عدد دوم (b) را وارد کنید: "))
text = input("لطفاً یک متن وارد کنید: ")

sum = a + b
multiply = a * b
divide = a // b
power = a ** 2

print("\nنتایج محاسبات هومان:")
print(f"جمع: {sum} (نوع: {type(sum)})")
print(f"ضرب: {multiply} (نوع: {type(mulltiply)})")
print(f"تقسیم صحیح: {divide} (نوع: {type(divide)})")
print(f"توان: {power} (نوع: {type(power)})")
print(f"متغیر متن: {text} (نوع: {type(text)})")
