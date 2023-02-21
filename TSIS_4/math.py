import math

# 1
degree = int(input("Input degree: "))
radian = float(math.radians(degree))
print(f"Output radian: {radian:.6f}")


# 2
height = int(input("Height: "))
value_first = int(input("Base, first value: "))
value_second = int(input("Base, second value: "))
area = ((value_first + value_second)/2)*height
print(f"Expeccted Output: {area}")

# 3
num_sides = int(input("Input number of sides: "))
num_lenght = int(input("Input the length of a side: "))
area_regular_polygon = (num_sides*pow(num_lenght,2))/(4 * math.tan(math.pi/num_sides))
print(f"The area of the polygon is: {int(area_regular_polygon)}")



# 4
length = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area_of_parallelogram = float(length * height)
print(f"Expected Output: {area_of_parallelogram}")