# ###
# # A program that calculates the sum of two numbers.
# # Modify the program to calculate the sum of three numbers.
# #
# number1 = 71
# number2 = 14
# number3 = 3
# result = number1 + number2 + number3
# print('Number 1: ', number1)
# print('Number 2: ', number2)
# print('Number 3: ', number3)
# print('The result of summation: ', result)


# ###
# # A program for swapping two varable values
# #
# x = 7
# y = 34
# z = 0 # additional, auxiliary variable
# print("Before swapping: x=", x, "y=", y)

# # swap the values
# z=x
# x=y
# y=z


# print("After swapping: x=", x, "y=", y)




# ###
# # A program that, for a given speed in km/h,
# # prints the speed in m/s
# #
# speed_kmh = 70
# speed_ms = speed_kmh * 0.621371
# print(speed_kmh, "km/h = ", speed_ms, "m/s")



# ###
# # A program that calculates the length of the diagonal
# # of a rectangle with sides a and b.
# #
# import math
# a = 5
# b = 3
# diagonal = math.sqrt(a**2 + b**2)
# print(diagonal)



# # d = 3.57 × √h

# import math
# height = 20
# result = 3.57 * math.sqrt(height / 1000)
# print(result)

# ----i
# height1 = 1.76
# result1 = 3.57 * math.sqrt(height1 / 1000)

# print(result1)

# height2 = 1.76 + 20
# result2 = 3.57 * math.sqrt(height2 / 1000)

# print(result2)




# ###
# # A program that calculates and prints:
# # - the number of people and percentage of the total
# #   population living in the Northern Hemisphere
# # - the number of people and percentage of the total
# #   population living in the Southern Hemisphere
# #
# total = 8000000000
# north = 7200000000
# south = total - north
# print("World population: ", total)
# print("Northern Hemisphere population: ", north)
# print("Northern Hemisphere in %: ", (north / total) * 100)
# print("Southern Hemisphere population: ", south)
# print("Southern Hemisphere in %: ", (south / total) * 100)




# ###
# # A program that calculates and prints
# # the average grade of a student
# #
# Math = 5
# art = 4
# music = 5
# history = 3
# average = (Math + art + music + history) / 4
# print("Average grade is", average)






# ###
# # Printing student's personal data
# #
# name = "Adam"
# age = 18
# height = 180
# print(f"My name is {name}.")
# print(f"I am {age} years old, and my height is {height} cm.")
# print(f"In 6 years I will be {age + 6}.")



# ###
# # Write a program that calculates and prints
# # the income of a family per person. To print the results
# # in a readable form, use f-strings.
# #
# father_income = 5450
# mother_income = 4920
# family_members = 5
# total_income = father_income + mother_income
# income_per_person = total_income / 5
# print(f'Total family income is {income_per_person}, and income per person is ...')




# a = 3
# b = 5
# print(f'{a}+{b} = {a+b}')
# print(f'{a}-{b} = {a-b}')
# print(f'{a}*{b} = {a*b}')
# print(f'{a}/{b} = {a/b}')





# # A program that reads your first and last name from the keyboard.
# # Store this data in two separate variables.
# # Then, print your full name i.e. first and last name separated by a single space.
# first_name = input('Enter your first name: ')
# last_name = input('Enter your last name: ')
# full_name = first_name + ' ' + last_name
# print(f'Your first name is {first_name} and your last name is {last_name}')
# print(f'And your full name is {full_name}')



# ###
# # A program to calculate the volume and surface area of ​​a cube.
# # 
# cube_side_string = input('Enter cube side: ')
# cube_side = int(cube_side_string)
# cube_volume = cube_side**3
# cube_surface_area = 6*cube_side**2
# print(f'The volume of a cube with side {cube_side} is {cube_volume}')
# print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')




# ###
# # A program that calculates the volume
# # and surface area of ​​a cuboid with sides a, b, and c.
# # Read the dimensions of the cuboid from the keyboard.
# #
# a = int(input('a='))
# b = int(input('b='))
# c = int(input('c='))

# volume = a * b * c
# surface_area = 2 * ((a*b) + (a*c) + (b*c))

# print(f"Volume: {volume}")
# print(f"Surface area: {surface_area}")





# amount = float(input('Enter amount: '))

# print(f"Amount: {amount}")
# print(f"VAT 23%: {amount * 0.23}")






