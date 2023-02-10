triplets = [(x, y, z) for z in range(1, 100) for y in range(1, z) for x in range(1, y) if z ** 2 == x ** 2 + y ** 2]
print(triplets)

for z in range(1, 100):
    for y in range(1, z):
        for x in range(1, y):
            if z * z == x * x + y * y:
                print(x, y, z)

