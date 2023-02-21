
import random 
from datetime import datetime
random_words = ['liam', 'snake', 
        'pool', 'ggg', 'hurray', 'yo', 'rock', 'football', 'basket', 'ice_cream', 'bing',
'chilling']
surnames = ['smith', 'black', 
'white', 'johnson', 'williams', 'jones', 'millers', 'wilson', 'anderson', 'holmes',
'moore']

def fake_user_generator():
    i = 0
    while i != 100:
        i += 1

        username = random.choice(random_words) + str(random.randint(0, 100)) + random.choice(surnames)

        date = {
            'username' : username,
            'age' : random.randint(0, 100),
            'gender' : random.choice(['female', 'male']),
            'created_at': datetime.now().strftime("%x")
        }
        yield date
    
