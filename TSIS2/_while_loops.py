""" WHILE LOOPS """
i = 1
while i < 6:
    print(i)
    i += 1 

''' THE BREAK STATEMENT '''
i = 1
while  i < 6:
    print(i)
    if i == 3:
        break
    i += 1

''' THE CONTINUE STATEMENTS '''
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

''' THE ELSE STATEMENT '''
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")