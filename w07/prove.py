"""
    1 - I added a frostbite estimator. It gives a rough
        guess about how long it would take for you to 
        get frostbite, at the given temperature. 
"""

# how long would it take to get frostbite?
def frostbite(temp, windc):
    frost_time = "30+"
    if(temp <= 10 and temp > 0):
        if(windc <= -18 and windc > 32):
            frost_time = 30
    elif(temp <= 0 and temp > -15):
        if(windc <= -19 and windc > -32):
            frost_time = 30
        elif(windc <= -32 and windc > -50):
            frost_time = 15
    elif(temp <= -15):
        if(windc <= -50):
            frost_time = 5
    
    return frost_time
        

# calculate windchill
def windchill(winds, temp):
    windc = 35.74 + (0.6215 * temp) - 35.75 * (winds ** 0.16) + 0.4275 * temp *(winds ** 0.16)
    return windc

# if the user enters C then you need to convert temp to F - EC
def convert_to_f(temp):
    converted = temp * (9/5) + 32
    return converted

def display(temp, need_to_convert):
    if(need_to_convert):
        temp = convert_to_f(temp)

    # display the results
    winds = 5
    while(winds <= 60):
        windc = windchill(winds, temp)
        frost_time = frostbite(temp, windc)
        print(f'\nAt temperature {temp}F, and wind speed {winds} mph, the windchill is: {windc:.2f}F. \nIt would take about {frost_time} minutes to get frostbite.')
        winds += 5


# declare all bools and global variables - EC
check_temp = True
check_f_c = True
need_to_convert = False
temp = 0

# make sure user enters number - EC
while(check_temp):
    try:
        temp = int(input("What is the temperature? "))
        check_temp = False
    except ValueError:
        print("\nPlease only enter a numeric value.")

# make sure the user enters only F or C
while(check_f_c):
    f_c = input("Fahrenheit or Celsius (F/C)? ")
    if(f_c.capitalize() == "F"):
        check_f_c = False
    elif(f_c.capitalize() == "C"):
        need_to_convert = True
        check_f_c = False
    else:
        print("Please enter F or C")

# call the display function
display(temp, need_to_convert)


