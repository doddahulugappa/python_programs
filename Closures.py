"""
Closure in Python is an inner function object, a function that behaves like an object,
that remembers and has access to variables in the local scope in which it was created
even after the outer function has finished executing
"""

def increment(start):
    def inc(step=1):
        nonlocal start
        start += step
        return start
    return inc


my_inc = increment(5)
print(my_inc(2))
print(my_inc(3))
print(my_inc(5))
print(my_inc(6))
print(my_inc(7))
print(my_inc)
print(my_inc(2), end=' ')
print(my_inc(3), end=" ")
print(my_inc(5), end=" ")
print(my_inc(6), end=" ")
print(my_inc(7), end="\n")
print(my_inc)
print(my_inc.__defaults__)

