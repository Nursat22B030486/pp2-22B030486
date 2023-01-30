my_set = {"apple", "banana", "cherry"}
print(my_set)

my_set = set(("apple", "banana", "cherry"))
print(my_set)

''' ACCESS ITEMS '''
my_set = {"apple", "banana", "cherry"}
for x in my_set:
    print(x)

''' CHECKING IT"S EXSIST '''
my_set = {"apple", "banana", "cherry"}
print("banana" in my_set)

''' ADD SET ITEMS '''
my_set = {"apple", "banana", "cherry"}
my_set.add("orange")
print(my_set)
# add SET
my_set = {"apple", "banana", "cherry"}
new_set = {"pineapple", "mango", "papaya"}
my_set.update(new_set)
print(my_set) # {'mango', 'banana', 'apple', 'cherry', 'papaya', 'pineapple'}
x = ["kiwi", "orange"]
my_set.update(x)
print(my_set) # {'papaya', 'banana', 'cherry', 'pineapple', 'apple', 'orange', 'mango', 'kiwi'}


''' REMOVE SET ITEMS '''
my_set = {"apple", "banana", "cherry"}
my_set.remove("banana")
my_set.discard("orange")
my_set.pop()
my_set.clear() # del my_set
print(my_set)


''' LOOPS SETS '''
my_set = {"appel", "banana", "cherry"}
for x in my_set:
    print(x)

''' JOIN SETS '''
# 1 BY USING UNION()
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# 2 USIGN UPDATE()
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3.update(set2)
print(set1)

''' KEEP ONLY THE DUPLICATES '''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x) # {'apple'}
z = x.intersection(y)
print(z) # {'apple'}

''' KEEO ALL, BUT NOT THE DUPLICATES '''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x) # {'banana', 'microsoft', 'cherry', 'google'}
z = x.symmetric_difference(y)
print(z) # {'banana', 'microsoft', 'cherry', 'google'}


