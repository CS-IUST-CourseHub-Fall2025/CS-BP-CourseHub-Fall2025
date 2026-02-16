number1 = int(input())
number2 = int(input())

firstdigit1 = number1 % 10  
lastdigit1 = number1 // 100 
middigit1 = (number1 // 10) % 10  

firstdigit2 = number2 % 10  
lastdigit2 = number2 // 100  
middigit2 = (number2 // 10) % 10  

if firstdigit1 > firstdigit2:
    print(f"{number2} < {number1}")
elif firstdigit1 < firstdigit2:
    print(f"{number1} < {number2}")
else:  
    if middigit1 > middigit2:
        print(f"{number2} < {number1}")
    elif middigit1 < middigit2:
        print(f"{number1} < {number2}")
    else:  
        if lastdigit1 > lastdigit2:
            print(f"{number2} < {number1}")
        elif lastdigit1 < lastdigit2:
            print(f"{number1} < {number2}")
        else:  
            print(f"{number2} = {number1}")