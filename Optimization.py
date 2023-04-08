import collections
box = [1,3,5,2,4]
quantity = [6,8,10,7,9]

most_com = collections.Counter(quantity)


truck_size = 7



dict_obj = dict(zip(box, quantity))

box_count_list = {}
for i in range(len(box)):

    total = 0
    box_quantity = 0
    while box_quantity <= truck_size:
        for b, q in zip(box[i:], quantity[i:]):
            if b < truck_size:
                total += b * q
                box_quantity += b
    box_count_list[total] = box_quantity

# print(total)
print(box_count_list)