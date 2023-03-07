import os

print(os.getcwd())

my_dir = os.chdir('C://Users//Kordabay Nursat//KBTU\'\'22//Python//Git_hub//pp2-22B030486//')
print(os.getcwd())

for item in os.listdir(my_dir):
    if os.path.isdir(item):
        print(item)

my_dir = os.chdir('./bonus')
print(os.getcwd())

for item in os.listdir(my_dir):
    if os.path.isfile(item):
        print(item)