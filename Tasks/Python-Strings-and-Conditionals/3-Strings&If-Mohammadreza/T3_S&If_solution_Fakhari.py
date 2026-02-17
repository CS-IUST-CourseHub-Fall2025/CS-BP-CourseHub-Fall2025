def main():
    xA, yA = map(float, input().split())
    xB, yB = map(float, input().split())
    xC, yC = map(float, input().split())
    xD, yD = map(float, input().split())
    
    sabc = 0.5 * (xA * (yB - yC) + xB * (yC - yA) + xC * (yA - yB))
    sacd = 0.5 * (xA * (yC - yD) + xC * (yD - yA) + xD * (yA - yC))
    sabd = 0.5 * (xA * (yB - yD) + xB * (yD - yA) + xD * (yA - yB))
    sbcd = 0.5 * (xB * (yC - yD) + xC * (yD - yB) + xD * (yB - yC))
    
    if sabc < 0.0:
        sabc = -0.5 * (xA * (yB - yC) + xB * (yC - yA) + xC * (yA - yB))
    if sacd < 0.0:
        sacd = -0.5 * (xA * (yC - yD) + xC * (yD - yA) + xD * (yA - yC))
    if sabd < 0.0:
        sabd = -0.5 * (xA * (yB - yD) + xB * (yD - yA) + xD * (yA - yB))
    if sbcd < 0.0:
        sbcd = -0.5 * (xB * (yC - yD) + xC * (yD - yB) + xD * (yB - yC))
    
    if ((sacd * sabd * sbcd != 0.0)) and (sabc == (sacd + sabd + sbcd)):
        print("in")
    elif sabc != (sacd + sabd + sbcd):
        print("out")
    elif ((sacd + sabd) == sabc) or (sabc == (sacd + sbcd)) or (sabc == (sabd + sbcd)):
        print("on")

if __name__ == "__main__":
    main()