import os

def create_file(file_name, my_list):
    f = open(f'{file_name}.txt', 'x')
    f.write(my_list)
    f.close()

text = str(list((input().split())))
create_file(input(), text)



                     