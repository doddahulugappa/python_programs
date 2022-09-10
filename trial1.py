print("="*50,"join 2 list odd & even")
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

odd_l = [j for i,j in enumerate(l1) if i%2==1]
even_l = [j for i,j in enumerate(l2) if i%2==0]
l3 = odd_l+even_l
print(l1,"l1")
print(l2,"l2")
print(l3,"l3")

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()
print("="*100)
odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements = list2[0::2]
print("Element at even-index positions from list two")
print(even_elements)

print("Printing Final third list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)

######################################################################################
sample_list = [34, 54, 67, 89, 11, 43, 94]

print("Original list ", sample_list)
element = sample_list.pop(4)
print("List After removing element at index 4 ", sample_list)

sample_list.insert(2, element)
print("List after Adding element at index 2 ", sample_list)

sample_list.append(element)
print("List after Adding element at last ", sample_list)
#######################################################################################
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89,43,54,76]
dividing_number = 3
len_list = len(sample_list)
start = 0
print("Sample Given List",sample_list)
while (len_list > 0):
    upto = len_list // dividing_number
    l1 = sample_list[start:start+upto]
    print("Orginal Chunk:",4-dividing_number)
    print(l1)
    print("Reversed Chunk:",4-dividing_number)
    print(l1[::-1])
    len_list = len_list - upto
    start +=upto
    dividing_number -= 1

##=========2==========
length = len(sample_list)
chunk_size = int(length / 3)
start = 0
end = chunk_size

# run loop 3 times
for i in range(3):
    # get indexes
    indexes = slice(start, end)

    # get chunk
    list_chunk = sample_list[indexes]
    print("Chunk ", i, list_chunk)

    # reverse chunk
    print("After reversing it ", list(reversed(list_chunk)))

    start = end
    end += chunk_size

#######################################################################################
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

count_each = { i:sample_list.count(i) for i in sample_list }
print(count_each)

###2==============
count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("Printing count of each item  ", count_dict)

########################################################################
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

list_pair = set(zip(first_list,second_list))
print(list_pair)
########################################################################
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
print(set(first_set)-set(second_set))
##2=======
print("First Set ", first_set)
print("Second Set ", second_set)

intersection = first_set.intersection(second_set)
print("Intersection is ", intersection)
for item in intersection:
    first_set.remove(item)

print("First Set after removing common element ", first_set)

#########################################################################

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

print("First set is subset of second set - ",first_set.issubset(second_set))
print("Second set is subset of First set - ",second_set.issubset(first_set))

