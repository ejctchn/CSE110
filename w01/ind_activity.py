fname = input("What is your first name? ")
lname = input("What is your last name? ")
email = input("What is your email address? ")
phone = input("What is your phone number? ")
job = input("What is your job title? ")
id = input("What is your ID number? ")
hair = input("What is your hair color? ")
eyes = input("What is your eye color? ")
month = input("What month did you start? ")
train = input("Did you complete advanced training? ")

print("The ID card is: ")
print("------------------------------------")
print(f'{lname.upper()}, {fname.capitalize()}')
print(job.title())
print(f'ID: {id}')
print()
print(email.lower())
print(phone)
print()
print(f'Hair Color: {hair:<15} Eye Color: {eyes}')
print(f'Month: {month:<20} Training: {train}')
print("------------------------------------")