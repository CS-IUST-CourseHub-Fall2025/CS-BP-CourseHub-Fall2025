def effect_tag(tag, input):
    if tag in ["a", "p", "article", "figure", "div", "span"]:
        return f"<{tag}>{input}</{tag}>"
    elif tag == "comment":
        return f"/*{input}*/"
    else:
        return f"{input}" * 2


starting_phrase = input()
ans = ""
commands = input().split()
for _ in commands:
    ans = effect_tag(_, ans if (ans != "") else starting_phrase)
print(ans)
