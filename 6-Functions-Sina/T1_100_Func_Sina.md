### 🏷️ تگ‌های HTML

زبان **HTML** برای ساختاردهی صفحات وب استفاده می‌شود. در این زبان، هر بخش از محتوا معمولاً داخل یک **تگ (Tag)** قرار می‌گیرد. یک تگ به‌صورت زیر نوشته می‌شود:

```
<tag>Content</tag>

```

برای مثال:

```
<p>Hello</p>

```

که در آن `p` یک تگ پاراگراف است. با معانی و عملکرد تگ ها کاری نداریم

در این مسئله، شما باید با استفاده از تعدادی تگ، یک متن را مرحله‌ به‌ مرحله تغییر دهید.

---

### 🔹نحوه اضافه کردن تگ ها

- به شما یک **متن اولیه** داده می‌شود.

- سپس یک لیست از **دستورات (نام تگ‌ها)** به ترتیب داده می‌شود.

    هر تگ ممکن است یکی از عناصر ["a", "p", "article", "figure", "div", "span"] باشد

- برای هر دستور:

1.  اگر دستور یک تگ جزو لیست بالا باشد:

    ```
    <tag>Starting Phrase</tag>

    ```

2.  اگر دستور تگ comment باشد:

    ```
    /*Starting Phrase*/
    ```

3.  اگر دستور هر چیز دیگری باشد، جمله بدست امده فعلی را دو بار کنار هم بذارید برای مثال اگر جمله Phrase باشد

    ```
    PhrasePhrase
    ```

---

### 🧩 ورودی

- خط اول: یک رشته به عنوان متن اولیه

- خط دوم: نام تعدادی (حداکثر 16) تگ با حروف کوچک انگلیسی که با فاصله از هم جدا شده‌اند.

---

### 🧾 خروجی

یک خط شامل نتیجه‌ی نهایی پس از اعمال تمام دستورات به ترتیب.

---

### 🔢 نمونه ورودی 1

Hello
div p comment span

### 🖨️ نمونه خروجی 1

```
<span>/*<p><div>Hello</div></p>*/</span>
```

---

### 🔢 نمونه ورودی 2

FuncsAreGreat
something div unvalid p

### 🖨️ نمونه خروجی 2

```
<p><div>FuncsAreGreatFuncsAreGreat</div><div>FuncsAreGreatFuncsAreGreat</div></p>
```

---

```
Input:
Hello
a
Output:
<a>Hello</a>

Input:
World
p
Output:
<p>World</p>

Input:
Test
comment
Output:
/*Test*/

Input:
Word
unknown
Output:
WordWord

Input:
Phrase
a p
Output:
<p><a>Phrase</a></p>

Input:
Hi
div span
Output:
<span><div>Hi</div></span>

Input:
Foo
article figure
Output:
<figure><article>Foo</article></figure>

Input:
Bar
span div a
Output:
<a><div><span>Bar</span></div></a>

Input:
Baz
comment a
Output:
<a>/*Baz*/</a>

Input:
Quux
p unknown
Output:
<p>Quux</p><p>Quux</p>

Input:
Test
unknown unknown
Output:
TestTestTestTest

Input:
Hello World
a comment div
Output:
<div>/*<a>Hello World</a>*/</div>

Input:
Simple
span
Output:
<span>Simple</span>

Input:
Complex
figure p article span
Output:
<span><article><p><figure>Complex</figure></p></article></span>

Input:
End
comment unknown a p
Output:
<p><a>/*End*//*End*/</a></p>
```
