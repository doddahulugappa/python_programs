def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    print(len(s))
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s) - i)
        else:
            stusc += (len(s) - i)
        print(kevsc,stusc)
    # print(kevsc,stusc)
    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)