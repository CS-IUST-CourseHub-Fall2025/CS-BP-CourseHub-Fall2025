### 📘 **آغاز، میان، پایان**

محدودیت زمان: **۲ ثانیه**
محدودیت حافظه: **۲۵۶ مگابایت**

برنامه‌ای بنویسید که با دریافت یک رشته به طول سه یا بیشتر، بررسی کند:

چاپ شود yes اگر طول رشته زوج باشد، و حرف اول، حرف آخر، و 2 حرف وسط یکسان باشد

چاپ شود yes اگر طول رشته فرد باشد، و حرف اول، حرف آخر، و حرف وسط یکسان باشد-

بزرگی و کوچکی حروف در نظر گرفته نمیشود
a = A یعنی

چاپ شود no در غیر این دو صورت

---

### 🧩 **ورودی**

یک رشته شامل حروف انگلیسی کوچک و بزرگ.
رشته می‌تواند طولی بین ۱ تا ۱۰۰ داشته باشد.

---

### 🧾 **خروجی**

چاپ شود (no, yes) در یک خط یکی از دو مورد
به بزرگی و کوچیکی حروف دقت کنید

---

### 🔢 **ورودی نمونه ۱**

`AbA`

### 🖨️ **خروجی نمونه ۱**

`yes`

---

### 🔢 **ورودی نمونه ۲**

`AbabA`

### 🖨️ **خروجی نمونه ۲**

`no`

---

### 🔢 **ورودی نمونه ۳**

`zazbz`

### 🖨️ **خروجی نمونه ۳**

`yes`

```
Input:
abcba
Output:
no

Input:
abba
Output:
no

Input:
zazaz
Output:
yes

Input:
AaA
Output:
yes

Input:
abcdba
Output:
no
yaml

Input:
aaaa
Output:
yes

Input:
AaAa
Output:
yes

Input:
bBb
Output:
yes

Input:
abBA
Output:
no

Input:
xyzzyx
Output:
no

Input:
wowow
Output:
yes

Input:
xX
Output:
yes

Input:
maddam
Output:
no

Input:
ttttt
Output:
yes

Input:
AbCdEfG
Output:
no
```
