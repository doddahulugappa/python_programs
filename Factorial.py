def find_factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * find_factorial(number - 1)  # 5*fact(4),4*fact(3),3*fact(2),2*fact(1)

    # else:
    #     fact = 1
    #     for i in range(1,number+1):
    #         fact = fact * i
    # ======================
    #     fact = 1
    #     while(number>1):
    #       fact *= number
    #       number = number - 1

    return fact


print(find_factorial(5))
print(find_factorial(6))
print(find_factorial(4))
print(find_factorial(8))
