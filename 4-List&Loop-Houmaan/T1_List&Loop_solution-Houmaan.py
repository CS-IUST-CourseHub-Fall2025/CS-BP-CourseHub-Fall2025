nums = input()
p =int(input())

total_sum = sum(nums)
target = total_sum % p

if target == 0:
    result = 0
else:
    mod_map = {0: -1}
    current_sum = 0
    min_len = len(nums)
    
    for i, num in enumerate(nums):
        current_sum = (current_sum + num) % p
        needed = (current_sum - target + p) % p
        
        if needed in mod_map:
            current_len = i - mod_map[needed]
            if current_len < min_len:
                min_len = current_len
        
        mod_map[current_sum] = i
        
    if min_len == len(nums):
        result = -1
    else:
        result = min_len

print(result)
