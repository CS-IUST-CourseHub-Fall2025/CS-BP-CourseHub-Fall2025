# مدیریت پارکینگ

آرمین به‌تازگی یک پارکینگ کوچک **سه‌طبقه** راه‌اندازی کرده است. **هر** طبقه **سه** جایگاه دارد و او می‌خواهد ورود و خروج خودروها را به‌صورت خودکار مدیریت کند.
آرمین می‌خواهد ورود هر خودرو را در اولین جای خالی (از طبقه‌ی اول به ترتیب تا طبقه‌ی سوم) ثبت کند و هنگام خروج، هزینه‌ی توقف را محاسبه کرده و جایگاه را خالی کند.
برای همین از شما خواسته است که توابع اصلی این سیستم را برای او بنویسید.

تاریخ ورود و خروج خودروها فقط یک **عدد** است که نشان‌دهنده‌ی روز می‌باشد. کافی است اختلاف آن‌ها را حساب کنید تا مدت توقف خودرو در پارکینگ مشخص شود.

---

# **توابع مورد نیاز**

شما باید سه تابع زیر را پیاده‌سازی کنید:

## تابع برای ورود خودرو
هنگام ورود خودرو فراخوانی می‌شود.

```
def enter_car(id, entry_date):
```



این تابع باید:

* با دریافت یک آیدی(رشته) و یک تاریخ ورود(عدد)
* اولین جای خالی را در ترتیب طبقات F1 → F2 → F3 پیدا کند
* خودرو را در آن جایگاه ثبت کند
* در صورت موفقیت، رشته‌ی زیر  را برگرداند، که عدد بعد از `F` بیانگر طبقه و عدد بعد از `S` بیانگر جایگاه در آن طبقه است.
```
car {id} is parked in {parking_slot}
```
parking_slot : جایگاهی که خودرو در آن پارک شده
```
car C1 is parked in F1S1
```
* F1S1 → طبقه اول، جایگاه اول
* F2S3 → طبقه دوم، جایگاه سوم


اگر پارکینگ کاملاً پر باشد، باید برگرداند:

```
parking lot is full!
```

---
## تابع برای خروج خودرو

هنگام خروج خودرو فراخوانی می‌شود.

```
def exit_car(id, exit_date):
```

این تابع باید:

* با دریافت آیدی(رشته) و تاریخ خروج(عدد)
* بررسی کند آیا این خودرو داخل پارکینگ ثبت شده است یا نه
* اگر وجود داشته باشد:

  * جایگاه را آزاد کند
  * هزینه توقف را با استفاده از calculate_fee محاسبه کند
  * و متن زیر را برگرداند:

```
parked in {parking_slot} with the fee of {amount}$
```
* parking_slot : جایگاهی که خودرو در آن پارک شده
* amount : میزان هزینه‌ی توقف که توسط تابع calculate_fee محاسبه می‌شود

اگر خودرو با این ID در پارکینگ وجود نداشت، باید برگرداند:

```
no such a car in the parking lot!
```

---

## تابع برای محاسبه‌ی هزینه

```
def calculate_fee(entry_date, exit_date):
```

هنگام خروج با دریافت تاریخ خروج میزان هزینه را محاسبه می‌کند و آن مقدار را برمی‌گرداند.


* تعداد روزهای توقف = اختلاف دو عدد (تاریخ ورود و تاریخ خروج)
* هزینه = تعداد روز × هزینه ثابت روزانه
* هزینه‌ی ثابت برابر با **10** دلار می‌باشد.

---

# ورودی

ورودی به شکل دستورات متنی است که هر خط یکی از دو نوع زیر است:

```
enter {id} {date}
exit {id} {date}
```

مثال:

```
enter C101 15
enter C102 16
exit C101 20
EOF
```

تا زمانی به دریافت ورودی ادامه دهید که به `EOF` برسید.

---

# خروجی

هر خط ورودی باید مطابق نمونه زیر پردازش شود:

ورودی :

```
enter C101 15
enter C102 16
exit C101 20
EOF
```
> نکته: ابتدا تمام دستورات را تا زمانی که به EOF برسید از ورودی دریافت کنید، سپس دستورات را به ترتیب به صورت زیر پردازش کنید:


```
print( enter_car("C101", 15) )
print( enter_car("C102", 16) )
print( exit_car("C101", 20) )
```
---

### ورودی نمونه 1
```
enter C101 10
enter C102 12
exit C101 15
exit C102 20
EOF
```
----------

### خروجی نمونه 1
```
car C101 is parked in F1S1
car C102 is parked in F1S2
parked in F1S1 with the fee of 50$
parked in F1S2 with the fee of 80$
```
----------

### ورودی نمونه 2
```
enter C10 5
enter C11 6
enter C12 7
exit C11 10
enter C13 11
EOF
```
----------

### خروجی نمونه 2
```
car C10 is parked in F1S1
car C11 is parked in F1S2
car C12 is parked in F1S3
parked in F1S2 with the fee of 40$
car C13 is parked in F1S2
```
---------



test case 1:

```
enter C1 1
enter C2 2
exit C1 5
exit C2 10
EOF
```

output 1:

```
car C1 is parked in F1S1
car C2 is parked in F1S2
parked in F1S1 with the fee of 40$
parked in F1S2 with the fee of 80$
```

