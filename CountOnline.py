def online_count(dict1):
    new_dict = dict(filter(lambda elem: elem[1] == "online", dict1.items()))
    return len(new_dict)


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

print(online_count(statuses))