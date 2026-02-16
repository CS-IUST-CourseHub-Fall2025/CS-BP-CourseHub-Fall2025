#first solution (greater time complexity)
def CalculateTrappedWater(n, blocks):
    trapped_water = 0

    for i in range(len(blocks)):
        block_height = blocks[i]
        while block_height > 0:
            for j in range(i+1,len(blocks)):
                if blocks[j] >= block_height:
                    trapped_water += (j-i-1)
                    break
            block_height -= 1
    
    return trapped_water



# second solution
def Divide(lst):
    length = len(lst)
    if (length < 3):
        return 0
   
    lst_copy = lst.copy()
    left_max = max(lst_copy)
    i = lst_copy.index(left_max)
    lst_copy.pop(i)
    second_max = max(lst_copy)
    for k in range(length-1, -1, -1):
        if (lst[k] == second_max) and (k != i):
            j = k
            break
    i, j = min(i,j), max(i,j)
    
    if (i == 0) and (j == length - 1):
        return WaterAmount(lst, i, j)
    else:
        return Divide(lst[:i+1]) + Divide(lst[i:j+1]) + Divide(lst[j:])


def WaterAmount(lst, i, j):
    h = min(lst[i], lst[j])
    water = 0
    for k in range(i+1, j):
        water += max(0, h - lst[k])
    return water
    

# third solution with lowest time complexity (GPT solution)
def TrappedWater(n, blocks):
    if n < 3:
        print(0)
        exit()

    left_max = [0] * n
    left_max[0] = blocks[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], blocks[i])

    right_max = [0] * n
    right_max[-1] = blocks[-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], blocks[i])

    water_amount = 0
    for i in range(n):
        water_amount += max(0, min(left_max[i], right_max[i]) - blocks[i])
    
    return water_amount




if (__name__ == "__main__"):
    
    n = int(input())
    blocks = []
    for i in range(n):
        blocks.append(int(input()))

    water_amount = Divide(blocks)
    print(water_amount)

