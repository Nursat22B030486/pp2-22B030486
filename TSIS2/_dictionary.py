''' CREATING THE DICTIONARY '''
my_dict = {
    "brand" : "FORD",
    "model" : "MUSTANG",
    "year" : 1964
}
print(my_dict)

''' DICTIONARY ITEMS '''
my_dict = {
    "brand" : "FORD",
    "model" : "MUSTANG",
    "year" : 1964
}
print(my_dict["brand"])

''' DUPLICATES NOT ALLOWED '''
my_dict = {
    "brand" : "FORD",
    "model" : "MUSTANG",
    "year" : 1964,
    "year" : 2000
}
print(my_dict) # {'brand': 'FORD', 'model': 'MUSTANG', 'year': 2000} 
print(len(my_dict)) # 3

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(thisdict)) # <class 'dict'>

''' THE DICT() CONSTRUCTOR '''
my_dict =  dict(name = "Nursat", age = 36, country = "KZ")
print(my_dict) # {'name': 'Nursat', 'age': 36, 'country': 'KZ'}

'''  ACCESS DICTIONARY ITEMS '''
my_dict = {
    "brand" : "FORD",
    "model" : "MUSTANG",
    "year" : 1964
}
x = my_dict["model"] # MUSTANG
y = my_dict.get("year")  # 1964
x = my_dict.keys() # dict_keys(['brand', 'model', 'year'])
my_dict["color"] = "blue"
print(my_dict.keys()) # dict_keys(['brand', 'model', 'year', 'color'])
print(my_dict.values()) # dict_values(['FORD', 'MUSTANG', 1964, 'blue'])
print(my_dict.items()) # dict_items([('brand', 'FORD'), ('model', 'MUSTANG'), ('year', 1964), ('color', 'blue')])

''' CHECK IF KEY EXISTS '''
my_dict = {
    "brand" : "FORD",
    "model" : "MUSTANG",
    "year" : 1964
}
if "model" in my_dict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

 
''' CHANGE DICTIONARY ITEMS '''
# change the value
my_dict = {
    "brand" : "FORD",
    "model" : "MUSTANG",
    "year" : 1964
}
my_dict["year"] = 5555 # year 5555
my_dict.update({"year" : 2020}) # year 2020

''' ADD DICTIONARY ITEMS '''
my_dict = {
    "brand" : "FORD",
    "model" : "MUSTANG",
    "year" : 1964
}
my_dict["color"] = "blue"
my_dict.update({"doors": 7})


''' REMOVING DICTIONARY ITEMS '''
my_dict = {
    "brand" : "FORD",
    "model" : "MUSTANG",
    "year" : 1964
}
my_dict.pop("model")
print(my_dict) # {'brand': 'Ford', 'year': 1964} 
my_dict.popitem()
print(my_dict) # {'brand': 'FORD'}
del my_dict["brand"]
print(my_dict) # {}

my_dict = {
    "brand" : "FORD",
    "model" : "MUSTANG",
    "year" : 1964
}
my_dict.clear()
print(my_dict) # {}

''' LOOPS DICTIONARY '''
my_dict = {
    "brand" : "FORD",
    "model" : "MUSTANG",
    "year" : 1964
}
for x in my_dict:
    print(x) # print all key names 
    print(my_dict[x]) # print all the values

for i in my_dict.values():
    print(i)
for o in my_dict.keys():
    print(o)

for x, y in my_dict.items():
    print(x, y)

''' COPY DICTIONARY '''
my_dict = {
    "brand" : "FORD",
    "model" : "MUSTANG",
    "year" : 1964
}
my_dict1 = my_dict.copy()
print(my_dict1) # {'brand': 'FORD', 'model': 'MUSTANG', 'year': 1964}


my_dict = {
    "brand" : "FORD",
    "model" : "MUSTANG",
    "year" : 1964
}
my_dict1 = dict(my_dict)
print(my_dict1) 

''' NESTED DICTIONARY '''
my_dict = {
    "child1" : {"namme" : "Emil", "year" : 2004},
    "child2" : {"name" : "Toby", "year" : 2005},
    "child3" : {"name" : "Linus", "year" : 2011}
}
child1 = {"namme" : "Emil", "year" : 2004},
child2 = {"name" : "Toby", "year" : 2005},
child3 = {"name" : "Linus", "year" : 2011}
my_family = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}