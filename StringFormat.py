def print_formatted(number):
    # your code goes here
    bin_len = len(bin(number))-1
    # print(bin_len)
    for i in range(1,number+1):
        print(str(i).rjust(bin_len-1)+oct(i)[2:].rjust(bin_len)+hex(i)[2:].upper().rjust(bin_len)+bin(i)[2:].rjust(bin_len))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)