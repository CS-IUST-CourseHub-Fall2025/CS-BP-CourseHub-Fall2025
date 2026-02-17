### 🔊 **اکوی معکوس**

محدودیت زمان: **۲ ثانیه**
محدودیت حافظه: **۲۵۶ مگابایت**

جواد می‌خواهد کلمه‌ای را که سخنران گفته یادداشت کند، اما این‌بار بلندگوها یک اکوی عجیب دارند:
کلمه را **از آخر به اول** پخش می‌کنند و سپس اکوی صدا به‌صورت مرحله‌ای از **انتهای کلمه** تغییر می‌کند.
شما فعلا تصمیم دارید رفتار عجیب کلمات رو به خوبی متوجه بشید
قانون اکو این‌گونه است:

فرض کنید سخنران یک رشته به طول n گفته است.

1.  در بار اول، بلندگو **برعکسِ کلمه** را پخش می‌کند.

2.  در هر بار بعدی (تا مجموعاً n بار):
    - یک حرف جدید از **سمت راست** حذف می‌شود،

    - و همه‌ی حروف حذف‌شده با **حرف جدیدِ آخرِ باقی‌مانده** جایگزین می‌شوند.

برای مثال اگر سخنران بگوید `golabi`، بلندگو این‌طور پخش می‌کند:

ibalog
ibaloo
iballl
ibaaaa
ibbbbb
iiiiii

---

### 🧩 **ورودی**

در تنها خط ورودی یک رشته شامل حروف انگلیسی کوچک و بزرگ می‌آید که کلمه‌ی گفته‌شده توسط سخنران است.
تضمین میشود طول رشته بین 3 تا 25 است

---

### 🧾 **خروجی**

خروجی شامل `n` خط است.
در خط `i`‌ام (از ۱ تا `n`) باید کلمه‌ی پخش‌شده‌ی همان مرحله را چاپ کنید.

---

### 🔢 **ورودی نمونه ۱**

Angoor

### 🖨️ **خروجی نمونه ۱**

roognA
roognn
rooggg
rooooo
rooooo
rrrrrr

---

### 🔢 **ورودی نمونه ۲**

desreveRmI

### 🖨️ **خروجی نمونه ۲**

ImReversed
ImReversee
ImReversss
ImReverrrr
ImReveeeee
ImRevvvvvv
ImReeeeeee
ImRRRRRRRR
Immmmmmmmm
IIIIIIIIII

```
Input:
abc
Output:
cba
cba
cbb
ccc

Input:
cat
Output:
tac
tac
taa
ttt

Input:
xyz
Output:
zyx
zyx
zyy
zzz

Input:
code
Output:
edoc
edoc
edoo
eddd
eeee

Input:
loop
Output:
pool
pool
pooo
pooo
pppp

Input:
data
Output:
atad
atad
ataa
attt
aaaa

Input:
hello
Output:
olleh
olleh
ollee
ollll
ollll
ooooo

Input:
world
Output:
dlrow
dlrow
dlroo
dlrrr
dllll
ddddd

Input:
python
Output:
nohtyp
nohtyp
nohtyy
nohttt
nohhhh
nooooo
nnnnnn

Input:
string
Output:
gnirts
gnirts
gnirtt
gnirrr
gniiii
gnnnnn
gggggg

Input:
testing
Output:
gnitset
gnitset
gnitsee
gnitsss
gnitttt
gniiiii
gnnnnnn
ggggggg

Input:
abcdefgh
Output:
hgfedcba
hgfedcba
hgfedcbb
hgfedccc
hgfedddd
hgfeeeee
hgffffff
hggggggg
hhhhhhhh

Input:
algorithm
Output:
mhtirogla
mhtirogla
mhtirogll
mhtiroggg
mhtiroooo
mhtirrrrr
mhtiiiiii
mhttttttt
mhhhhhhhh
mmmmmmmmm

Input:
programming
Output:
gnimmargorp
gnimmargorp
gnimmargorr
gnimmargooo
gnimmargggg
gnimmarrrrr
gnimmaaaaaa
gnimmmmmmmm
gnimmmmmmmm
gniiiiiiiii
gnnnnnnnnnn
ggggggggggg

Input:
computerscience
Output:
ecneicsretupmoc
ecneicsretupmoc
ecneicsretupmoo
ecneicsretupmmm
ecneicsretupppp
ecneicsretuuuuu
ecneicsretttttt
ecneicsreeeeeee
ecneicsrrrrrrrr
ecneicsssssssss
ecneicccccccccc
ecneiiiiiiiiiii
ecneeeeeeeeeeee
ecnnnnnnnnnnnnn
ecccccccccccccc
eeeeeeeeeeeeeee

```
