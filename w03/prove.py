"""
I used while loops to make sure the user enters 
the correct input before moving on. I added a map
function that the user can call on, once they
have aquired the map. I added golbal variables to 
keep track of the 3 keys that the user needs to be
able to complete the game.

The way to complete the game is to;
Get the flashlight(in the field by the starting area),
get the rope (from the truck), get the first key from the well
(with the rope from the truck). Go to the lake and get the key
to the house. Get gas from house, burn trash pile, get second key.
Use flashlight to go to cave and get third key.

You can now go to the top right of the map (gate) and use all 
three keys to exit the map.
"""

flashlight = False
building_key = False
key_trash = False
key_well = False
key_cave = False
all_unlocked = False
rope = False
map = False
map_realized = False
gas = False
inspected_cave = False
inspected_truck = False
burned = False

def display_map():
    global map
    if(map):
        print(" ----- ----- ----- ")
        print("|     |     |     |")
        print("|Shack| Well| Gate|")
        print("|     |     |     |")
        print(" ----- ----- ----- ")
        print("|                 |")
        print("|    Open Field   |")
        print("|                 |")
        print(" ----- ----- ----- ")
        print("|     |Start|     |")
        print("|Field|     |Build|")
        print("|     |Area | ing |")
        print(" ----- ----- ----- ")
        print("|Burn |     |     |")
        print("|     |Truck|Lake |")
        print("|Pile |     |     |")
        print(" ----- ----- ----- ")
        print("      |     |      ")
        print("      |Cave |      ")
        print("      |     |      ")
        print("       -----       ")

def good_game():
    print("Good game! Thank you for playing!")
    play_again = input("\nDo you want to play again(yes/no)? ")
    if(play_again.lower() == "yes"):
        print("You wake up in the middle of a forest.")
        intro_scene()
    elif(play_again.lower() == "no"):
        print(f'\nThank you for playing {name}. Goodbye.')
    else:
        print("Please enter a valid option.")

def game_over():
    print("\nYou are dead.")
    play_again = input("\nWould you like to start again (yes/no)? ")

    if(play_again.lower() == "yes"):
        print("You wake up in the middle of a forest.")
        intro_scene()
    elif(play_again.lower() == "no"):
        print(f'\nThank you for playing {name}. Goodbye.')
    else:
        print("Please enter a valid option.")


def locked_gate():
    global all_unlocked
    global key_cave
    global key_trash
    global key_well
    global map
    count = 0

    print("\nYou come up on a chainlink fence door.") 
    print("It has three padlocks on it. Each one has their own symbol.")
    print("One has a garbage can on it") 
    print("One has a water well on it")
    print("One has a skull and bones on it.")
    print("\nAny keys you find will be automatically used on these padlocks.")
    print()

    
    if(key_trash):
        print("The Grabage Key Padlock is open.")
    if(key_well):
        print("The Well Key Padlock is open.")
    if(key_cave):
        print("The Skull and Crossbones Key Padlock is open.")
    if(key_well and key_cave and key_trash):
        all_unlocked = True
        print("\nYou unlocked all the padlocks! The door swings open.")

    if(all_unlocked):
        print("You found the exit.") 
        final_action = ""
        final_directions = ["forward", "backward"]
        
        while final_action.lower() not in final_directions:
            final_action = input("\nYou can go BACKWARD or FORWARD. ")
        if(final_action.lower() == "backward"):
            forest_opening()
        elif(final_action.lower() == "forward"):
            good_game()
        else:
            print("Please enter a valid option.")
    else:
        action = ""
        directions = ["forward", "backward"]
        while action.lower() not in directions:
            action = input("\nYou can go BACKWARD. ")
            if(action.lower() == "backward"):
                forest_opening()
            elif(action.lower() == "forward"):
                if(count == 0):
                    print("You come up on the chainlink fence door, too high to climb. There is a humming sound comming from it.")
                    print("You return back to where you were.")
                    count += 1
                elif(count == 1):
                    print("It sounds like the fence might be electrified.")
                    print("Are you sure you want to push your luck?")
                    count += 1
                elif(count == 2):
                    print("You touch the fence and ZAP!")
                    print("You wake up on your back... Not sure how much time has passed.")
                else:
                    print("Despite your better judgement, you reach forward and grab hold of the fence again.")
                    print("...")
                    game_over()
            else:
                print("Please enter a valid option.")

