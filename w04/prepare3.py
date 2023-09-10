word = "commitment"
fav_letter = input("What is your favorite letter? ")

for i in word:
    if(i == fav_letter.lower()):
        print("_", end="")
    else:
        print(i, end="")