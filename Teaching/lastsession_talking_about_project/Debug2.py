def zoj(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
user_input = int(input("Yek adad vared konid :"))
zoj_budn = zoj(user_input)

if zoj_budn :
    print("adad even hast")
else:
    print("adad fard hast")