print("First set is Super set of second set - ",first_set.issuperset(second_set))
print("Second set is Super set of First set - ",second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print("First Set ", first_set)
print("Second Set ", second_set)

#####################################################################
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
print("List:", roll_number)
print("Dictionary:", sample_dict)
roll_number[:] = [i for i in roll_number if i in sample_dict.values()]
updated_list = [i for i in roll_number if i in sample_dict.values()]
print("After removing unwanted elements from list",roll_number)
print("After removing unwanted elements from list",updated_list)
########################################################################

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

print("Dictionary's values - ", speed.values())

speed_list = list()

# iterate dict values
for val in speed.values():
    # check if value not present in a list
    if val not in speed_list:
        speed_list.append(val)
print("unique list", speed_list)

#############################################################################
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
print("original list",sample_list)
l1 = [ i for i in sample_list if sample_list.count(i) == 1] # this removes completely which are repeated
print("After Removing duplicates",l1)
print("Tuple",tuple(l1))
print("Minimum", min(l1))
print("Maximum",max(l1))

##2============
sample_list = [87, 52, 44, 53, 54, 87, 52, 53]

print("Original list", sample_list)

sample_list = list(set(sample_list))
print("unique list", sample_list)

t = tuple(sample_list)
print("tuple ", t)

print("Minimum number is: ", min(t))
print("Maximum number is: ", max(t))

#==================================================================
def format_number(number):
    if number < 0:
        return "Pass only positive number"
    else:

        return '{:,}'.format(number) #python2 & python3
number = 2352232300
print("Original Number ",number)
print("built-in Number with thousand separator ",format_number(number))

def format_number(n):
    "1233452424"
    result = ""
    for i, digit in enumerate(reversed(str(n))):
        if i != 0 and (i % 3) == 0:
            result += ","
        result += digit
    print("Without reverse",result)

    return result[::-1]
print("With Logic Number with thousand separator ",format_number(number))

#================================================
def param_count(*args):
    return len(args)
print("No of Args Passed with param_count(2, 3, 4):" ,param_count(2, 3, 4))
print("No of Args Passed with param_count(2, 3):" ,param_count(2, 3))

#====================================================================
def list_xor(n,list1,list2):
    if (n in list1 and n not in list2) or (n not in list1 and n in list2):
        return True
    else:
        return False
print(list_xor(1, [1, 2, 3], [4, 5, 6]))
print(list_xor(1, [0, 2, 3], [1, 5, 6]))
print(list_xor(1, [1, 2, 3], [1, 5, 6]))
print(list_xor(1, [0, 0, 0], [4, 5, 6]))
print("="*70,"Inbuilt XOR")
def list_xor(n, list1, list2):
    return (n in list1) ^ (n in list2)

print(list_xor(1, [1, 2, 3], [4, 5, 6]))
print(list_xor(1, [0, 2, 3], [1, 5, 6]))
print(list_xor(1, [1, 2, 3], [1, 5, 6]))
print(list_xor(1, [0, 0, 0], [4, 5, 6]))

#============================================

import re

code = """
def validate(number):
    return number
"""


def validate(code):
    if "def" not in code:
        return "missing def"
    elif ":" not in code:
        return "missing :"
    elif "(" not in code or ")" not in code:
        return "missing paren"
    elif re.search("\([a-z-_]+\)", code) is None: #if "(" + ")" in code:
        return "missing param"
    elif "    " not in code:
        return "missing indent"
    elif "validate" not in code:
        return "wrong name"

    elif "return" not in code:
        return "missing return"


    else:
        return True


print(validate(code))

#=======================================================
print("="*70,"Defining custom zip")
def zap(list1, list2):
    tuple_list = []
    tuple_list = [(list1[i], list2[i]) for i in range(len(list1))]
    # for i in range(len(list1)):
    #     tuple_list.append((list1[i],list2[i]))
    return tuple_list

print(zap([0, 1, 2, 3],
          [5, 6, 7, 8]))

#====================================
def convert(list1):
    return list(map(str,list1))
print(convert([1,2,3,4]))
#=========================================================
def triple_and(a,b,c):
    return a and b and c
print(triple_and(True,True,True))
print(triple_and(False,True,True))
print(triple_and(True,False,True))
print(triple_and(False,True,False))
#===========================================================
def all_equal(list1):
    if list1 == []:
        return True
    return len(list(set(list1))) == 1

print(all_equal([1,1,5]))
print(all_equal([]))
# naive solution
def all_equal(items):
    for item1 in items:
        for item2 in items:
            if item1 != item2:
                return False
    return True

print(all_equal([1,1,1]))
print(all_equal([1,3,1]))

#==========================================
import re


def consecutive_zeros(string_number):
    maximux_count = re.findall("[0]+", string_number)
    if maximux_count == []:
        return 0
    return len(max(maximux_count))


print(consecutive_zeros("1001101000110"))

# naive solution
def consecutive_zeros(bin_str):
    result = 0
    streak = 0
    for letter in bin_str:
        if letter == "0":
            streak += 1
        else:
            streak = 0
        result = max(result, streak)
    return result
print(consecutive_zeros("10011000001000110"))

# shorter solution
def consecutive_zeros(bin_str):
    return max([len(s) for s in bin_str.split("1")])
print(consecutive_zeros("10011010110"))
#===============================
def up_down(x):
    return (x-1, x+1)
print(up_down(5))

#====================================
def palindrome(string):
    # if string == string[::-1]:
    #     return True
    # else:
    #     return False
    flag = 1
    for i in range(0, len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            flag = 0
            break
    if flag:
        return True
    else:
        return False


print(palindrome("mam"))
print(palindrome("abba"))


def palindrome(string):
    print(string)
    if len(string) < 2:
        return True
    return string[0] == string[-1] and palindrome(string[1:-1])

print(palindrome("abcd"))
print(palindrome("mamu"))
def palindrome(string):
    while len(string) > 1:
        head = string[0]
        tail = string[-1]
        string = string[1:-1]
        if head != tail:
            return False
    return True
print(palindrome("madam"))
print(palindrome("bob"))

#=======================================
def get_row_col(choice):
    translate = {"A": 0, "B": 1, "C": 2}
    letter = choice[0]
    number = choice[1]
    row = int(number) - 1
    column = translate[letter]
    return (row, column)


print(get_row_col("A3"), "A3")
print(get_row_col("C3"), "C3")
print(get_row_col("B2"), "B2")
print(get_row_col("B1"), "B1")
#========================================
def div_3(number):
    return number % 3 == 0
print(div_3(6))
print(div_3(5))
print(div_3(0))
#========================================
# naive solution
def largest_difference(numbers):
    smallest = 100
    for n in numbers:
        if n < smallest:
            smallest = n

    largest = -100
    for n in numbers:
        if n > largest:
            largest = n

    difference = largest - smallest
    return difference
print(largest_difference([1, 2, 3]))
def largest_difference(list1):
    return max(list1)-min(list1)

print(largest_difference([100, 5, 65]))
#=======================================
def flatten(list1):
    list2 = []
    for l in list1:
        list2.extend(l)
    return list2
print(flatten([[1, 2], [3, 4, 8]]))
def flatten(outer_list):
    return [
        item
        for inner_list in outer_list
        for item in inner_list
    ]
print(flatten([[1, 2], [3, 4]]))

#=================

def solution(A):

    # write your code in Python 3.6
    s = set(A)
    for x in range(1, 100002):
        if x not in s:
            return x

    # for i in range(len(A)+1):
    #     if i+1 not in A:
    #         return i+1
A = [1, 3, 6, 4, 1, 2]
print(solution(A))
A = [1, 2, 3]
print(solution(A))
A = [-1, -3]
print(solution(A))

A = [1,2,-1000000]
print(solution(A))




