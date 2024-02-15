#degree to radian
pi=22/7
value = 15
degree = float(value)
radian = degree*(pi/180)
print(radian)

#trapezoid area
base1 = 5
base2 = 6
height = float(5)
base_1 = float(base1)
base_2 = float(base2)
area = ((base1 + base2) / 2) * height
print("Area is:", area)

#area of parallelogram
base = float(5)
height = float(6)
area = base * height
print("Area is: ", area)

#area of regular polygon
from math import tan, pi
sides = 4
length = float(25)
area = sides * (length ** 2) / (4 * tan(pi / sides))
print("The area of the polygon is: ",area)