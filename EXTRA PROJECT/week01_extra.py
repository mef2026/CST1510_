#%%

name = input('Name: ')
hobby = input('Hobby: ')
nationality = input('Nationality: ')
course = input('Course: ')
experience = input('Programming experience: ')
age = input('Age:')
print(f'User Information:\n\tName: {name}\n\tHobby: {hobby}'
      f'\n\tNationality: {nationality}\n\tCourse: {course}'
      f'\n\tExperience: {experience} \n\tAge:{age}')



#%%

width = 4.5
height = 7.9
area = width * height
perimeter = 2 * (width + height)


print(f'Area = {area:.2f}')

print(f'Perimeter = {perimeter:.2f}')

# %%

pounds = float(input('Weight in pounds: '))
kilograms = pounds * 0.454
print(f'{pounds} pounds is {kilograms} kilograms')


# %%
feet = float(input('Length in feet: '))
metres = feet * 0.305
print(f'{feet} feet is {metres} meters')

# %%
season_1_seconds = 45 * 60 + 35
other_season_seconds = 35 * 60 + 15
total_seconds = 10 * season_1_seconds + 40 * other_season_seconds
hours, remainder = divmod(total_seconds, 3600)
minutes, seconds = divmod(remainder, 60)
print(f'Total time: {hours}h {minutes}m {seconds}s')

# %%
weeks = 3 * 52
savings = 0.0
savings += 10 * weeks
savings += 20 * 52
savings -= 0.50 * (weeks // 2)
print(f'Final savings after 3 years: £{savings:.2f}')

#%%

population = 312032486
seconds_per_year = 365 * 24 * 60 * 60
annual_change = (seconds_per_year // 7
                 - seconds_per_year // 13
                 + seconds_per_year // 45)
for year in range(1, 6):
    population += annual_change
    print(f'Year {year}: {population:,}')


# %%
ip = input('IP: ')
method = input('Method: ').upper()
path = input('Path: ')
status = int(input('HTTP status: '))
byte_count = int(input('Bytes: '))
print(f'{ip} - "{method} {path}" {status} {byte_count}')

# %%
