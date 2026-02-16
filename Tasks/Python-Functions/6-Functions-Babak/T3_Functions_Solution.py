def count_subsets(n, s, current, memo=None):
    if memo is None:
        memo = {}

    if s == 0:
        return 1
    
    if s < 0 or current > n:
        return 0
    
    if (current, s) in memo:
        return memo[(current, s)]

    include = count_subsets(n, s - current, current + 1, memo)

    exclude = count_subsets(n, s, current + 1, memo)
    
    memo[(current, s)] = include + exclude
    return memo[(current, s)]


n, s = map(int, input().split())

result = count_subsets(n, s, 1)
print(result)
