def balance(sequence):
    while True:
        if '()' in sequence:
            sequence = sequence.replace('()', '')
        elif '{}' in sequence:
            sequence = sequence.replace('{}', '')
        elif '[]' in sequence:
            sequence = sequence.replace('[]', '')
        else:
            return not sequence


print(balance("(){}[]"))
print(balance("(){[]"))
print(balance("{[]}"))
print(balance("({[]})"))
print(balance("({[]})()"))
