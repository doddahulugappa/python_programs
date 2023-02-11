# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    """
    Returns the length of the longest palindromic subsequence in 'str'
    :param S:
    :return: longest polindrome subsequence
    """
    n = len(S)

    # Create a table to store
    # results of sub problems
    L = [[0 for x in range(n)] for y in range(n)]

    # Sings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1

    # Build the table. Note that
    # the lower diagonal values
    # of table are useless and
    # not filled in the process.
    # c1 is length of substring
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if (S[i] == S[j] and cl == 2):
                L[i][j] = 2
            elif (S[i] == S[j]):
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i][j - 1], L[i + 1][j])

    return L[0][n - 1]



def minimumNumberOfDeletions(str):
    """
    # function to calculate minimum number of deletions
    :param str:
    :return: number of letters to be deleted
    """
    n = len(str)

    # Find longest palindromic subsequence
    l = solution(str)

    # After removing characters other than the long_poly_sub, we get palindrome.
    return (n - l)

string = "ervervige"
print(minimumNumberOfDeletions(string))

l1 = ['1', '2', '3', 8, 9]
l2 = [3,6,8]
a = 5
b = 10
print(a,"+",b,"=",a+b,"(a+b)")
l3 = []
for i,j in enumerate(l1):
    print(i,"===>",j)
    if i%2 == 1:
        l3.append(j)
for i,j in enumerate(l2):
    if i%2 == 0:
        l3.append(j)
print(l3)


def square(x):
    return x*x

l1 = [ 1, 2 , 3, 4, 5]

squared_list = list(map(square,l1))
squared_list = list(map(lambda x:x*x,l1))
print(squared_list)





