# def find_second_lowest_scorer(records):
#     if len(records) > 5 or len(records) < 2:
#         return
#     records.sort(key=lambda x: x[1])
#     second_lowest = records[1][1]
#     names = [rec[0] for rec in records if rec[1] == second_lowest]
#     names.sort()
#     return "\n".join(names)
#
#
# if __name__ == '__main__':
#     records = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         records.append([name, score])
#
#     print(find_second_lowest_scorer(records))


records = []
for _ in range(int(input())):
    a,b = input().split()
    records.append((a,b))
for rec in records:
    print(rec)
    try:
        a,b = rec
        print(int(a)//int(b))
    except Exception as e:
        print("Error Code:",e)