n = int(input())

alphabet = "_abcdefghijklmnopqrstuvwxyz"
vowles = "aeiou"

lst = []
lst_score = []

for i in range(n):
    lst.append(input())
    
for word in lst:

    score = 0
    for char in word:
        if (char.isupper()):
            if (char.lower() in vowles):
                score += 2 * (alphabet.find(char.lower()) **2)
            else:
                score += 2 * (alphabet.find(char.lower()))
        else:
            if (char in vowles):
                score += (alphabet.find(char) **2)
            else:
                score += (alphabet.find(char))
    lst_score.append(score)


max_score = max(lst_score)
print(f"word = {lst[lst_score.index(max_score)]}")
print(f"score = {max_score}")