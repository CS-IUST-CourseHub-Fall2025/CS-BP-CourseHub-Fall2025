initialMoney = float(input())
profitPercent = float(input())
amountOfYears = int(input())
finalMoney = int(initialMoney * (1 + profitPercent / 100) ** amountOfYears)

print(finalMoney, "$")
