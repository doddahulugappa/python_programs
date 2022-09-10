import collections

def round_up(item):
    return round(item,2)

list1 = [60.42365,60.429887,60.426568,60.44987,60.446328,60.44782,60.46321]

round_up_list = list(map(round_up,list1))
print(collections.Counter(round_up_list))
