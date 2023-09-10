'''
I added the ability to check if the tender payment amount
is too little to cover the bill. In which case, a message
is displayed to tell the user that they need to offer more 
to cover the bill.
I also added the ability to add gratuity(tip) to the bill.
'''
# slam the user with questions
print()
meal_child_price = float(input("What is the price of a child's meal? "))
meal_adult_price = float(input("What is the price of an adult's meal? "))
num_child = int(input("How many children are there? "))
num_adult = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))
paid = False
tip_accepted = False

#tip?
while(not tip_accepted):
    tip_yn = input("Would you like to add a tip (y/n)? ")
    if(tip_yn.lower() == 'y'):
        tip_amount = float(input("How much would you like to tip? "))
        tip_accepted = True
    elif(tip_yn.lower() == 'n'):
        tip_amount = 0
        tip_accepted = True
    else:
        print("That is not a valid input. Please enter only 'y' or 'n' (without quotes).")
        print()


#compute. total. beep boop...
total_child = meal_child_price * num_child
total_adult = meal_adult_price * num_adult
total_sub = total_adult + total_child + tip_amount

# Give the state some MONEYYYYYYY
tax = total_sub * (tax_rate / 100)
total_final = tax + total_sub

# display the girthy green paper to the user
print()
print(f'Subtotal: ${total_sub:.2f}')
print(f'Sales Tax: ${tax:.2f}')
print(f'Total: ${total_final:.2f}')
print()



# GIVE ME THE MOOLAH
while(not paid):
    tender = float(input("What is the payment amount? "))
    # how dare you shortchange me
    if(tender < total_final):
        print("How dare you shortchange me... I REQUIRE MORE!")
        print()
    else:
        change = tender - total_final
        paid = True

# reluctantly give the change...
print(f'Change: ${change:.2f}')
print()