s = input()
lenght = len(s)

if s.count('0') == lenght:
    print('0')
else:
    result = ''
    for index, char in enumerate(s):
        if char == '0':
            continue
        if result:
            result += ' + '
        result += char + '0' * (lenght - index - 1)
    print(result)

