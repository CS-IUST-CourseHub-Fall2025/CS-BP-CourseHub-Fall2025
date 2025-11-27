### 🕵️ **کلمات مخفی**

محدودیت زمان: **۱ ثانیه**
محدودیت حافظه: **۲۵۶ مگابایت**

ما دو لیست از کلمات داریم. هر دو شامل کلمات کلمات انگلیسی با حروف **کوچک** هستند
شما باید بررسی کنید کدام‌یک از کلمات لیست اول، درون کلمات لیست وجود دارند (یعنی زیررشته‌ی آن‌ها هستند).

قواعد بررسی:

- دو خط ورودی به شما داده می‌شود که هر کدام شامل تعدادی رشته (کلمه) است که با فاصله از هم جدا شده‌اند.

- باید کلماتی از **لیست اول** را پیدا کنید که زیررشته‌ی حداقل یکی از کلمات **لیست دوم** باشند.
  تمام کلمات لیست اول حداقل در یکی از کلمات لیست دوم وجود دارند
  و تضمین میشود هر کلمه از لیست دوم، دقیقا حاوی صفر یا یک کلمه از لیست اول است و نه بیشتر

- **ترتیب خروجی مهم است:** کلمات پیدا شده باید به ترتیبِ ظاهر شدنِ کلماتِ در **لیست دوم** مرتب شوند.

- در لیست نهایی نباید کلمه‌ی تکراری وجود داشته باشد.

- خروجی باید دقیقاً با فرمت یک لیست پایتونی ['string1', 'string2'] چاپ شود.

---

### 🧩 **ورودی**

- خط اول و دوم: لیستی از کلمات با حروف **کوچک** که با فاصله از هم جدا شده‌اند. (هیچکدام خالی نیستند)

---

### 🧾 **خروجی**

در یک خط، لیست کلمات پیدا شده را با فرمت استاندارد لیست چاپ کنید.

---

### 🔢 **ورودی نمونه ۱**

arp live strong
lively alive harp sharp armstrong

### 🖨️ **خروجی نمونه ۱**

['live', 'arp', 'strong']

---

### 🔢 **ورودی نمونه ۲**

tarp mice bull
lively alive harp sharp armstrong

### 🖨️ **خروجی نمونه ۲**

[]

---

### 🔢 **ورودی نمونه ۳**

grape peach pear apple
pineapple fruit spear grapplers sweet peachy grapefruit

### 🖨️ **خروجی نمونه ۳**

['apple', 'pear', 'peach', 'grape']

```
Input:
strong live arp
lively filler alive harp sharp armstrong extra
Output:
['live', 'arp', 'strong']

Input:
bull mice tarp
lively alive harp sharp armstrong
Output:
[]

Input:
man hero
superhero spider bat human ironman
Output:
['hero', 'man']

Input:
fish bird dog cat
scatter dogma birdcage selfish
Output:
['cat', 'dog', 'bird', 'fish']

Input:
four two one
telephone network flour stone
Output:
['one', 'two']

Input:
green blue red
bored sky blueberry grass greenhouse
Output:
['red', 'blue', 'green']

Input:
sky star moon sun
sunny day honeymoon night start skyscraper
Output:
['sun', 'moon', 'star', 'sky']

Input:
grape peach pear apple
pineapple fruit spear sweet peachy sour grapefruit
Output:
['apple', 'pear', 'peach', 'grape']

Input:
truck van bus car
scarab business advantage struck sedan
Output:
['car', 'bus', 'van', 'truck']

Input:
bio chem phys math
polymath history physical geography alchemy biology
Output:
['math', 'phys', 'chem', 'bio']

Input:
soft data web net
network hardware website server database microsoft
Output:
['net', 'web', 'data', 'soft']

Input:
swim jump run play
player walker runner sprinter jumper swimmer
Output:
['play', 'run', 'jump', 'swim']

Input:
earth wind fire ice
police water bonfire air window rock hearth
Output:
['ice', 'fire', 'wind', 'earth']

Input:
iron bronze silver gold
marigold platinum quicksilver copper bronzed steel irony
Output:
['gold', 'silver', 'bronze', 'iron']

Input:
west east south north
northern up southern down eastern right western left
Output:
['north', 'south', 'east', 'west']

```
