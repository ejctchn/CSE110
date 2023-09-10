shopping_list = []
entry = ""


print("\nPlease enter the items of the shopping list (type 'quit' to finish)")

while(entry != "quit"):
    entry = input("Item: ")
    if entry == "quit":
        pass
    else:
        shopping_list.append(entry)

counter = 0
print("\nThe shopping list with index is:")
for i in shopping_list:
    print(f'{counter}. {i}')
    counter += 1

correction = int(input("What item would you like to change? "))
new_item = input("What is the new item? ")

shopping_list[correction] = new_item

counter = 0
print("\nThe shopping list with index is:")
for i in shopping_list:
    print(f'{counter}. {i}')
    counter += 1