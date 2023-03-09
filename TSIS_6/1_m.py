import math
my_list = list(map(int, input().split()))
print(math.prod(my_list))


result = 1
for i in range(len(my_list)):
    result *= my_list[i]


print(result)
