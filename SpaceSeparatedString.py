def get_sentence(set_string, str1):
    string = ""
    counter = len(set_string)
    original_str = str1

    while string != str1 and counter:
        max_len = 0
        sub_str = ""
        for word in set_string:
            if str1.startswith(word):
                if len(word) > max_len:
                    max_len = len(word)
                    sub_str = word
        string += sub_str
        str1 = str1[len(sub_str):]
        counter -= 1
    if string == original_str:
        return "Yes", original_str
    return "No", original_str


if __name__ == "__main__":
    string_set = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"}
    print(get_sentence(string_set, "ilike"))
    print(get_sentence(string_set, "ilikesamsung"))
    print(get_sentence(string_set, "ilikesam"))
    print(get_sentence(string_set, "ilikeicecream"))
    print(get_sentence(string_set, "ilikeicecam"))
    print(get_sentence(string_set, "mobilemango"))
    print(get_sentence(string_set, "mobilemangogo"))
    print(get_sentence(string_set, "lik"))
    print(get_sentence(string_set, "ilikegomango"))
    print(get_sentence(string_set, "ilikehuli"))
    print(get_sentence(string_set, "ilikesamsungsammobilecreamicegomangoman"))
    print(get_sentence(string_set, "ilikesamsungsammobilecreamicegomangomanhuli"))
    print(get_sentence(string_set, "imancreamice"))
