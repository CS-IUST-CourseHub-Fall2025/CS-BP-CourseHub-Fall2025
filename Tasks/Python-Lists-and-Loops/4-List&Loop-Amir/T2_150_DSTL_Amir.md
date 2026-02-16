# عین‌الله مُرد!
عین‌الله که تازگیا در رقابت  با عبدالرشید تو شطرنج شکست خورد، تصمیم گرفت با چندتا از دوستاش برن کمپ کنن و خوش بگذرونن تا جنجال آخر بازیشون از یادش بره.  
چند روز که گذشت خودش و دوستاش میفهمن که آذوقه‌ای که آورده بودن کافی نبود و تمام شد!  
اونا بعد از بحث و گفتوگوی فراوان تصمیم گرفتند که در حرکتی شکوهمندانه (؟)، نوبتی خودکشی کنن!
## ورودی
ورودی دو خط و به ترتیب اعداد `n` و `k` هستند به طوری که:  
n: تعداد جمع دوستان عین‌الله  
k: نشان دهنده ترتیب و نوبت خودکشی افراده
$$
n, k \in \mathbb{N}
$$
## خروجی
برنامه شما باید در خروجی ترتیب مردن افراد رو در قالب یک لیست چاپ کنه و سپس  بگه که عین‌الله نفر چندم مرد.


**توجه**: عین‌الله رو همیشه نفر اول در جمع دوستاش در نظر بگیرید.

---
### ورودی نمونه 1:
```
7
3
```
### خروجی نمونه 1:
```
[3, 6, 2, 7, 5, 1, 4]
Ainollah died in: 6
```
#### بررسی جواب:
[1,2,3,4,5,6,7] => initial sequence  
[1,2,4,5,6,7] => 3 is counted out and goes into the result [3]  
[1,2,4,5,7] => 6 is counted out and goes into the result [3,6]  
[1,4,5,7] => 2 is counted out and goes into the result [3,6,2]  
[1,4,5] => 7 is counted out and goes into the result [3,6,2,7]  
[1,4] => 5 is counted out and goes into the result [3,6,2,7,5]  
[4] => 1 is counted out and goes into the result [3,6,2,7,5,1]  
[] => 4 is counted out and goes into the result [3,6,2,7,5,1,4]


مشخصه که عدد 1، نفر 6ام حذف شد!

---
### ورودی نمونه 2:
```
8
2
```
### خروجی نمونه 2:
```
[2, 4, 6, 8, 3, 7, 5, 1]
Ainollah died in: 8
```

---
P.S. Remember that Ainollah never dies!

---
### Test Cases:
Input:  
7  
3  
Output:  
[3, 6, 2, 7, 5, 1, 4]  
Ainollah died in: 6  

Input:  
8  
2  
Output:  
[2, 4, 6, 8, 3, 7, 5, 1]  
Ainollah died in: 8  

Input:  
2  
7  
Output:  
[1, 2]  
Ainollah died in: 1  

Input:  
3  
100  
Output:  
[1, 3, 2]  
Ainollah died in: 1  

Input:  
1  
1  
Output:  
[1]  
Ainollah died in: 1  

Input:  
10  
1  
Output:  
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
Ainollah died in: 1  

Input:  
10  
9  
Output:  
[9, 8, 10, 2, 5, 3, 4, 1, 6, 7]  
Ainollah died in: 8  

Input:  
5  
6  
Output:  
[1, 3, 2, 5, 4]  
Ainollah died in: 1  

Input:  
9  
4  
Output:  
[4, 8, 3, 9, 6, 5, 7, 2, 1]  
Ainollah died in: 9  