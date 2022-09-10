# easy solution
def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

print(is_anagram("typhoon", "opython"))
print(is_anagram("Alice", "Bob"))

# harder solution:
# count how many times each letter appears in each string,
# and make sure all the counts are the same.
def count_letters(string):
    return {l: string.count(l) for l in string}
def is_anagram(string1, string2):
    print(count_letters(string1),count_letters(string2))
    return count_letters(string1) == count_letters(string2)

print(is_anagram("typhoon", "opython"))
print(is_anagram("Alice", "Bob"))

