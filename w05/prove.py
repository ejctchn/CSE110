"""
    1 - I added the ability to check if the user enters something other than
        numerical values when the user shouldn't (for prices or for the 
        main choices)
    2 - If the cart is empty upon the user entering '2', a special message 
        will display.
    3 - I made sure that when Removing an item, that the user doesn't enter 
        a number above what is available (if there are only two items in the 
        cart, user may not enter the number 4 to remove.)
"""

#1
def addItem():
    not_num = True
    item_name = input("What is the item you would like to add? ").capitalize()
    #Check to see if what they typed is a number or not
    while(not_num):
        item_price = input(f"What is the price of '{item_name}?' $")
        try:
            item_price = float(item_price)
            not_num = False
        except ValueError:
            print("\nPlease only enter numerical values.")

    item_details = f'{item_name} - ${item_price:.2f}'

    return item_details, item_name, item_price

#2
def viewCart(cart):
    if(cart):
        print("\nThe contents of the cart are: ")
        count = 1
        for i in cart:
            print(f'{count}. {i}')
            count += 1
    else:
        print("\nThe cart is empty.")

#3
def removeItem(cart):
    not_num = True
    while(not_num):
        remove = input("Which item would you like to remove? ")
        try:
            remove = int(remove)
            if(remove > len(cart)):
                print(f"\nThat number is invalid. Please choose a number between 1 - {len(cart)}.")
            else:
                not_num = False
        except ValueError:
            print("\nPlease only enter integers.")
    return remove - 1


cart = []
cart_prices = []
keep_going = True

print("\nWelcome to the Shopping Cart Program!")
while(keep_going):
    print("\nPlease select one of the following: ")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Calculate Total")
    print("5. Quit")

    user_in = input("Please enter an action: ")
    try:
        user_in = int(user_in)

        match(user_in):
            case 1:
                item, item_name, item_price = addItem()
                cart.append(item)
                cart_prices.append(item_price)
                print(f'{item_name} added to the cart.')
            case 2:
                viewCart(cart)
            case 3:
                remove_index = removeItem(cart)
                cart.pop(remove_index)
                cart_prices.pop(remove_index)
                print("Item removed.")
            case 4:
                print(f'The total price of the items in the shopping cart is ${sum(cart_prices):.2f}')
            case 5:
                print("Thank you. Goodbye!")
                keep_going = False
            case _:
                print("Please enter a valid option")
                
    except ValueError:
        print("\nPlease only enter integers.")
    
    

