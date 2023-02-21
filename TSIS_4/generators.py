# 1
def to_square(n):
    yield int(n)**2

# my_list = [1, 5, 6, 7]
for i in to_square(5):
    print(i)


# 2

def even_numbers(n):
    for i in range(n):
        if i %2 == 0:
            yield i
        else:
            continue

n = int(input())
my_list = []
for i in even_numbers(n):
    my_list.append(str(i))
print(", ".join(my_list))

# 3

def divisble(n):
    for i in range(n):
        if i%3==0 and i%4==0:
            yield i

number = int(input())
for i in divisble(number):
    print(i, end = ", ")

# 4
print("\n")
def squares(a, b):
    for i in range(a,b):
        yield i**2

num1, num2 = int(input()), int(input())
for i in squares(num1, num2):
    print(i)

# 5
def down(n):
    while n != 0:
        yield n-1
        n -= 1

num_1 = int(input())
for i in down(num_1):
    print(i)




