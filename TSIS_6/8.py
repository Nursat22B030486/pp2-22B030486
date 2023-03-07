import os 

my_path = 'C://Users//Kordabay Nursat//KBTU\'\'22//Python//Git_hub//pp2-22B030486//TSIS_6//'
removing_file = 'second.txt'
specified_path = os.path.join(my_path, removing_file)
try: 
    if os.path.exists(os.path.join(my_path, removing_file)):
        print("Exists!")
        print(os.access(removing_file, os.X_OK))
        os.remove(specified_path)
except: pass
    
  
    