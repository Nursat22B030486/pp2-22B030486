from generator import fake_user_generator

class User:
    def __init__(self, username, age, gender, created_at):
        self.username = username
        self.age = age
        self.gender = gender
        self.created_at = created_at

    def age_group(self):
        if 0 < self.age and self.age < 12:
            return 'Child'
        elif 13 < self.age and self.age < 17:
            return 'Adolescent'
        elif 18 < self.age and self.age < 65:
            return 'Adult'
        elif 65 <= self.age:
            return 'Old adult'
    
user_generator = fake_user_generator()
count = 0
for _ in range(1000):
    new_user = next(user_generator)
    count += 1
 
    print('User:', new_user)
    user = User(new_user['username'], new_user['age'], new_user['gender'], new_user['created_at'])
    print(f'{user.username} age group is', user.age_group(), "\n")
print(count)