# 1
# def calculate(grams):
#     return 28.3495231 * grams


# grams = int(input())
# print(calculate(grams))

# # 2
# def convert(f):
#     return (5 / 9) * (f - 32)


# temparature = int(input())
# print(convert(temparature))

# # 3
def solve(numheads, numlegs):
    for i in range(numheads):
        if (numheads-i)*2 + i*4 == numlegs:
            return i
    return 0

numheads, numlegs  = int(input()), int(input())
result = solve(numheads, numlegs)
if result != 0:
    print(f"We have {result} rabbits and {numheads-result} chicken")
else:
    print("NO solution")


# # 4
# def prime(my_list):
    
#     new_list = []
#     for x in my_list:
#         count = 0
#         for i in range(1,int(x)+1):
#             if int(x)%i == 0:
#                 count += 1
#         if count == 2:
#             new_list.append(x)
#     return new_list


# my_list = list(input())
# print(prime(my_list))

# 5
# def all_permutations(words):
#     for i in range
# all_permutations("abacaba")

# 6
# def reverse(words):
    
#     result = ""
#     total = ""
#     for x in words[::-1]:
#         if x != ' ':
#             result += x
#         else:
#             total += result[::-1] + ' '
#             result = ""
#     total += result[::-1]
#     return total
   
    
# words = input()
# print(reverse(words))

# 7
# def has_33(nums):
#     for i in range(len(nums)-1):
#         if int(nums[i]) == int(3):
#             if int(nums[i+1]) == int(3):
#                 return True
#     return False    

# my_list = list(input())
# print(has_33(my_list))

# # 8
# def spy_game(nums):
#     for i in range(len(nums)):
#         if int(nums[i]) == int(0):
#             for j in range(i+1,len(nums)):
#                 if int(nums[j]) == int(0):
#                     for k in range(j, len(nums)):
#                         if int(nums[k]) == int(7):
#                             return True
#     return False

# my_list = list(input())
# print(spy_game(my_list))

# 9 
# def volume(n):
#     return 4/3 * 3.14 * n**3

# radius = int(input()) 
# print(volume(radius))

# 10 
# def remove_duplicates(my_list):
#     new_list = []
#     for i in my_list:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list


# my_list = list(input())
# print(remove_duplicates(my_list))

# 11
# def is_polindrome(s):
#     a = s[::1]
#     if a == s:
#         return True
#     return False

# word = input()
# print(is_polindrome(word))

# 12
# def histogram(my_list):
#     for i in my_list:
#         print("*" * int(i))
           

# my_list = list(input())
# print(histogram(my_list))

# 13
# import random

# rand_num = random.randint(1, 21)
# print(rand_num)
# def guess_num(count,rand_num):
#     num = int(input())
#     if(num > rand_num):
#         print(f"Your guess is too up. \nTake a guess.\n")
#         count += 1
#         guess_num(count,rand_num)
#     elif(num < rand_num):
#         print(f"Your guess is too low.\nTake a guess.\n")
#         guess_num(count,rand_num)
#         count +=1
#     else:
#         print(f"Good job, KBTU! You guessed my number in {count+1} guesses!")


# name = input("Hello! What is your name?\n")
# print(f"\nWell, {name}, I am thinking of a number between 1 and 20.\nTake a guess.\n")
# count = 0
# guess_num(count,rand_num)




