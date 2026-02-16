def fw(s, n, C, D, A):
    result = 0
    if D >= C:
        result = s - ((D - C) * n)
        if result >= 0:
            return result
        else:
            return -1
    else:
        result = s - ((A - C + D) * n)
        if result >= 0:
            return result
        else:
            return -1

def bw(s, m, C, D, A):
    result = 0
    if D <= C:
        result = s - ((C - D) * m)
        if result >= 0:
            return result
        else:
            return -1
    else:
        result = s - ((A + C - D) * m)
        if result >= 0:
            return result
        else:
            return -1

def main():
    s, n, m, f, l, t = map(int, input().split())
    
    fw_result = fw(s, n, f, l, t)
    bw_result = bw(s, m, f, l, t)
    
    if fw_result != -1:
        print("J :", fw_result)
    if bw_result != -1:
        print("A :", bw_result)
    if fw_result == -1 and bw_result == -1:
        print("-1")

if __name__ == "__main__":
    main()