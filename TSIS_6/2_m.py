import string 
word = input()

count_lower = 0
count_upper = 0
for i in range(len(word)):
    if word[i] in string.ascii_lowercase:
        count_lower += 1
    elif word[i] in string.ascii_uppercase:
        count_upper += 1
    
print(count_lower, count_upper)


    