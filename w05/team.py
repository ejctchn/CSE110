numbers = []
entry = -1

while(entry != 0):
    entry = int(input("Enter number: "))
    if entry == 0:
        pass
    else:
        numbers.append(entry)

print(f'The sum of the numbers is: {sum(numbers)}')
avg = sum(numbers) / len(numbers)
print(f'The average of the list is: {avg}')

"""max = numbers[0]
for n in numbers:
    if(n > max):
        max = n
    else:
        pass

print(f'the largest number is: {max}')"""
print(min(numbers))
print(min(i for i in numbers if i > 0))