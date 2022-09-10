def sort_words(letter):
    letter = letter.split()
    for i in range(len(letter)):
        for j in range(i+1,len(letter)):
            if letter[j] < letter[i]:
                tmp = letter[j]
                letter[j] = letter[i]
                letter[i] = tmp
    return letter

print(sort_words("my name is huli"))
print(sort_words("hello world how are you"))
print(sort_words("Hi Praveen Prajwal"))
print(sort_words("love like a doll"))
a=5
b=10

# c=a
# a=b
# b=c
a,b=b,a
print(a,b)