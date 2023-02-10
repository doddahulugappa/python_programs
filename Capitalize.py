def solve(s):
    if len(s) < 0 or len(s) >= 1000:
        return
    words = s.split()
    result = []
    for item in words:
        if item.isalpha():
            result.append(item.title())

    for word in result:
        if word.lower() in s:
            s = s.replace(word.lower(), word)
    return s


s = "hello world"
print(solve(s))
