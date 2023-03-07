import os

 
specified_path = 'C://Users//Kordabay Nursat//KBTU\'\'22//Git_hub//'
os.getcwd()
os.chdir('../')
# try:
#     if os.path.exists(os.getcwd()):
#         print("Exists")
#         print(os.path.dirname(os.getcwd()))
#         print(os.path.basename(os.getcwd()))
# except:
#     print('I didn\'t find!!!')
# if os.path.exists(os.getcwd()):
#     print("Exists")
#     print(os.path.dirname(os.getcwd()))
#     print(os.path.basename(os.getcwd()))
# else: print("I didn\'t find!!!")
try:
    if os.path.exists(specified_path):
        print("Exists")
        print(os.path.dirname(specified_path))
        print(os.path.basename(specified_path))
finally:
    print('I didn\'t find!!!')