# naive solution
def count(word):
    syllables = 1
    for letter in word:
        if letter == "-":
            syllables = syllables + 1
    return syllables

print(count("ho-tel"))
print(count("cat"))
print(count("met-a-phor"))
print(count("ter-min-a-tor"))

# using the count method
def count(word):
    return word.count("-") + 1

print(count("ho-tel"))
print(count("cat"))
print(count("met-a-phor"))
print(count("ter-min-a-tor"))

# using split
def count(word):
    return len(word.split("-"))

print(count("ho-tel"))
print(count("cat"))
print(count("met-a-phor"))
print(count("ter-min-a-tor"))