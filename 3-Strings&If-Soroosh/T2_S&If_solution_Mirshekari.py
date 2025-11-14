fhour, fminute = map(int, input().split())

ahour = 12 - fhour
aminute = 60 - fminute

if ahour == 12:
    ahour = 0
if aminute == 60:
    aminute = 0

if ahour < 10 and aminute < 10:
    print(f"0{ahour}:0{aminute}")
elif ahour < 10 and aminute >= 10:
    print(f"0{ahour}:{aminute}")
elif ahour >= 10 and aminute < 10:
    print(f"{ahour}:0{aminute}")
else:
    print(f"{ahour}:{aminute}")