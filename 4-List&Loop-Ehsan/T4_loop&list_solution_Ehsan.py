n = int(input())
blocks = []
for i in range(n):
    blocks.append(int(input()))

water_amount = 0

for i in range(len(blocks)):
    block_height = blocks[i]
    while block_height > 0:
        for j in range(i+1,len(blocks)):
            if blocks[j] >= block_height:
                water_amount += (j-i-1)
                break
        block_height -= 1
        
print(water_amount)