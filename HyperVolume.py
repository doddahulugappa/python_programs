# import functools


def hyperVolume(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v

print(hyperVolume(1, 2, 5, 4, 5))
l = [1, 2, 5, 4, 5]
print(functools.reduce(lambda a, b: a*b, l))
