people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

oldest_age = 0
oldest_name = ""
youngest_age = 200
youngest_name = ""

for person in people:
    attribute = person.split()
    if(int(attribute[1]) > oldest_age):
        oldest_age = int(attribute[1])
        oldest_name = attribute[0]
    if(int(attribute[1]) < youngest_age):
        youngest_age = int(attribute[1])
        youngest_name = attribute[0]

print(f'The oldest is: {oldest_name}, Age: {oldest_age}')
print(f'The youngest is: {youngest_name}, Age: {youngest_age}')