# start_price = float(input("Enter price: "))
# discount = int(input("Enter discount: "))

# price_with_discount = start_price - (start_price * (discount / 100))


# print(f"Product price: {start_price}")
# print(f"Discount: {discount}")
# print(f"Price with discount: {price_with_discount}")
# print(f"Reduction: {start_price - price_with_discount}")






# ###
# # A program that calculates the number of characters
# # of your name, surname and full name
# #
# name = 'Andriy'   # replace Anna with your name
# surname = 'Lazor' # replace May with your surname
# characters_in_name = len(name)
# characters_in_surname = len(surname)
# print(f'Your name has {characters_in_name} characters')
# print(f'Your surname has {characters_in_surname} characters')
# print(f'Your full name has {characters_in_name + characters_in_surname}') 





# ###
# # A program that prints your initials
# #
# name = 'Andriy'
# surname = 'Lazor'

# print(f"Name: {name}")
# print(f"Surname: {surname}")
# print(f"Initials: {name[0] + surname[0]}")



# ###
# # A program that prints a university abbreviation
# #   
# university = "Krakow University of Economics"

# print(f"University name: {university}")
# print(f"Abbreviation: {university[0] + university[7] + university[21]}")





# ###
# # A program for printing detailed information.
# #
# employee = "Mr. John May, born on 1998-02-16"
# print(f'Name: {employee[4:8]}')
# print(f'Surname: {employee[9:12]}')
# print(f'Born: {employee[22:32]}')
# print(f'Initials: {employee[4] + employee[9]}')




# ###
# # a program that prints a 9-digit telephone number
# # entered from the keyboard as three groups of 3 digits each,
# # separated by a dash character.
# #
# phone = input('Enter phone number: ')
# print(phone[0:3] + '-' + phone[3:6] + '-' + phone[6:9])





# ###
# # A program to print numerical representations of characters.
# #
# print(f'a {ord('a')}')
# print(f'b {ord('b')}')
# print(f'z {ord('z')}')
# print(f'A {ord('A')}')
# print(f'B {ord('B')}')
# print(f'Z {ord('Z')}')
# print(f'1 {ord('1')}')
# print(f'= {ord('=')}')
# print(f'+ {ord('+')}')
# print(f'€ {ord('€')}')




# ###
# # A program that prints a numerical representation of each letter of your name.
# #
# name = 'Andriy' # replace John with your name
# print(f'The letter {name[0]} has a code {ord(name[0])}')
# print(f'The letter {name[1]} has a code {ord(name[1])}')
# print(f'The letter {name[2]} has a code {ord(name[2])}')
# print(f'The letter {name[3]} has a code {ord(name[3])}')
# print(f'The letter {name[4]} has a code {ord(name[4])}')
# print(f'The letter {name[5]} has a code {ord(name[5])}')







# ###
# # A program that calculates
# # how many letters are between two given letters
# #
# first = input('Enter first letter: ')
# last = input('Enter last letter: ')
# first_letter_code = ord(first)
# last_letter_code = ord(last)

# print(first_letter_code)
# print(last_letter_code)
# number_of_letters = last_letter_code - first_letter_code
# print(f'Between {first} and {last} is {number_of_letters} letters')




# ###
# # Character code conversion
# #
# print(chr(67),chr(111), chr(111),chr(108),chr(33))




# ###
# # String manipulation
# #

# movie = "The Lord of the Rings: The Return of the King"

# # print number of characters
# print('Number of characters: ', len(movie))

# # print title in capital letters
# print(movie.upper())

# # print title in small letters
# print(movie.lower())

# # print how many times the vowel "e" appears in the title
# print(f"Count of the vowel 'e': {movie.count('e')}")

# # print where in the text is the word "Lord"
# print(movie.rfind('Lord'))

# # print where in the text is the word "dragon"
# print(movie.rfind('Dragon'))






# ###
# # People up to and including 26 years of age are exempt
# # from paying taxes in Poland. Write a program that,
# # based on the person's age entered from the keyboard,
# # prints True if the person is exempt from paying taxes
# # and prints False otherwise.
# #
# age = int(input('Enter age: '))
# no_tax = age <= 26
# print(f'Exemption from paying taxes: {no_tax}')





