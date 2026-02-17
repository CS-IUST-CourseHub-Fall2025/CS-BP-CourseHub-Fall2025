### 🪐 **سیاره‌های قاطی‌شده**

محدودیت زمان: **۲ ثانیه**
محدودیت حافظه: **۲۵۶ مگابایت**

برای حفظ ترتیب سیاره‌ها معمولاً یک جمله‌ی یادآور می‌سازند؛ طوری که حرف اول هر کلمه، با حرف اول سیاره‌ی مربوطه یکی ست
حالا سیاره‌ها به‌هم ریخته‌اند و یک جمله‌ی یادآور به شما داده میشود. شما باید بررسی کنید این جمله با منظومه‌ی جدید جور درمیاد یا نه.

قواعد بررسی:

- یک لیست با طول حداقل 1 از اجرام منظومه شمسی به شما داده می‌شود.
  Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Asteroid

- شهاب سنگ ها (Asteroid) در ترتیب سیاره ها قرار نمیگیرند

- جمله‌ی یادآور چند کلمه دارد؛
  باید تعداد کلماتش دقیقاً برابر تعداد سیاره‌های باقی‌مانده باشد و
  **حرف اول هر کلمه** با **حرف اول سیاره‌ی متناظر** یکی باشد. (به بزرگی و کوچکی حساس است)

- هیچ سیاره‌ای دوبار نمی‌آید (جز Asteroid که ممکن است چند بار تکرار شود).

اگر جمله دقیقاً مطابق باشد، `True` وگرنه `False` چاپ کنید.

---

### 🧩 **ورودی**

- خط اول: `n` کلمه با فاصله، یک لیست از کلمات داده شده بالا
- خط دوم: جمله یادآور، یک لیست به طول دلخواه (بزرگتر از 0) از کلمات انگلیسی

---

### 🧾 **خروجی**

در یک خط چاپ کنید:

- `True` اگر جمله درست باشد

- `False` در غیر این صورت

---

### 🔢 **ورودی نمونه ۱**

`Asteroid Mercury Asteroid Venus Asteroid Earth Asteroid Mars Asteroid`

`A M A V A E A M A`

### 🖨️ **خروجی نمونه ۱**

`False`

---

### 🔢 **ورودی نمونه ۲**

`Jupiter Asteroid Earth Asteroid Saturn Mercury`

`Joyful Eagles Soar Magnificently`

### 🖨️ **خروجی نمونه ۲**

`True`

---

### 🔢 **ورودی نمونه ۳**

`Mercury Jupiter`

`mAintenance JustIncomprehensibilities`

### 🖨️ **خروجی نمونه ۳**

`False`

```
Input: Mercury Venus Earth Mars
Many Very Exciting Moments
Output:
True

Input: Earth Jupiter Asteroid Asteroid Mercury Asteroid Saturn
Even Jaguars Make Spaghetti
Output:
True

Input: Jupiter Saturn Uranus Neptune
Just Some Unique Names
Output:
True

Input: Asteroid Mercury Asteroid Earth Jupiter Asteroid Uranus
Mighty Eagles Jump Upward
Output:
True

Input: Venus Asteroid Neptune Saturn
Very Nice
Output:
False

Input: Mars Uranus
Many Unusual Random Things
Output:
False

Input: Mercury Jupiter
maintenance Jumping
Output:
False

Input: Neptune
Neptune
Output:
True

Input: Asteroid Asteroid Asteroid Uranus
Ultimate
Output:
True

Input: Earth Mars
Elegant Violins
Output:
False

Input: Mercury Asteroid Venus Earth Asteroid Mars Jupiter Saturn Asteroid Uranus Neptune
My Very Educated Mother Just Served Us Nachos
Output:
True

Input: Asteroid Saturn Asteroid Asteroid Mars Asteroid Venus Asteroid
Super Massive Volcano
Output:
True

Input: Jupiter Uranus Neptune
JUMPING Unicorns Never
Output:
True

Input: Jupiter Asteroid Earth Asteroid Saturn Mercury Uranus Neptune
Joyful Eagles Soar Magnificently Under Nighttime
Output:
True

Input: Venus Earth Jupiter
Very Magnificent Journey
Output:
False
```
