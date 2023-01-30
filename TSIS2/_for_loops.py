fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
''' LOOPING THROUGH A STRING '''
for x in "banana":
    print(x)

''' BREAk '''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

''' CONTINUE '''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x) # apple cherry

''' THE RANGE() '''
for i in range(6):
    print(i)
for i in range(2, 6):
    print(i)
    for i in range(2, 30, 3):
        print(i) # 2 5 8 11 14 ...

''' ELSE in for loop '''        
for i in range(6):
    print(i)
else:
    print("Finally finished") # 1 2 3 4 5 Finall...

for i in range(6):
    if x == 3 : break
    print(x)
else:
    print("Finally finished!") # 0 1 2 

''' NESTED LOOP '''
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

''' The PASS statement '''
for i in [1, 2, 3]:
    pass