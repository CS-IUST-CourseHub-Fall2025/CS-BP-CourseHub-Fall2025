password = input("لطفاً رمز عبور خود را وارد کنید: ")

has_min_length = len(password) >= 8

has_upper = False
if len(password) > 0:
    if password[0].isupper():
        has_upper = True
    elif len(password) > 1 and password[1].isupper():
        has_upper = True
    elif len(password) > 2 and password[2].isupper():
        has_upper = True
    elif len(password) > 3 and password[3].isupper():
        has_upper = True
    elif len(password) > 4 and password[4].isupper():
        has_upper = True
    elif len(password) > 5 and password[5].isupper():
        has_upper = True
    elif len(password) > 6 and password[6].isupper():
        has_upper = True
    elif len(password) > 7 and password[7].isupper():
        has_upper = True

has_digit = False
if len(password) > 0:
    if password[0].isdigit():
        has_digit = True
    elif len(password) > 1 and password[1].isdigit():
        has_digit = True
    elif len(password) > 2 and password[2].isdigit():
        has_digit = True
    elif len(password) > 3 and password[3].isdigit():
        has_digit = True
    elif len(password) > 4 and password[4].isdigit():
        has_digit = True
    elif len(password) > 5 and password[5].isdigit():
        has_digit = True
    elif len(password) > 6 and password[6].isdigit():
        has_digit = True
    elif len(password) > 7 and password[7].isdigit():
        has_digit = True

has_special = False
if len(password) > 0:
    if password[0] == '@' or password[0] == '#' or password[0] == '$':
        has_special = True
    elif len(password) > 1 and (password[1] == '@' or password[1] == '#' or password[1] == '$'):
        has_special = True
    elif len(password) > 2 and (password[2] == '@' or password[2] == '#' or password[2] == '$'):
        has_special = True
    elif len(password) > 3 and (password[3] == '@' or password[3] == '#' or password[3] == '$'):
        has_special = True
    elif len(password) > 4 and (password[4] == '@' or password[4] == '#' or password[4] == '$'):
        has_special = True
    elif len(password) > 5 and (password[5] == '@' or password[5] == '#' or password[5] == '$'):
        has_special = True
    elif len(password) > 6 and (password[6] == '@' or password[6] == '#' or password[6] == '$'):
        has_special = True
    elif len(password) > 7 and (password[7] == '@' or password[7] == '#' or password[7] == '$'):
        has_special = True


print(f"طول مناسب: {'True' if has_min_length else 'False'}")
print(f"حرف بزرگ: {'True' if has_upper else 'False'}")
print(f"عدد: {'True' if has_digit else 'False'}")
print(f"کاراکتر ویژه: {'True' if has_special else 'False'}")
