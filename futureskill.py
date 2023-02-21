a = 1, 2, 3
# a[0] = 12
print(a)

a = "hrli saf safsa"
print(list(a))


def ae(a, *b, **c):
    print(type(a), type(b), type(c))


ae(4, 5, name="huli")

counter = 1


def do_lot(a):
    def inner(b):
        global counter
        nonlocal a
        for i in (1, 2, 3):
            counter += 1
            a += b

    inner(a + [0])


x = []
do_lot(x)
print(counter, x)


class english(object):
    def __init__(self, sen):
        self.sen = sen

    def printme(self):
        for line in self.sen:
            print(line)


word_sent = english(["this", "is", "book"])
word_sent1 = english(["and its love"])
word_sent1.printme()
word_sent.printme()

sum = -1
count = 0
pylist = [1, 2, 3, 4, 5, 6]
for j in pylist[::-1]:
    if j == 3 or count >= 2:
        pass
    else:
        sum += j
        count += 1

print(sum, "sum")
