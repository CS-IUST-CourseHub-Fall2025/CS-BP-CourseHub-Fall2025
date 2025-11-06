word = input()

alphabet = "_abcdefghijklmnopqrstuvwxyz"
vowles = "aeiou"
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

print(score)
