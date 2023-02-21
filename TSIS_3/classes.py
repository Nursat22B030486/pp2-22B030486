# 1
# class A:
#     def __init__(self):
#         pass

#     def get_string(self):
#         self.word = input()
    

#     def print_string(self):
#         print(self.word.upper())

# words = A()
# words.get_string()
# words.print_string()

# 2 and 3
class Shape():
    def __init__(self, length, width):
        self.length = length
        self.width = width
   
class Square(Shape):
    
    def __init__(self, length):
         self.length = length
    def area(self):
        return self.length**2

class Rectangle(Shape):
        # def __init__(self, length, width):
        #     super().__init__(sel...)
      
        def area(self):
            return self.length * self.width
my_wish = Rectangle(5, 8)
print(my_wish.area())
my_wish2 = Square(8)
print(my_wish2.area())


# # 4
# class Point():
#         def __init__(self, x, y):
#             self.x = x
#             self.y = y

#         def show(self):
#               return self.x, self.y
        

#         def move(self, dx, dy):
#             self.x += dx
#             self.y += dy
#             return f"({self.x}, {self.y})"
            
            

#         def dist(self, other):
#             return f"{(((self.x - other.x)**2)+((self.y - other.y)**2))**0.5 :.2f}"
        
        
#         def __str__(self):
#               return f"({self.x}, {self.y})"
        
# point1 = Point(2, 1)
# point2 = Point(3, 8)
# point1.move(5, 4)
# print(point1.dist(point2))
# print(point1.__str__())

# 5
# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, depo):
#         self.balance = self.balance + depo
#         return f"You give us {depo}"
        
        

#     def withdraw(self, withd):
#         if withd > self.balance:
#             print(f"You {self.owner} can't receive money")
#         else:
#             self.balance -= withd
#             print(f"You ({self.owner}) have {self.balance} money")
        
# my_account = Account("Nursat", 15000)
# my_account.deposit(4500)
# my_account.withdraw(17500)


# 6
# def prime(x):
#     count = 0
#     for i in range(2,int(x)):
#         if (int(x)%i== 0):
#             return False
#     if int(x) == 1:
#         return False
#     return True

# my_list = list(input())
# new_list = []
# new_list = list(filter(lambda x: prime(x), my_list))
# print(new_list)
