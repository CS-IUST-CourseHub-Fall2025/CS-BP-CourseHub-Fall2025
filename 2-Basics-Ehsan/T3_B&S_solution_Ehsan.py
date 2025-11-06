s = input()

last_char = s[-1]
final_temperature = 0

if (last_char in "Cc"):
    temperature = float(s[:-1])
    if ((temperature // 10) % 2 == 0 and int(temperature) != temperature):
        final_temperature = int(temperature) + 1
    else:
        final_temperature = int(temperature)

elif (last_char in "Ff"):
    temperature = float(s[:-1])
    temperature = (temperature - 32) / 1.8
    if ((temperature // 10) % 2 == 0 and int(temperature) != temperature):
        final_temperature = int(temperature) + 1
    else:
        final_temperature = int(temperature)

else:
    print("what a witch!")
    exit()


if (final_temperature < 10):
    print(f"{final_temperature}C too cold!")
elif (final_temperature > 45):
    print(f"{final_temperature}C too hot!")
else:
    print(f"{final_temperature}C just fine!")