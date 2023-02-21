movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
# 1
# def above(movies):
#     for i in movies:
#         if i["imdb"] >= 5.5:
#             i["is_above"] = True
#         else:
#             i["is_above"] = False
#     return movies


# for i in above(movies):
#     print(i, "\n")
# print("\nFirst task -> 1\n")
# 2
def sub_lists(movies):
    sub_list = []
    for i in movies:
        if i["imdb"] >= 5.5:
            sub_list.append(i)
        
    return sub_list
print("\nSecond task -> 2\n")
for i in sub_lists(movies):
    print(i, "\n")

# # 3
# def filter_category(movies):
#     my_wish = input()
#     new_list = []
#     for i in movies:
#         if i["category"] == my_wish:
#             new_list.append(i)
#     return new_list


# print("\n Third task -> 3\n")
# for i in filter_category(movies):
#     print(i, "\n")

# # 4
# def average_imdb(movies):
#     total = 0
#     for i in movies:
#         total += i["imdb"]

#     return total/len(movies)

# print("\n Fourth task -> 4")
# print(average_imdb(movies))


# # 5
# def cat_ave_imdb(my_list):
#     total = 0
#     for i in my_list:
#         total += i["imdb"]
#     return total/len(my_list)
        

# cat_list = filter_category(movies)
# print(cat_ave_imdb(cat_list))
