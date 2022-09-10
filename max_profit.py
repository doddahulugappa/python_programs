profit = -1
list1 = input().split()
list1 = list(map(int,list1))

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if i > j:
            temp_profit = i - j
            profit = max(temp_profit,profit)

print(profit)