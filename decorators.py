def decorator_lowercase(function):  # defining python decorator
    def wrapper():
        func = function()
        input_lowercase = func.lower()
        return input_lowercase

    return wrapper


@decorator_lowercase  # calling decorator
def intro():  # Normal function
    return 'Hello,I AM SAM'


print(intro())


def find_sum(function):
    def convert_to_str():
        fun = function()
        output = list(map(str, fun))

        return output

    return convert_to_str()


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
def my_name():
    return "doddahulugappa"


print(my_name())
