''' task 4 '''
sentence = input() # hello hello my name is Nursat bye bye
my_dict = {}

for word in sentence.split():
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1
print(my_dict)