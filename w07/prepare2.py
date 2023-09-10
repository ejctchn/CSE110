def compute_area_square(side):
    area_square = side ** 2
    return area_square

keep_going = True
print("\nPlease enter one of the following numbers")
print("1. Square")
print("2. Rectangle")
print("3. Circle")

shape = int(input("\nWhat kind of shape do you have? "))


while(keep_going):
    try:
        side = float(input("What is the length of one side of the square? "))
        keep_going = False
    except ValueError:
        print("Please enter only integers")

area_square = compute_area_square(side)
print(f"The area of the square is: {area_square}")