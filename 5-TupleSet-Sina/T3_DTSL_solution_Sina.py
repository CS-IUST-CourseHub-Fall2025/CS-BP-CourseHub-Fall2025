l1 = list(input().split())
l2 = list(input().split())
l_final = []
for l2_word in l2:
    for l1_word in l1:
        if l1_word in l2_word:
            if l1_word not in l_final:
                l_final.append(l1_word)
print([*l_final])
