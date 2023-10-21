import functools


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

# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))


# Define a function to check
# if a number is a multiple of 3
def is_multiple_of_3(num):
    return num % 3 == 0


# Create a list of numbers to filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter and a lambda function to
# filter the list of numbers and only
# keep the ones that are multiples of 3
result = list(filter(lambda x: is_multiple_of_3(x), numbers))

# Print the result
print(result)

# python code to demonstrate working of reduce()


# initializing list
list1 = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, list1))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, list1))
