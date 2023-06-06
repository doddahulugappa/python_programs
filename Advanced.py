
def square(x):
    return x * x


l1 = [1, 2, 3, 4, 5]

squared_list = list(map(square, l1))
squared_list = list(map(lambda x: x * x, l1))
print(squared_list)


l1 = ['1', '2', '3', 8, 9]
l2 = [3, 6, 8]
l3 = []
for i, j in enumerate(l1):
    if i % 2 == 1:
        l3.append(j)
for i, j in enumerate(l2):
    if i % 2 == 0:
        l3.append(j)
print(l3)