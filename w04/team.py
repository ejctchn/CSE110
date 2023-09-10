import random
options = ["yes", "no"]
keep_playing = True


while(keep_playing):
    magic_num = random.randint(1, 100)
    number = int(input("Guess the Number: "))
    count = 1
    keep_going = ""

    while(number != magic_num):
        if(number < magic_num):
            print("Higher. Try again.")
            number = int(input("Guess the Number: "))
            count += 1
        elif(number > magic_num):
            print("Lower. Try again.")
            number = int(input("Guess the Number: "))
            count += 1
        else:
            pass
    print("You got it!")
    print(f'It took you {count} tries!')

    while(keep_going not in options):
        keep_going = input("Do you want to keep playing (yes/no)? ")
        if(keep_going.lower() == "yes"):
            pass
        elif(keep_going.lower() == "no"):
            keep_playing = False
        else:
            print("That is not a valid option.")