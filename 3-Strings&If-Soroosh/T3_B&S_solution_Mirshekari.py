import math

def main():
    k, a, b = map(int, input().split())
    
    if a > b:
        a, b = b, a
        
    distance = abs(a - b)
    
    ak = a / k
    bk = b / k
    
    station_a = math.floor(ak) + 1 if (ak - math.floor(ak)) >= 0.5 else math.floor(ak)
    station_a *= k
    
    station_b = math.floor(bk) if (bk - math.floor(bk)) <= 0.5 else math.floor(bk) + 1
    station_b *= k
    
    total = abs(a - station_a) + (abs(station_a - station_b) // k) + abs(station_b - b)
    
    print(min(total, distance))

if __name__ == "__main__":
    main()