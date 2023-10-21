
def reverse_number(number):
    """
    Returns reversed number

    :return:
    """
    modify_num = -(number) if number < 0 else number


    rev = 0 # assume revrse is zero
    while(modify_num):
        rem = modify_num % 10 #4 #3 #2
        rev = rev * 10 + rem #4 #43 #432
        modify_num = modify_num // 10 #123 #12 # 1
    if number < 0:
        rev = 0-rev

    return rev

print(reverse_number(1234))
print(reverse_number(-1234))
print(reverse_number(-876))
print(reverse_number(876))

