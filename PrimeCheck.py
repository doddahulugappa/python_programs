import math


def findout_prime_number(a):
    flag = True  # assume its prime
    for i in range(2, math.floor(math.sqrt(a)) + 1):
        if a % i == 0:
            flag = False  # set as not a prime
            break
    if not flag:
        print("its not a prime", a)
    else:
        print("its a prime", a)


findout_prime_number(5)
findout_prime_number(9)