def inside_building():
    global flashlight
    global gas
    global map
    inspected = False
    flashlight_on = False
    print("You step inside the building. It's very dark.")
    print("There is a faint smell of gasoline.")

    directions = ["right", "left", "backward"]
    action = ""
    while action.lower() not in directions:
        action = input("\nDo you want to go BACKWARD, INSPECT, or (if you have one) use FLASHLIGHT? ")

        if(action.lower() == "inspect"):
            if(inspected == False):
                if(flashlight_on):
                    print("\nYou see a gas can in the corner.")
                    gas = True
                    print("You pick it up.")
                else:
                    print("\nIt's too dark, maybe turn the flashlight on.")
            else:
                print("\nThere is nothing else of interest here.")
        elif(action.lower() == "flashlight"):
            flashlight_on = True
            print("\nThe flashlight is on.")
        elif(action.lower() == "backward"):
            intro_scene()
        elif(action.lower() == "map"):
            if(map):
                display_map()
            else:
                print("That's a good idea... if only I had a map.")
        else:
            print("Please enter a valid option.")

def lake_area():
    global map
    inspected = False
    count = 0
    count_right = 0
    print("You come up on a big lake. You see something shiny in the water.")
    directions = ["right", "left", "backward"]
    action = ""
    while action.lower() not in directions:
        action = input("\nDo you want to go BACKWARD, LEFT, or INSPECT the object? ")

        if(action.lower() == "inspect"):
            if(inspected):
                print("\nThere is nothing else of interest here.")
            else:
                print("\nYou run your hands through the water, you feel something.")
                building_key = True
                print("You pick up a key. It has a picture of a house on it.")
        elif(action.lower() == "backward"):
            truck_area()
        elif(action.lower() == "right"):
            if(count_right == 0):
                print("You come up on the chainlink fence, too high to climb. There is a humming sound comming from it.")
                print("You return back to where you were.")
                count_right += 1
            elif(count_right == 1):
                print("It sounds like the fence might be electrified.")
                print("Are you sure you want to push your luck?")
                count_right += 1
            elif(count_right == 2):
                print("You touch the fence and ZAP!")
                print("You wake up on your back... Not sure how much time has passed.")
            else:
                print("Despite your better judgement, you reach forward and grab hold of the fence again.")
                print("...")
                game_over()
        elif(action.lower() == "forward"):
            if(count == 0):
                print("You come up on the chainlink fence door, too high to climb. There is a humming sound comming from it.")
                print("You return back to where you were.")
                count += 1
            elif(count == 1):
                print("It sounds like the fence might be electrified.")
                print("Are you sure you want to push your luck?")
                count += 1
            elif(count == 2):
                print("You touch the fence and ZAP!")
                print("You wake up on your back... Not sure how much time has passed.")
            else:
                print("Despite your better judgement, you reach forward and grab hold of the fence again.")
                print("...")
                game_over()
        elif(action.lower() == "left"):
            building_front()
        elif(action.lower() == "map"):
            if(map):
                display_map()
            else:
                print("That's a good idea... if only I had a map.")
        else:
            print("Please enter a valid option.")

