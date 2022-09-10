# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import string


def solution(S):
    # write your code in Python 3.6
    string_partition = len(S) // 2
    # if string_partition == 1:
    #     S = str.replace(S, "?", "m")
    #     return S
    flag = 0
    for c in range(0, string_partition+1):
        for letter in string.ascii_lowercase:
            if S[c] != "?" and S[len(S) - c - 1] != "?":
                if S[c] == S[len(S) - c - 1]:
                    flag = 1
                    break
                else:
                    return "NO"
            elif S[c] == "?":
                S = S[0:c] + letter + S[c + 1:]
                if S[c] == S[len(S) - c - 1]:
                    flag = 1
                    break
                elif S[len(S) - c - 1] == "?":
                    S = S[0:len(S) - c - 1] + S[c] + S[len(S) - c:]
                    if S[c] == S[len(S) - c - 1]:
                        flag = 1
                        break

            elif S[len(S) - c - 1] == "?":
                S = S[0:len(S) - c - 1] + S[c] + S[len(S) - c:]
                if S[c] == S[len(S) - c - 1]:
                    flag = 1
                    break
            elif S[c] == S[len(S) - c - 1]:
                flag = 1
                break


            else:
                return "No"
    if flag:
        return S
    else:
        return "NO"

print(solution("?ab??a"))
print(solution("bab??a"))
print(solution("?a?"))
print(solution("m?da?"))
print(solution("mal?yal??"))
print(solution("mal???"))

