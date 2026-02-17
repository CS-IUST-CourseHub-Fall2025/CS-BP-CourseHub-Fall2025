#did you know that dp problems are really nice for our bp students? bet you didn't know
def max_gold(caves, n, memo=None):
    if memo is None:
        memo = {}
    
    if n < 0:
        return 0
    
    if n in memo:
        return memo[n]
    
    take_current = caves[n] + max_gold(caves, n - 2, memo)
    
    skip_current = max_gold(caves, n - 1, memo)
    
    memo[n] = max(take_current, skip_current)
    return memo[n]


n = int(input())
caves = list(map(int, input().split()))

result = max_gold(caves, n - 1)
print(result)
