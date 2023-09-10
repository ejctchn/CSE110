# Clever Stories (Mad Libs)

# For creativity, I added a Description or Example section
# so that if you type an 'x' or '?' at any time, you will
# receive a description or example of the word Adjective,
# Verb, Noun, or Adverb.

# When someone types '?'
def getDescription(i):
    match i:
        case 0: #Adjective
            print("\nAdjective: A word or phrase naming an attribute, added to or \n \
            grammatically related to a noun to modify or describe it.\n ")
        case 1: #Noun
            print("\nNoun: A word that names something, such as a person, place, thing, or idea. \n")
        case 2: #Verb
            print("\nVerb: A word that indicates a physical action (e.g., “drive”), a mental action \n \
                  (e.g., “think”), or a state of being (e.g., “exist”) \n")
        case 3: #Adverb
            print("\nAdjective: a word or phrase that modifies or qualifies an adjective, verb, or other adverb or a word \n \
                  group, expressing a relation of place, time, circumstance, manner, cause, degree, etc. \n")
        case _:
            print("\nan error with descriptions \n")

# When someone types 'x'
def getExample(j):
    match j:
        case 0: #Adjective
            print("\nAdjective Examples: Red, Quick, Happy...\n The ->quick<- rabbit, The ->happy<- hat, etc. \n")
        case 1: #Noun
            print("\nNoun Examples: John, house, river, car, etc. \n")
        case 2: #Verb
            print("\nVerb Examples: Jumping, leaning, driving, talking, etc. \n")
        case 3: #Adverb
            print("\nAdverb Examples: Don't drive ->fast<-, Eat ->slowly<-, etc. \n")
        case _:
            print("\nan error with examples \n")

# Welcome and instructions
print()
print("Please fill out the following ->")
print("If you need a description, just type '?'.")
print("If you need an example, just type 'x'.")
print()

# declare all the variables to use in the While Statements
adj_1 = ""
ptv = ""
adv_1 = ""
adj_2 = ""
noun_1 = ""
noun_2 = ""
noun_3 = ""
adj_3 = ""
verb = ""
adv_2 = ""
ptv_2 = ""
adj_4 = ""


while(adj_1 == "" or adj_1 == '?' or adj_1.lower() == 'x'):
    adj_1 = input("Adjective: ")
    if(adj_1 == '?'):
        getDescription(0)        
    elif(adj_1.lower() == 'x'):
        getExample(0)

while(noun_1 == "" or noun_1 == '?' or noun_1.lower() == 'x'):
    noun_1 = input("Noun: ")
    if(noun_1 == '?'):
        getDescription(1)       
    elif(noun_1.lower() == 'x'):
        getExample(1)

while(ptv == "" or ptv == '?' or ptv.lower() == 'x'):
    ptv = input("Verb (Past Tense): ")
    if(ptv == '?'):
        getDescription(2)       
    elif(ptv.lower() == 'x'):
        getExample(2)

while(adv_1 == "" or adv_1 == '?' or adv_1.lower() == 'x'):
    adv_1 = input("Adverb: ")
    if(adv_1 == '?'):
        getDescription(3)       
    elif(adv_1.lower() == 'x'):
        getExample(3)

while(adj_2 == "" or adj_2 == '?' or adj_2.lower() == 'x'):
    adj_2 = input("Adjective: ")
    if(adj_2 == '?'):
        getDescription(0)        
    elif(adj_2.lower() == 'x'):
        getExample(0)

while(noun_2 == "" or noun_2 == '?' or noun_2.lower() == 'x'):
    noun_2 = input("Noun: ")
    if(noun_2 == '?'):
        getDescription(1)       
    elif(noun_2.lower() == 'x'):
        getExample(1)

while(noun_3 == "" or noun_3 == '?' or noun_3.lower() == 'x'):
    noun_3 = input("Noun: ")
    if(noun_3 == '?'):
        getDescription(1)       
    elif(noun_3.lower() == 'x'):
        getExample(1)

while(adj_3 == "" or adj_3 == '?' or adj_3.lower() == 'x'):
    adj_3 = input("Adjective: ")
    if(adj_3 == '?'):
        getDescription(0)        
    elif(adj_3.lower() == 'x'):
        getExample(0)

while(verb == "" or verb == '?' or verb.lower() == 'x'):
    verb = input("Verb: ")
    if(verb == '?'):
        getDescription(2)       
    elif(verb.lower() == 'x'):
        getExample(2)

while(adv_2 == "" or adv_2 == '?' or adv_2.lower() == 'x'):
    adv_2 = input("Adverb: ")
    if(adv_2 == '?'):
        getDescription(3)       
    elif(adv_2.lower() == 'x'):
        getExample(3)

while(ptv_2 == "" or ptv_2 == '?' or ptv_2.lower() == 'x'):
    ptv_2 = input("Verb (Past Tense): ")
    if(ptv_2 == '?'):
        getDescription(2)       
    elif(ptv_2.lower() == 'x'):
        getExample(2)

while(adj_4 == "" or adj_4 == '?' or adj_4.lower() == 'x'):
    adj_4 = input("Adjective: ")
    if(adj_4 == '?'):
        getDescription(0)        
    elif(adj_4.lower() == 'x'):
        getExample(0)

story = f'Today I went to the zoo. I saw a(n)\n \
{adj_1} {noun_1.capitalize()} jumping up and down in its tree.\n \
He {ptv} {adv_1} through the large tunnel that led to its \
{adj_2} {noun_2}. I got some peanuts and passed\n \
them through the cage to a gigantic gray {noun_3}\n \
towering above my head. Feeding that animal made\n \
me hungry. I went to get a {adj_3} scoop\n \
of ice cream. It filled my stomach. Afterwards I had to\n \
{verb} {adv_2} to catch our bus. When I got home I\n \
{ptv_2} my mom for a {adj_4} day at the zoo.'


print()
print("Your Story is: ")
print()
print(story)
print()
