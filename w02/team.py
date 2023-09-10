import math

#1
square = float(input("What is the length of a side of the square? "))
print(f'The area of the square is: {square**2}')

#2
rect_l = float(input("What is the length of rectangle? "))
rect_w = float(input("What is the width of rectangle? "))
print(f'The area of the rectangle is: {rect_l * rect_w}')

#3
radius = float(input("What is the radius of the circle? "))
circle_a = 3.14 * (radius**2)
print(f'The area of the circle is: {circle_a:.1f}')


#Stretch Challenges

#1
radius = float(input("What is the radius of the circle? "))
circle_a = math.pi * (radius**2)
print(f'The area of the circle is: {circle_a:.1f}')

#2
single_input = float(input("Enter a value: "))
print(f'The area of the square is: {single_input**2}')

single_circle_a = math.pi * (single_input**2)
print(f'The area of the circle is: {single_circle_a}')

print(f'The area of the cube is: {single_input**3}')
sphere_a = (4/3) * math.pi * (single_input**3)
print(f'The area of the sphere is: {sphere_a}')

#3
print("Please enter the following in centimeters.")
square = float(input("What is the length of a side of the square? "))
print(f'Centimeters Squared: {square**2}')
print(f'Meters Squared: {(square**2)/10000}')

rect_l = float(input("What is the length of rectangle? "))
rect_w = float(input("What is the width of rectangle? "))
print(f'Centimeters Squared: {rect_l * rect_w}')
print(f'Meters Squared: {(rect_l * rect_w)/10000}')

radius = float(input("What is the radius of the circle? "))
circle_a = 3.14 * (radius**2)
print(f'Centimeters Squared: {circle_a:.1f}')
print(f'Meters Squared: {(circle_a)/10000}')
