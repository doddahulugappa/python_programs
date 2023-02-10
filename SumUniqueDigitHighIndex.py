# unique sum of digits which have have highest index


def solution(a):
    """
    unique sum of digits which have have highest index
    :param: a
    :rtype: object
    """
    dict_sum = {}
    for i in range(len(a)):
        temp_sum_of_digits = 0
        num = a[i]
        while num:
            temp_sum_of_digits += num % 10
            num = num // 10
        dict_sum[i] = temp_sum_of_digits

    print(dict_sum)
    sum_of_two = {value: key for key, value in dict_sum.items() if
                  value == max(dict(filter(lambda elem: elem[1] == value, dict_sum.items())).values())}

    print(sum_of_two)


arr = [51, 71, 17, 42]
solution(arr)
