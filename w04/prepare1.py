#ask for positive number
pos_number = int(input("Please enter a positive number: "))
while(pos_number < 0):
    print("Sorry, that is a negative number. Please try again.")
    pos_number = int(input("Please enter a positive number: "))
        
print(f'The number is {pos_number}')

answer = "no"
while(answer.lower() != "yes"):
    answer = input("Can I have a piece of candy? ")
print("Thank you!")