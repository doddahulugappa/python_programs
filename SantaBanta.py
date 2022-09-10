
numbers = input("enter numbers:")
numbers = numbers.split()

numbers = list(map(int,numbers))
abs_sum_list = []
for number in numbers:
    abs_sum = [abs(num-number) for num in numbers]
    abs_sum_list.append(sum(abs_sum))
print(min(abs_sum_list))
