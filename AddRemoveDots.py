# the longer way
def add_dots(s):
    out = ""
    for letter in s:
        out += letter + "."
    return out[:-1]


def remove_dots(s):
    out = ""
    for letter in s:
        if letter != ".":
            out += letter
    return out


string = "test"
print(remove_dots(add_dots(string)))

string = "t.e.s.t"
print(remove_dots(add_dots(string)))


# the short way
def add_dots(s):
    return ".".join(s)


def remove_dots(s):
    # return "".join(str1.split("."))
    return s.replace(".", "")


string = "test"
print(remove_dots(add_dots(string)))

string = "t.e.s.t"
print(remove_dots(add_dots(string)))
