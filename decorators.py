def decorator_lowercase(function):   # defining python decorator
    def wrapper():
        func = function()
        input_lowercase = func.lower()
        return input_lowercase
    return wrapper
@decorator_lowercase    ##calling decoractor
def intro():                        #Normal function
    return 'Hello,I AM SAM'
print(intro())


def find_sum(function):
    def findsum():
        fun = function()
        output = list(map(str,fun))

        return  output
    return findsum()

@find_sum
def array_sum():
    return list(range(10))

print(array_sum)

def decorate_title(function):
    def deco():
        str1 = function()
        return str1.capitalize()
    return deco
@decorate_title
def myname():
    return "doddahulugappa"

print(myname())

for i in range(10):
    print(i)
    if i == 3:
        continue
    elif i==5:
        pass
    elif i == 8:
        break
    # else:
    #     print(i)