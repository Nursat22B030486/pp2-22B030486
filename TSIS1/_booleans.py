print(10 > 9)
print(10 == 9)
print(10 < 9)


a = 200
b = 33
if a > b:
    print("b is greater than a")
else:
    print("b is less than a")

print(bool("Hello")) # True
print(bool(5)) # True

a = "Hello"
b = 15
print(bool(a)) # True
print(bool(b)) # True

bool("abc") # True
bool(123) # True
bool(["apple", "cherry", "banana"]) # True

bool(False) # False
bool(None) # False
bool(0) # False
bool("",(),[],{}) # False

def function():
    return True
print(function()) # True
if function():
    print("YES!")
else:
    print("NO!")
    
x = 200
print(isinstance(x, int)) # True