# ###
# # A program that checks whether the password length
# # read from the keyboard is correct.
# #
# password = input('Enter password: ')
# password_ok = len(password) >= 8
# print(f'Password length is valid: {password_ok}')







# ###
# # A program that checks whether the number entered
# # from the keyboard is even.
# # A number is even if the remainder when divided by 2 is 0.
# # What operator do you need to use to calculate
# # the remainder of division?
# #

# number = int(input('Enter number: '))
# even = number % 2 == 0
# print(f'Number is even: {even}')









# circumference = int(input('Enter the tree circumference: '))
# cut = circumference >= 50
# print(f'Tree can be cut down: {cut}')








# ###
# # Vehicle registration numbers in Krakow start
# # with the letters KR or KK. Write a program that checks
# # whether the vehicle registration number entered
# # from the keyboard means a vehicle from Krakow.
# # Print True whether a car is from Krakow or False otherwise.
# #
# car_number = input('Enter car registration number: ')
# is_krakow = car_number[0:2] == "KR" or car_number[0:2] == "KK"
# print(f'Car is from Krakow: {is_krakow}')







# speed = int(input("Enter vehicle speed: "))
# is_allowed = 40 < speed < 140
# print(f"Speed is valid: {is_allowed}")







# import random
# random_number = random.randint(5,10)
# print(random_number)



# ###
# # A program that prints results of three dice rolls
# # and the sum of dice rolled.
# #
# import random
# dice_roll_1 = random.randint(1,6)
# dice_roll_2 = random.randint(1,6)
# dice_roll_3 = random.randint(1,6)

# print(f"First dice roll: {dice_roll_1}")
# print(f"Second dice roll: {dice_roll_2}")
# print(f"Third dice roll: {dice_roll_3}")
# total = dice_roll_1 + dice_roll_2 + dice_roll_3
# print(total)




# import random

# dice_rolled = random.randint(1,6)
# is_special = dice_rolled == 1 or dice_rolled == 6

# print(f"Number: {dice_rolled}")
# print(f"Special number (1 or 6) : {is_special}")








# ###
# # A program that enables a user to challenge a computer.
# # The computer throws dice. Then, the user then tries to guess
# # the number from dice by entering a number from 1 to 6
# # from the keyboard. If the user has guessed the number
# # from the dice, the computer prints True. Otherwise,
# # the computer prints False.
# #
# import random
# computer = random.randint(1,6)
# you = int(input('Enter your number: '))

# is_equal = computer == you
# print(f'You won: {is_equal}')







# radius = int(input('Enter radius of a circle: '))
# PI = 3.14

# print(f"Area: {PI*radius**2}")
# print(f"Circumference : {2*PI*radius}")






# temperature = int(input("Enter temperature: "))

# print(f"Temperature in Kelvin: {temperature + 273.15}") # Converting temperature to Kelvin
# print(f"Temperature in Fahrenheit: {temperature * 9/5 + 32}") # Converting temperature to Fahrenheit




# ###
# # A program that prints your height both in cm and in feet and inches.
# #
# cm = 170
# feet = cm //30.48
# remaining_cm = cm % 30.48

# inches = remaining_cm // 2.54
# remaining_inches = remaining_cm % 2.54

# print(f'I am {cm} cm tall, i.e. {int(feet)} feet and {int(inches)} inches')








# ###
# # A program that reads a SWIFT code from the keyboard
# # and prints the bank code and country code.
# #
# swift = input('Enter SWIFT code: ')

# bank_code = swift[:4]
# country_code = swift[4:6]


# print(f'Bank Code: {bank_code}')
# print(f'Country Code: {country_code}')













# ###
# # The program calculates the cost of transporting goods
# # based on the given distance in km, fuel price per 1 liter,
# # and fuel consumption in liters per 100 km.
# #
# distance = int(input('Enter distance in km: '))
# fuel_price = float(input('Enter fuel price per liter: '))
# fuel_consumption = float(input('Enter fuel consumption: '))
# total_fuel_consumption = (distance / 100) * fuel_consumption
# total_cost = total_fuel_consumption * fuel_price

# print(f'Total fuel consumption: {total_fuel_consumption} liters')
# print(f'Total cost of transportation: {total_cost} currency units')








# number = int(input('Enter number: '))

# print(f'Binary number: {bin(number)}')
# print(f'Hexadecimal number: {hex(number)}')














































































































































