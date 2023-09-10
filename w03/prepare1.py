# numbers (if-else Statements)
print()
num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))

#is the first number greater?
if(num1 > num2):
    print("The first number is greater.")
else:
    print("The first number is not greater.")

# are the numbers equal?
if(num1 == num2):
    print("The numbers are equal")
else:
    print("The numbers are not equal")

#is the second number greater?
if(num1 < num2):
    print("The second number is greater")
else:
    print("The second number is not greater")

print()
animal = input("What is your favorite animal? ")

if(animal.lower() == "tiger"):
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")
print()