import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def is_valid(email):
    if re.fullmatch(regex, email):
        print("Valid email")
    else:
        print("Invalid email")


is_valid("name.surname@gmail.com")
is_valid("anonymous123@yahoo.co.uk")
is_valid("anonymous123@...uk")
is_valid("...@domain.us")
is_valid("lara@hackerrank.com")
is_valid("brian-23@hackerrank.com")
is_valid("britts_54@hackerrank.com")