def forest_opening():
    directions = ["right", "left", "backward"]
    directions2 = ["go in", "go back"]
    global map
    global map_realized
    global rope
    global key_well

    if(map_realized or map == False):
        print("In the middle of the field, there is a stone well.")
        print("To your left, there is a small shack.")
        action = ""
        while action.lower() not in directions:
            action = input("Do you want to INSPECT the well, go LEFT, RIGHT, or BACKWARD? ")

            if(action.lower() == "inspect"):
                print("There is something shiny at the bottom.")
                if(rope):
                    action2 = input("Would you like to tie the rope to the well (YES/NO) ?")
                    if(action2.lower() == "yes"):
                        key_well = True
                        print("\nYou tie the rope to the well, climb down, retrive the key, and climb back up.")
                    elif(action2.lower() == "no"):
                        pass
            elif(action.lower() == "left"):
                print("You walk up to the shack. The wooden door looks old and rotten.")
                action2 = ""
                while action2 not in directions2:
                    action2 = input("Would you like to GO IN, or GO BACK? ")
                    if(action2.lower() == "go in"):
                        mannequin_area()
                    elif(action2.lower() == "go back"):
                        pass
                    else:
                        print("Please enter a valid option.")
            elif(action.lower() == "right"):
                locked_gate()
            elif(action.lower() == "forward"):
                if(count == 0):
                    print("You come up on a chainlink fence, too high to climb. There is a humming sound comming from it.")
                    print("You return back to where you were.")
                    count += 1
                elif(count == 1):
                    print("It sounds like the fence might be electrified.")
                    print("Are you sure you want to push your luck?")
                    count += 1
                elif(count == 2):
                    print("You touch the fence and ZAP!")
                    print("You wake up on your back... Not sure how much time has passed.")
                else:
                    print("Despite your better judgement, you reach forward and grab hold of the fence again.")
                    print("...")
                    game_over()
            elif(action.lower() == "backward"):
                intro_scene()
            elif(action.lower() == "map"):
                if(map):
                    display_map()
                else:
                    print("That's a good idea... if only I had a map.")
            else:
                print("Please enter a valid option.")
    elif(map and map_realized == False):
        print("You look in your palm and you hold...")
        print("a MAP!")
        print("\n(at anytime hereafter, as long as you have a source of light like sun or a flashlight,")
        print("you can type MAP and the map will display)")
        map_realized = True
        forest_opening()

def cave_entrance():
    global map
    global flashlight
    global key_cave
    global inspected_cave
    print("\nYou are at the entrance of a dark, wet cave.")

    directions = ["inspect", "backward"]

    action = ""
    while action.lower() not in directions:
        action = input("Do you want to INSPECT the cave, or go BACKWARD? ")

        if(action.lower() == "inspect"):
            if(inspected_cave):
                print("\nNothing more of interest here.")
            else:
                if(flashlight):
                    print("\nYou see skeletons and bones littered on the floor.")
                    print("You see something shiny on the floor. You pick it up.")
                    key_cave = True
                    print("It's a key. It has a picture of a skull and crossbones.")
                    inspected_cave = True
                else:
                    print("\nIt's a little dark, maybe we need a flashlight?")
                    cave_entrance()
        elif(action.lower() == "forward"):
            if(count == 0):
                print("You come up on a chainlink fence, too high to climb. There is a humming sound comming from it.")
                print("You return back to where you were.")
                count += 1
            elif(count == 1):
                print("It sounds like the fence might be electrified.")
                print("Are you sure you want to push your luck?")
                count += 1
            elif(count == 2):
                print("You touch the fence and ZAP!")
                print("You wake up on your back... Not sure how much time has passed.")
            else:
                print("Despite your better judgement, you reach forward and grab hold of the fence again.")
                print("...")
                game_over()
        elif(action.lower() == "backward"):
            truck_area()
        elif(action.lower() == "map"):
            if(map):
                display_map()
            else:
                print("That's a good idea... if only I had a map.")
        else:
            print("Please enter a valid option.")


def mannequin_area():
    global flashlight
    global map_realized
    global map
    flashlight_on = False
    inspected = False
    print("You find yourself in the middle of a room. It's dark, but you can make out some figures in the darkness.")

    directions = ["backward"]
 
    action = ""
    while action.lower() not in directions:
        action = input("\nYou can INSPECT, go BACKWARD, or (if you have it) use FLASHLIGHT. ")

        if(action.lower() == "inspect"):
            if(flashlight):
                if(flashlight_on):
                    print("You shine your light all around the room to see many mannequines")
                    print("some sitting, some standing. They are all facing you.")
                else:
                    print("You walk closer to the figures in the dark. As you get closer,")
                    print("you notice they're mannequines. One of them seems to have an arm extended.")
                    action2 = input("You can INSPECT or LEAVE. ")
            else:
                print("You walk closer to the figures in the dark. As you get closer,")
                print("you notice they're mannequines. One of them seems to have an arm extended.")
                action2 = input("You can INSPECT or LEAVE. ")

            if(action2.lower() == "inspect"):
                if(inspected):
                    print("There is nothing else to find here.")
                else:
                    print("You feel the mannequin's arm, and feel some paper in it's hand. You pick it up.")
                    map = True
                    if(flashlight):
                        print("You shine your flashlight on it to see...")
                        print("a MAP!")
                        print("\n(at anytime hereafter, as long as you have a source of light like sun or a flashlight,")
                        print("you can type MAP and the map will display)")
                        map_realized = True
                    else:
                        print("You need to go outside to see what it is.")
                    inspected = True

        elif(action.lower() == "flashlight"):
            if(flashlight):
                flashlight_on = True
                print("The flashlight is now on.")
            else:
                print("Good idea... if only I had a flashlight")
        elif(action.lower() == "backward"):
            forest_opening()
        elif(action.lower() == "map"):
            if(map):
                if(flashlight):
                    display_map()
                else:
                    print("I don't have enough light to see it here. I need to go outside.")
            else:
                print("That's a good idea... if only I had a map.")
        else:
            print("Please enter a valid option.")

