import os

os.getcwd()
my_dir = 'C://Users//Kordabay Nursat//KBTU\'\'22//Python//Git_hub//pp2-22B030486//'
print('Is it executed?!',os.access(my_dir, os.X_OK))


my_dir = 'C://Users//Kordabay Nursat//KBTU\'\'22//Python//pp2-22B030486//'
print('Is it executed?!',os.access(my_dir, os.X_OK))

print('Is path exist?!',os.path.exists(my_dir))

current = os.getcwdb()
print('Is it readable?',os.access(current, os.R_OK))

os.chdir('../')
print(os.getcwd())
print('Is it writable?!', os.access(os.getcwd(), os.W_OK & os.R_OK))


