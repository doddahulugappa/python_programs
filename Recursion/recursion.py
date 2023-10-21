print("Factorial of given number ")


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(6))

"""
6 * factorial(5) ==> 720
5 * factorial(4) ==> 120
4 * factorial(3) ==> 24
3 * factorial(2) ==> 6
2 * factorial(1) ==> 2

"""

print("Fibonacci series")


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


for i in range(10):
    print(fib(i))

print("Addition of numbers")


def add(n):
    if n == 1:
        return 1
    return n + add(n - 1)


print(add(10))

print("GCD of given numbers")


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)


print(f"gcd(4, 6) is {gcd(4, 6)}")
print(f"gcd(3, 6) is {gcd(3, 6)}")
print(f"gcd(18, 12) is {gcd(18, 12)}")
print(f"gcd(3, 5) is {gcd(3, 5)}")
print(f"gcd(1, 5) is {gcd(1, 5)}")
print(f"gcd(30, 45) is {gcd(30, 45)}")

