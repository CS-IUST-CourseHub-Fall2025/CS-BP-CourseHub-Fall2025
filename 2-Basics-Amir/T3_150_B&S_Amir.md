# حق با عبدالرشیده یا عین‌الله؟ 

یه روز عبدالرشید و عین‌الله داشتن شطرنج بازی میکردن که یهویی بحث شد بهشون:
> عین‌الله: «عبدالرشید چه حرکتیه میزنی؟ شاهت تو کیشه!»  
> عبدالرشید: «چی چرت میگی بابا کجا شاهم کیشه؟؟»

حالا این دو بزرگوار نزد شما اومدن که ببینن حق با کیه.

شما باید یه کد بزنید که مشخص کنه که حالا واقعا شاه عبدالرشید تو کیش بود یا نه. (حواستون باشه که عین‌الله مهره های سفیده و عبدالرشید سیاه )

## ورودی
خط اول ورودی مختصات شاه رو نشون میدن که با فاصله از هم جدا شدن.
خط دوم نوع مهره و مختصاتش رو به این شکل نشون داده:

`piece_type: piece_coordinetes`

حواستون باشه مختصات درست وارد شده باشه! (مخصوصا سرباز یا همون پیاده)

نوع مهره ها هم به این شکله:
  - `Q` → وزیر (Queen)
  - `B` → فیل (Bishop)
  - `R` → رخ (Rook)
  - `N` → اسب (Knight)
  - `P` → پیاده (Pawn)

## خروجی
اگر مختصات وارد شده اشتباه بود خروجی باید `Invalid positions` باشه

اگر نوع مهره وارد شده معتبر نبود خرجی باید `Invalid piece` باشه

هیچوقت این دو اشتباه همزمان رخ نمیدن.

اگر حق با عین‌الله بود و شاه کیش شده بود خروجی باید `YOU ARE IN CHECK` باشه و در غیر این صورت `It's Safe`

---

### ورودی نمونه 1
```
8 8
P: 7 7
```
### خروجی نمونه 1
```
YOU ARE IN CHECK
```
---
### ورودی نمونه 2
```
8 9
Q: 1 1
```
### خروجی نمونه 2
```
Invalid positions
```
---
پ.ن: بازم میگم خیلی حواستون به سرباز باشه!

---
### Test Cases:
Input:  
7 8  
P: 8 7  
Output:  
YOU ARE IN CHECK

Input:  
5 5  
P: 5 4  
Output:  
It's Safe  

Input:  
1 1  
R: 5 1  
Output:  
YOU ARE IN CHECK

Input:  
7 5  
R: 6 4  
Output:  
It's Safe  

Input:  
4 8  
B: 7 7  
Output:  
It's Safe  

Input:  
1 8  
B: 5 4  
Output:  
YOU ARE IN CHECK

Input:  
1 1  
Q: 5 1  
Output:  
YOU ARE IN CHECK

Input:  
7 5  
Q: 6 3  
Output:  
It's Safe  

Input:  
4 8  
Q: 7 7  
Output:  
It's Safe  

Input:  
1 8  
Q: 5 4  
Output:  
YOU ARE IN CHECK  

Input:  
2 3  
N: 1 1  
Output:  
YOU ARE IN CHECK  

Input:  
4 4  
N: 3 3  
Output:  
It's Safe  

Input:  
4 8  
q: 7 7  
Output:  
Invalid piece  

Input:  
4 8  
P: 2 8  
Output:  
Invalid positions  

Input:  
4 8  
P: 7 1  
Output:  
Invalid positions  

Input:  
4 9  
Q: 2 8  
Output:  
Invalid positions  

Input:  
4 8  
B: 9 8  
Output:  
Invalid positions  