def truck_area():
    global map
    global inspected_truck
    global rope
    directions = ["right", "left", "backward", "forward"]

    print("\nYou walk through some trees and find yourself in a clearing.")
    print("There is an old beat up truck in the middle of the clearing.")
    action = ""
    while action.lower() not in directions:
        action = input("Do you want to INSPECT the truck, go LEFT, RIGHT, FORWARD, or BACKWARD? ")

        if(action.lower() == "inspect"):
            if(inspected_truck):
                print("\nThere is nothing else of interest.")
            else:
                inspected_truck = True
                directions2 = ["backward", "pick up"]
                action2 = ""
                while action2.lower() not in directions2:
                    print("\nOne of the truck's tires is flat.")
                    print("There is something in the back of the truck.")
                    action2 = input("Do you want to PICK UP the object, or go BACKWARD? ")    

                if(action2.lower() == "pick up"):
                    rope = True
                    print("\nYou picked up a rope!")
                    print("\nYou return back to where you were.")
                elif(action2.lower() == "backward"):
                    pass
                elif(action2.lower() == "map"):
                    display_map()
                else:
                    print("\nPlease enter a valid option.")
        elif(action.lower() == "left"):
            lake_area()
        elif(action.lower() == "right"):
            pile_trash()
        elif(action.lower() == "forward"):
            cave_entrance()
        elif(action.lower() == "backward"):
            intro_scene()
        elif(action.lower() == "map"):
            if(map):
                display_map()
            else:
                print("\nThat's a good idea... if only I had a map.")
        else:
            print("\nPlease enter a valid option.")

def pile_trash():
    global map
    global key_trash
    global gas
    global burned
    directions = ["right", "left", "backward"]
    directions2 = ["pick up", "leave"]

    print("\nYou find yourself standing in front of a pile of trash.")
    print("There is a strange buzzing sound coming from your left.")
    action = ""
    action2 = ""
    count = 0
    while action.lower() not in directions:
        action = input("Do you want to go LEFT, RIGHT, BACKWARD, or (if you have the items) BURN the trash? ")

        if(action.lower() == "left"):
            print()
            print("As you pass through the trees, you are blinded by a light.")
            mannequin_area()
        elif(action.lower() == "right"):
            flashlight_area()
        elif(action.lower() == "forward"):
            if(count == 0):
                print("You come up on a chainlink fence, too high to climb. There is a humming sound comming from it.")
                print("You return back to where you were.")
                count += 1
            elif(count == 1):
                print("It sounds like the fence might be electrified.")
                print("Are you sure you want to push your luck?")
                count += 1
            elif(count == 2):
                print("You touch the fence and ZAP!")
                print("You wake up on your back... Not sure how much time has passed.")
            else:
                print("Despite your better judgement, you reach forward and grab hold of the fence again.")
                print("...")
                game_over()
        elif(action.lower() == "backward"):
            truck_area()
        elif(action.lower() == "burn"):
            if(gas and burned == False):
                print("You pour the gas on top of the pile and light it")
                print("The trash pile burns.")
                print("\nAfter a while, the pile stops burning. There's something shiny in the ashes.")
                while action2.lower() not in directions2:
                    action2 = input("PICK UP or LEAVE? ")
                    if(action2.lower() == "pick up"):
                        key_trash = True
                        print("\nYou picked up a key.")
                        print("There is a picture of a trash can on it.")
            else:
                print("You don't have the right materials to burn this.")
        elif(action.lower() == "map"):
            if(map):
                display_map()
            else:
                print("That's a good idea... if only I had a map.")
        else:
            print("Please enter a valid option.")

