data = input().split()
res = ''
n = len(data)  # n >= 3

# if n >= 1:
#     if len(data[0]) >= 5:
#         res += f"{data[0][::-1]} "
#     else:
#         res += f"{data[0]} "
    
#     if n >= 2:
#         if len(data[1]) >= 5:
#             res += f"{data[1][::-1]} "
#         else:
#             res += f"{data[1]} "

#         if n == 3:
#             if len(data[2]) >= 5:
#                 res += f"{data[2][::-1]} "
#             else:
#                 res += f"{data[2]} "

# Cleaner way:
if n >= 1:
    res += (data[0][::-1] if len(data[0]) >= 5 else data[0]) + ' '

if n >= 2:
    res += (data[1][::-1] if len(data[1]) >= 5 else data[1]) + ' '

if n >= 3:
    res += (data[2][::-1] if len(data[2]) >= 5 else data[2]) + ' '


print(res.strip())