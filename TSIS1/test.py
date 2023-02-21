sentence = "My name is Nursat"
my_list = []
result = ""
for i in sentence:
    if i != " ":
        result += i
    else:
        my_list.append(result)
        result = ""
my_list.append(result)
print(my_list)

