def parse_number(s:str,iterations:int):
    if iterations == 0:
        return s

    new_s = ""
    flag = True

    i = 0
    while flag:
        c = s[i]
        count = 0
        while c == s[i]:
            count += 1
            i += 1
            if i >= len(s):
                flag = False
                break
        new_s += f"{count}{c}"

    return parse_number(new_s, iterations-1)

def extract_number(lst, iterations):
    result = []
    for item in lst:
        if type(item) == str:
            result.append(parse_number(item, iterations))
        else:
            result.append(extract_number(item, iterations))
            
    return result


user_input = input()
l = eval(user_input)
n = int(input())

print(extract_number(l, n))