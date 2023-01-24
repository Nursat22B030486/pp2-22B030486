''' Python Conditions and If statements 
        a = b
        a != b
        a < b
        a > b
        a <= b
        b >= a

'''
a = 3
b = 200
if b > a:
    print("b is greater than")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

if a > b:
    print("a is greater than b")
else: 
    print("b is greater than b")

''' Short Hand if '''
if a > b: print("a is greater than b")


''' Short Hand if...else '''
a = 2
b = 330
print("A") if a > b else print ("b")

a = 220
b = 220
print("a") if a > b else print("=") if a == b else print("b")


a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditins are True")
if a > b or a > c:
    print("At least one of the conditions is True") 

x = 41
if x > 10:
    print("Above ten")
    if x > 20:
        print("and also above 20!")
    else: print("but not above 20.")

a = 33
b = 200
if b > a:
    pass
