# چالش الفبا

امیررضا  همیشه با درس **زبان انگلیسی** مشکل داشت.  
او نه در تلفظ واژه‌ها خیلی موفق بود و نه در به‌خاطر سپردن ترتیب حروف الفبا.  
تا این‌که یک روز، **خانم جوادپور** — دبیر زبانش — تصمیم گرفت تمرینی متفاوت برایش بنویسد.

----------

## مأموریت دبیر

خانم جوادپور گفت:

> «امیررضا! هر حرف در زبان انگلیسی یک جایگاه عددی  دارد که امتیاز آن است.  
> مثلاً:
> 
> -   a = 1
>     
> -   b = 2
>     
> -   c = 3  
>     ...  
>     تا z = 26.»
>     

سپس لبخند زد و ادامه داد:

> «اگر حرفی **صدادار** بود، یعنی یکی از حروف  
> **a, e, i, o, u**،  
> امتیازش را باید **به توان دو** برسانی.  
> و اگر حرفی **بزرگ (Capital)** بود، نمره‌اش را **دو برابر** حساب کنید!  
> البته در نظر داشته باشید که در ترتیب عملیات، به توان 2 رسیدن نسبت به ضرب در 2 ارجحیت دارد!
> در آخر، مجموع همه‌ی امتیازها نمره‌ی نهایی آن کلمه می‌شود.»

----------

## برنامه‌نویسی امیررضا

امیررضا که تازه با پایتون آشنا شده بود، با خودش گفت:

> «اگر قرار است نمره‌ی هر کلمه را حساب کنم، چرا دستی حساب کنم؟  
> بگذار یک برنامه برایش بنویسم!»

وظیفه شما این است که به امیررضا در نوشتن این برنامه کمک کنید.

----------

## ورودی

در خط اول ورودی به شما عدد n داده می‌شود که بیانگر تعداد کلمات ورودی است.

در n خط بعدی هر بار به عنوان ورودی یک کلمه به شما داده خواهد شد که باید امتیاز هر کدام را محاسبه کنید.

----------

## خروجی

پس از محاسبه‌ی امتیاز هر کلمه در خط اول خروجی ابتدا کلمه‌ای که بیشترین امتیاز را دارد خروجی داده و در خط بعدی امتیاز آن را برگردانید.

> تضمین می‌شود که تنها یک کلمه از کلمات ورودی دارای بیشینه‌ی امتیاز است.

----------

### ورودی نمونه 1
```
2
CLAIR
OBSCUR
```
----------

### خروجی نمونه 1
```
word = OBSCUR
score = 1416
```
----------

### ورودی نمونه 2
```
3
PyThOn
pNeumonoultraMicroscOpicsIlIcovolcanoconiosiS
HELLO
```
----------

### خروجی نمونه 2
```
word = pNeumonoultraMicroscOpicsIlIcovolcanoconiosiS
score = 4175
```
---------

### Test Cases

test case 1:

```
3
book
cat
dog
```

output 1:

```
word = book
score = 463
```

test case 2:

```
4
BCDF
QRST
JKLM
XYZ
```

output 2:

```
word = XYZ
score = 150
```

test case 3:

```
3
AEIOU
aEiOu
uUuUu
```

output 3:

```
word = uUuUu
score = 3087
```


test case 4:

```
4
AbC
aBc
ABC
abc
```

output 4:

```
word = ABC
score = 12
```

test case 5:

```
2
supercalifragilisticexpialidocious
QuEeN
```

output 5:

```
word = supercalifragilisticexpialidocious
score = 2183
```

test case 6:

```
13
a
U
b
Z
o
l
s
f
g
j
i
q
M
```

output 6:

```
word = U
score = 882
```

test case 7:

```
3
CPP
RuBy
JaVa
```

output 7:

```
word = RuBy
score = 506
```

test case 8:

```
3
rhythm
CRYPT
brrr
```

output 8:

```
word = CRYPT
score = 164
```

test case 9:

```
3
aeiou
AEIOU
aEiOu
```

output 9:

```
word = AEIOU
score = 1546
```

test case 10:

```
3
Alphabet
DiCtIoNaRy
VoWeLs
```

output 10:

```
word = DiCtIoNaRy
score = 592
```

test case 11:

```
3
A
a
B
```

output 11:

```
word = B
score = 4
```

test case 12:

```
3
OoOoO
ooooo
OOOOO
```

output 12:

```
word = OOOOO
score = 2250
```

test case 13:

```
4
antidisestablishmentarianism
counterrevolutionaries
hyperimmunoelectrophoresis
SuPeRcAlIfRaGiLiStIcExPiAlIdOcIoUs
```

output 13:

```
word = SuPeRcAlIfRaGiLiStIcExPiAlIdOcIoUs
score = 3325
```

test case 14:

```
3
ALgoRitHm
MAGIC
uNIvErsE
```

output 14:

```
word = uNIvErsE
score = 790
```

test case 15:

```
2
Ehsan
Moeini
```

output 15:

```
word = Moeini
score = 452
```

