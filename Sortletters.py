def sort_letter(letter):
    # for i in range(letter):
    #     for j in range(i+1,letter):
    #         if letter[i] < letter[j]:
    #             tmp = letter[i]
    #             letter[i] = letter[j]
    #             letter[j] = letter[i]
    return "".join(sorted(letter))

print(sort_letter("complication"))
print(sort_letter("apple"))
print(sort_letter("complex"))
print(sort_letter("love"))