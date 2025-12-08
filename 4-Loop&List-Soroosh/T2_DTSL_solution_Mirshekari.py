nums = eval(input().strip())
p = int(input().strip())
total = sum(nums)
need = total % p
if need == 0:
    print(0)
else:
    prefix = 0
    seen = {0: -1}  
    ans = float('inf')
    for i, x in enumerate(nums):
        prefix = (prefix + x) % p
        target = (prefix - need) % p

        if target in seen:
            ans = min(ans, i - seen[target])
        seen[prefix] = i
    print(ans if ans != float('inf') and ans != len(nums) else -1)
