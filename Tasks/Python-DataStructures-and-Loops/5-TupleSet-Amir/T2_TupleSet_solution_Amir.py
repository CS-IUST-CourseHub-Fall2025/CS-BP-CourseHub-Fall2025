inpt = eval(input())
pre_set = set()
print(dict(list({x: [pre_set.add(y) or y for y in inpt[x] if y not in pre_set] for x in sorted(inpt, key=int, reverse=True)}.items())[::-1]))