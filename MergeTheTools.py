def merge_the_tools(string, k):
    if len(string) < 1 or len(string) > 10 ** 4:
        return
    if k < 1 or k > len(string):
        return
    if len(string) % k != 0:
        return
    # your code goes here
    i = 0
    while (True):
        output = string[i:i + k]
        temp_char = ""
        for char in output:
            if char not in temp_char:
                print(char, end="")
                temp_char += char
        print()
        i += k
        if i > len(string):
            break


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)