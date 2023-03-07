import os


# with open('first.txt', 'r') as f:
#     copy_text = f.read()
#     second_file = open("second.txt", 'w')
#     second_file.write(copy_text)
#     second_file.close()

import shutil
source = ('C://Users//Kordabay Nursat//KBTU\'\'22//Python//Git_hub//pp2-22B030486//TSIS_6//first.txt')
new_file = 'second.txt'
try :
    # if not os.path.exists(new_file):
    with open(new_file, 'x'):
        print("New file created!")    
        pass
except FileExistsError: 
    print('Such name file already exists!')

destination = ('C://Users//Kordabay Nursat//KBTU\'\'22//Python//Git_hub//pp2-22B030486//TSIS_6//second.txt')

with open('first.txt', 'r')as f:
    print('Text from first file:', f.read())
    file_2 = open('second.txt', 'r+')
    print('Before copy:', file_2.read())
    shutil.copy(source, destination)
    print('Arter copy:', file_2.read())

