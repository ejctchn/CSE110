friends = []
add_friends = ""

while(add_friends != "end"):
    add_friends = input("Type the name of a friend: ")
    if(add_friends == "end"):
        pass
    else:
        friends.append(add_friends)

print("\nYour friends are: ")
print("\n".join(friends))