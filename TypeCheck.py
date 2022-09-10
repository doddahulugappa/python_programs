def only_ints(a, b):
    if isinstance(b, bool) or isinstance(a, bool):
        return False
    return isinstance(a, int) and isinstance(b, int)

# def only_ints(a, b):
#     return type(a) == int and type(b) == int


print(only_ints(1, 2))
print(only_ints(1, "b"))
print(only_ints(1, True))
print(only_ints(False, 1))

import hashlib
password = ''
hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
print(hashed_password)