def flashlight_area():
    global map
    global flashlight
    count = 0
    directions = ["left", "backward"]

    print("\nYou walk through some trees and kick something hard with your foot.")
    action = ""
    while action.lower() not in directions:
        action = input("Do you want to PICK UP the object, go LEFT, RIGHT, or BACKWARD? ")

        if(action.lower() == "pick up"):
            if(flashlight):
                print("There is nothing else of interest here.")
            else:
                flashlight = True
                print("You've picked up a flashlight!")
        elif(action.lower() == "left"):
            pile_trash()
        elif(action.lower() == "right"):
            if(count == 0):
                print("\nYou come up on a chainlink fence, too high to climb. There is a humming sound comming from it.")
                print("You return back to where you were.")
                count += 1
            elif(count == 1):
                print("\nIt sounds like the fence might be electrified.")
                print("Are you sure you want to push your luck?")
                count += 1
            elif(count == 2):
                print("\nYou touch the fence and ZAP!")
                print("You wake up on your back... Not sure how much time has passed.")
                count += 1
            else:
                print("\nDespite your better judgement, you reach forward and grab hold of the fence again.")
                print("...")
                game_over()
        elif(action.lower() == "forward"):
            if(count == 0):
                print("\nYou come up on a chainlink fence, too high to climb. There is a humming sound comming from it.")
                print("You return back to where you were.")
                count += 1
            elif(count == 1):
                print("\nIt sounds like the fence might be electrified.")
                print("Are you sure you want to push your luck?")
                count += 1
            elif(count == 2):
                print("\nYou touch the fence and ZAP!")
                print("You wake up on your back... Not sure how much time has passed.")
                count += 1
            else:
                print("\nDespite your better judgement, you reach forward and grab hold of the fence again.")
                print("...")
                game_over()
        elif(action.lower() == "backward"):
            intro_scene()
        elif(action.lower() == "map"):
            if(map):
                display_map()
            else:
                print("That's a good idea... if only I had a map.")
        else:
            print("Please enter a valid option.")

def building_front():
    global map
    global building_key
    directions = ["right", "left", "backward", "pick up"]

    print("\nYou come up on a big, abandoned, dark building. Looks industrial.")
    print("There appears to be an alleyway to the left of the building.")
    action = ""
    while action.lower() not in directions:
        action = input("Do you want to try to open the DOOR, go LEFT, RIGHT, or BACKWARD? ")

        if(action.lower() == "left"):
            forest_opening()
        elif(action.lower() == "right"):
            lake_area()
        elif(action.lower() == "door"):
            if(building_key):
                inside_building()
            else:
                print("The door doesn't open. It's locked.")
                print("If only I had the key.")
        elif(action.lower() == "backward"):
            intro_scene()
        elif(action.lower() == "map"):
            if(map):
                display_map()
            else:
                print("That's a good idea... if only I had a map.")
        else:
            print("Please enter a valid option.")

def intro_scene():
    global map
    directions = ["right", "left", "forward", "backward"]
    
    print("The only visible light is some sun shining")
    print("through the trees. ")
    
    action = ""
    while action.lower() not in directions:
        action = input("Do you want to go FORWARD, LEFT, RIGHT, or BACKWARD? ")

        if(action.lower() == "left"):
            building_front()
        elif(action.lower() == "right"):
            flashlight_area()
        elif(action.lower() == "forward"):
            truck_area()
        elif(action.lower() == "backward"):
            print("\nYou push through some thick shrubs and see a spacious field.")
            forest_opening()
        elif(action.lower() == "map"):
            if(map):
                display_map()
            else:
                print("That's a good idea... if only I had a map.")
        else:
            print("Please enter a valid option.")
    
if __name__ == "__main__":
    print()
    print(f"Welcome to the Adventure Game!")
    print("Available commands will always be in CAPS.")
    print()
    name = input("What is your name? ")
    print(f'Good luck {name.capitalize()}.')
    print()
    print("You wake up in the middle of a forest.")
    intro_scene()