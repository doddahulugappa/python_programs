def get_gcd(m,n):
    # print(m,n,"*********")
    if m % n == 0:
        return n
    else:
     return get_gcd(n,m%n)
def CountNoChacolate(m,n):
    if m%n == 0:
        return 1

    else:
        gcd = get_gcd(m, n)
        print("N {} / GCD {} = No Of Chacolates {} with M {} steps".format(n,gcd,int(n//gcd),m))
        return(n//gcd)
print(CountNoChacolate(4,12))
print(CountNoChacolate(12,5))
print(CountNoChacolate(12,3))
print(CountNoChacolate(12,18))
print(CountNoChacolate(6,8))
print(CountNoChacolate(6,3))

# print(get_gcd(12,8),"GCD")
# print(get_gcd(12,6),"GCD")
# print(get_gcd(12,5),"GCD")
# print(get_gcd(12,9),"GCD")
import math
def findout_prime_number(a):
    flag = True # assume its prime
    for i in range(2,math.floor(math.sqrt(a))+1):
        if a%i == 0:
            flag = False #set as not a prime
            break
    if flag == False:
        print("its not a prime", a)
    else:
        print("its a prime",a)

findout_prime_number(5)
findout_prime_number(9)