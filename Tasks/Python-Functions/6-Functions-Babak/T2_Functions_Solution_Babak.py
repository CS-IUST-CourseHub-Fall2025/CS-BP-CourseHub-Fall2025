def count_paths(grid, n, m, row, col, memo=None):
    """
    تابع بازگشتی برای شمارش تعداد مسیرها
    grid: شبکه جادویی
    n, m: ابعاد شبکه
    row, col: موقعیت فعلی
    memo: دیکشنری برای ذخیره‌سازی نتایج
    """
    if memo is None:
        memo = {}
    
    if row >= n or col >= m or grid[row][col] == '#':
        return 0
    
    if row == n - 1 and col == m - 1:
        return 1
    
    if (row, col) in memo:
        return memo[(row, col)]
    
    right = count_paths(grid, n, m, row, col + 1, memo)
    
    down = count_paths(grid, n, m, row + 1, col, memo)
    
    memo[(row, col)] = right + down
    return memo[(row, col)]


n, m = map(int, input().split())
grid = []
for i in range(n):
    grid.append(input().strip())

result = count_paths(grid, n, m, 0, 0)
print(result)
