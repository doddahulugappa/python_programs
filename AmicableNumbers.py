def find_factors(num):
    return [i for i in range(1,num) if num % i == 0]
a = find_factors(220)
b = find_factors(284)
print(a,sum(a))
print(b,sum(b))


# Python3 program to count
# amicable pairs in an array
# Calculate the sum
# of proper divisors
def sumOfDiv(x):
    sum = 1
    for i in range(2, x):
        if x % i == 0:
            sum += i
    return sum


# Check if pair is amicable
def CheckAmicable(a, b):
    if sumOfDiv(a) == b and sumOfDiv(b) == a:
        return True
    else:
        return False


def countPairs(arr, n):
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if CheckAmicable(arr[i], arr[j]):
                count = count + 1
    return count


list1 = [220, 284, 1184,
         1210, 2, 5]
n1 = len(list1)
print(countPairs(list1, n1))

list2 = [2620, 2924, 5020,
         5564, 6232, 6368]
n2 = len(list2)
print(countPairs(list2, n2))

def count_amicable_pairs(n):
    counter = 0
    pair = []
    for i in range(1,n+1):
        fact_sum = sum(find_factors(i))
        if fact_sum != i:
            pair_fact_sum = sum(find_factors(fact_sum))
            if i == pair_fact_sum:
                if set([i,fact_sum]) not in pair:
                    pair.append(set([i,fact_sum]))
                    print(i,fact_sum)
                    counter += 1
    return counter

print(count_amicable_pairs(300))
print(count_amicable_pairs(6000))
print(count_amicable_pairs(10000))
print(count_amicable_pairs(18000))