
#Grade Calculator
"""
#A >= 90
#B >= 80
#C >= 70
#D >= 60
#F < 60
"""

#core requirements
grade = int(input("\nWhat is your grade percentage? "))
letter_grade = ""
print()

if(grade >= 90):
    letter_grade = "A"
elif(grade >= 80):
    letter_grade = "B"
elif(grade >= 70):
    letter_grade = "C"
elif(grade >= 60):
    letter_grade = "D"
else:
    letter_grade = "F"

#Stretch Challenges 
if(grade % 10 >= 7):
    if(grade < 90 and grade > 60):
        letter_grade += "+"
    else:
        pass
elif(grade % 10 <= 3):
    if(grade > 50):
        letter_grade += "-"
    else:
        pass
else:
    pass

print(f'Your letter grade is: {letter_grade}')

if(grade >= 70):
    print("You did it! YAY!")
else:
    print("Oof... Better luck next time...")
    
print()

