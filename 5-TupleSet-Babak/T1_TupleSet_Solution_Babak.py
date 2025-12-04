def weighted_average(grades):
    n = len(grades)
    total_weight = sum(range(1, n+1))
    weighted_sum = sum(grades[i]*(i+1) for i in range(n))
    return weighted_sum / total_weight

def analyze_students(students):
    result = [(name, weighted_average(grades)) for name, grades in students.items()]
    result.sort(key=lambda x: (-x[1], x[0]))
    return result

n = int(input())
students = {}

for _ in range(n):
    name = input()
    grades = list(map(int, input().split()))
    students[name] = grades

print(analyze_students(students))
