def display_regular(text):
    print(f"The regular text is: {text}")
def display_upper(text):
    print(f"The uppercase text is: {text.upper()}")
def display_lower(text):
    print(f"The lowercase text is: {text.lower()}")

text = input("What is your message? ")

display_regular(text)
display_upper(text)
display_lower(text)