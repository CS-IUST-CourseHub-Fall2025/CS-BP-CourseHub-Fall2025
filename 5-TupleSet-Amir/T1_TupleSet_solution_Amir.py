dic = eval(input())

main_dict = {}
lst = sorted(list(set(dic)), key = int)
for key in lst:
    main_dict.update({key: dic[key]})

temp_list = []
output_dict = {}

for key in list(main_dict.keys())[::-1]:
    value_list = []
    for val in main_dict[key]:
        if not val in temp_list:
            value_list.append(val)
            temp_list.append(val)
    output_dict[key] = value_list

print(dict(list(output_dict.items())[::-1]))