test case 2:

```
enter C1 1
enter C2 2
enter C3 3
enter C4 4
enter C5 5
enter C6 6
enter C7 7
enter C8 8
enter C9 9
enter C10 10
EOF
```

output 2:

```
car C1 is parked in F1S1
car C2 is parked in F1S2
car C3 is parked in F1S3
car C4 is parked in F2S1
car C5 is parked in F2S2
car C6 is parked in F2S3
car C7 is parked in F3S1
car C8 is parked in F3S2
car C9 is parked in F3S3
parking lot is full!
```

test case 3:

```
enter C10 5
exit C99 8
enter C11 6
exit C10 9
EOF
```

output 3:

```
car C10 is parked in F1S1
no such a car in the parking lot!
car C11 is parked in F1S2
parked in F1S1 with the fee of 40$
```


test case 4:

```
enter C1 1
enter C2 2
enter C3 3
exit C2 5
enter C4 6
EOF
```

output 4:

```
car C1 is parked in F1S1
car C2 is parked in F1S2
car C3 is parked in F1S3
parked in F1S2 with the fee of 30$
car C4 is parked in F1S2
```

test case 5:

```
enter C1 1
enter C2 1
enter C3 1
enter C4 2
enter C5 2
exit C3 4
exit C1 5
enter C6 6
enter C7 7
EOF
```

output 5:

```
car C1 is parked in F1S1
car C2 is parked in F1S2
car C3 is parked in F1S3
car C4 is parked in F2S1
car C5 is parked in F2S2
parked in F1S3 with the fee of 30$
parked in F1S1 with the fee of 40$
car C6 is parked in F1S1
car C7 is parked in F1S3
```

test case 6:

```
enter M1 1
enter M2 2
enter M3 3
enter M4 4
enter M5 5
enter M6 6
exit M2 7
exit M5 8
enter N1 9
enter N2 10
enter N3 11
exit Z9 12
enter N4 13
enter N5 14
enter N6 15
enter N7 16
EOF
```

output 6:

```
car M1 is parked in F1S1
car M2 is parked in F1S2
car M3 is parked in F1S3
car M4 is parked in F2S1
car M5 is parked in F2S2
car M6 is parked in F2S3
parked in F1S2 with the fee of 50$
parked in F2S2 with the fee of 30$
car N1 is parked in F1S2
car N2 is parked in F2S2
car N3 is parked in F3S1
no such a car in the parking lot!
car N4 is parked in F3S2
car N5 is parked in F3S3
parking lot is full!
parking lot is full!
```

test case 7:

```
enter A 1
enter B 1
enter C 1
enter D 2
enter E 2
exit B 3
exit D 5
enter F 6
enter G 7
EOF
```

output 7:

```
car A is parked in F1S1
car B is parked in F1S2
car C is parked in F1S3
car D is parked in F2S1
car E is parked in F2S2
parked in F1S2 with the fee of 20$
parked in F2S1 with the fee of 30$
car F is parked in F1S2
car G is parked in F2S1
```

test case 8:

```
enter A1 1
enter A2 1
enter A3 1
enter A4 2
enter A5 2
enter A6 2
exit A4 5
exit A2 6
enter B1 7
enter B2 8
enter B3 9
enter B4 10
exit A6 11
enter B5 12
EOF
```

output 8:

```
car A1 is parked in F1S1
car A2 is parked in F1S2
car A3 is parked in F1S3
car A4 is parked in F2S1
car A5 is parked in F2S2
car A6 is parked in F2S3
parked in F2S1 with the fee of 30$
parked in F1S2 with the fee of 50$
car B1 is parked in F1S2
car B2 is parked in F2S1
car B3 is parked in F3S1
car B4 is parked in F3S2
parked in F2S3 with the fee of 90$
car B5 is parked in F2S3
```

test case 9:

```
enter C1 1
enter C2 2
enter C3 3
exit C1 4
exit C2 5
exit C3 6
enter C4 7
enter C5 8
exit C5 10
enter C6 12
EOF
```

output 9:

```
car C1 is parked in F1S1
car C2 is parked in F1S2
car C3 is parked in F1S3
parked in F1S1 with the fee of 30$
parked in F1S2 with the fee of 30$
parked in F1S3 with the fee of 30$
car C4 is parked in F1S1
car C5 is parked in F1S2
parked in F1S2 with the fee of 20$
car C6 is parked in F1S2
```

test case 10:

```
enter A1 1
enter A2 2
enter A3 3
enter A4 4
enter A5 5
enter A6 6
exit A2 10
exit A4 12
enter B1 13
enter B2 14
exit A1 15
exit A6 16
enter C1 17
enter C2 18
EOF
```

output 10:

```
car A1 is parked in F1S1
car A2 is parked in F1S2
car A3 is parked in F1S3
car A4 is parked in F2S1
car A5 is parked in F2S2
car A6 is parked in F2S3
parked in F1S2 with the fee of 80$
parked in F2S1 with the fee of 80$
car B1 is parked in F1S2
car B2 is parked in F2S1
parked in F1S1 with the fee of 140$
parked in F2S3 with the fee of 100$
car C1 is parked in F1S1
car C2 is parked in F2S3
```



