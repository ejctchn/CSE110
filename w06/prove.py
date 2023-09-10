"""
    1 - I added the ability to see average life expectancy of a particular country.
"""

file = open('D:/Eli Cutchen/OneDrive - BYU-Idaho/2023 (12) Spring/cse110/w06/life-expectancy.csv', 'r')

max_life_ex = 0
max_life_country = ""
max_life_year = 0

min_life_ex = 200
min_life_country = ""
min_life_year = 0

sum_life_ex_interest_year = 0
avg_life_ex_interest_year = 0

max_life_ex_interest_year = 0
max_life_country_interest_year = ""

min_life_ex_interest_year = 200
min_life_country_interest_year = ""

sum_life_ex_interest_country = 0
avg_life_ex_interest_country = 0
count_interest_country = 0

count_lines = 0
count_years = 0

try_again = True
interest_year = input("Enter the year of interest: ")
interest_country = input("Also, enter a country of interest: ")

while(try_again):
    try:
        interest_year = int(interest_year)
        try_again = False
    except ValueError:
        print("Please only use numerical values.")


for i in file:
    if(count_lines == 0):
        count_lines += 1
    else:
        line = (i.strip()).split(",")

        country = line[0]
        code = line[1]
        year = int(line[2])
        life_ex = float(line[3])
        
        if(life_ex > max_life_ex):
            max_life_ex = life_ex
            max_life_country = country
            max_life_year = year
        if(life_ex < min_life_ex):
            min_life_ex = life_ex
            min_life_country = country
            min_life_year = year

        if(year == interest_year):
            sum_life_ex_interest_year += life_ex
            count_years += 1

            if(life_ex > max_life_ex_interest_year):
                max_life_ex_interest_year = life_ex
                max_life_country_interest_year = country
            if(life_ex < min_life_ex_interest_year):
                min_life_ex_interest_year = life_ex
                min_life_country_interest_year = country
        
        if(country == interest_country.capitalize()):
            sum_life_ex_interest_country += life_ex
            count_interest_country += 1

avg_life_ex_interest_country = sum_life_ex_interest_country / count_interest_country
avg_life_ex_interest_year = sum_life_ex_interest_year / count_years

print(f'The overall max life expectancy is: {max_life_ex} from {max_life_country} in {max_life_year}')
print(f'The overall min life expectancy is: {min_life_ex} from {min_life_country} in {min_life_year}')

print(f'\nFor the year {interest_year}:')
print(f'The average life expectancy across all countries was {avg_life_ex_interest_year:.2f}')
print(f'The max life expectancy was in {max_life_country_interest_year} with {max_life_ex_interest_year}')
print(f'The min life expectancy was in {min_life_country_interest_year} with {min_life_ex_interest_year}')

print(f'\nThe average life expectancy for {interest_country.capitalize()} is {avg_life_ex_interest_country}')


file.close()