roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def read_roman_string(str):
    sum = 0
    for char in str:
        sum += roman_dict[char]
    return sum


def print_roman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    while number:
        div, rem = divmod(number, num[i])
        number = rem

        while div:
            print(sym[i], end="")
            div -= 1
        i -= 1


total = read_roman_string("XXVVVVXXLDDCXXCXC")
print(total)

print_roman(total)