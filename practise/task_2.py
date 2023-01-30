''' task 2 '''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input())
k = set(a)
for i in range(n):
    command = input()
    if command != "pop":
        command2 = tuple(command.split())
        com = command2[0]
        el = command2[1]
        if com == "remove":
            k.remove(int(el)) 
        elif com == "discard":
            k.discard(int(el))
    else:
        k.pop()
print(k)