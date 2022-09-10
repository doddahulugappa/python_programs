def online_count(dict1):
    newDict = dict(filter(lambda elem: elem[1] == "online", dict1.items()))
    return len(newDict)


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

print(online_count(statuses))