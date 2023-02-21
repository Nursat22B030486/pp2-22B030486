from users import users
from datetime import datetime

def age(birthdate):
    date = datetime.strptime(birthdate, "%Y-%m-%d")
    today =  datetime.now()
    age = today.year - date.year - ((today.month, today. day) < (date.month, date.day))
    return age

def ab_group(users, max_age):
    filtered_date = (user for user in users if age(user["birthdate"]) <= max_age)
    sorted_date = sort(filtered_date, key = lambda x: x['height'])
    group_a, group_b = [], []
    for i in range(len(sorted_date)):
        (group_a if i%2 == 0 else group_b).append(sorted_date[i])

    return group_a, group_b

def ave_height(users):
    total_height = sum(user["height"] for user in users)
    return total_height/len(users)


max_age = 40
group_a, group_b = ave
print(age('1975-03-15'))
print(ave_height(users))
print(type(age('1975-03-15')))