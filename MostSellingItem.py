import collections

def find_most_seeling_item(items):
    # most_common = collections.Counter(items)
    # print(most_common.most_common(1))



    count_dict = {}

    for item in items:
        if item in count_dict:
            count_dict[item.lower()] += 1
        else:
            count_dict[item.lower()] = 1
    # print(count_dict)


    # initial_count = 0
    # counter = 0
    # for key,value in count_dict.items():
    #     if initial_count > value:
    #         print("step",counter)
    #         initial_count = value
    #         counter += 1
    # max_count_key = (sorted(count_dict,key=count_dict.get,reverse=True))[0]
    max_count = max(count_dict.values())
    # max_count = count_dict.get(max_count_key)



    most_selling_item = [key for key,value in count_dict.items() if value == max_count]
    most_selling_item.sort(reverse=False)
    return most_selling_item[0]



"""
Apple , banana , onions , banana , cucumber , biscuits , banana , banana,
Apple , banana , juice , orange , Apple , banana , Apple , biscuits , cucumber , cucumber , Apple , cucumber,
banana , juice , orange , Apple , biscuits , biscuits , juice , banana

"""
items = ["Apple","banana","banana","cucumber","biscuits","apple",
         "biscuits","biscuits","apple","biscuits","banana",
         "banana","bana","bana","bana","bana"]

print(find_most_seeling_item(items))


