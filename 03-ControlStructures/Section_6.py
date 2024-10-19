#------------------------------------------ Section 6





# ###
# # House lighting with three bulbs and two switches
# # Checking how many bulbs are illuminating the house
# #
# light_switch1 = True # False - switch off, True - switch on
# light_switch2 = True
# bulbs_on = 0
# if light_switch1:
#     bulbs_on += 1
# if light_switch2:
#     bulbs_on += 2
#     bulbs_on += 2
# print(f'Bulbs on: {bulbs_on}')





# ###
# # Password validator
# # New password is at least 12 characters long
# #
# new_password = input('Enter new password: ')
# if len(new_password) <= 12:
#    print('Password too short (min. 12 chars)') 






# ###
# # Program that simulates the operation of an electronic thermometer.
# #
# temperature = 32

# if temperature > 35:
#     print(f"{temperature}°C: It is extremely hot.")
# elif temperature > 30:
#     print(f"{temperature}°C: It is hot.")
# elif temperature >= 15:
#     print(f"{temperature}°C: It is warm.")
# elif temperature >= 0:
#     print(f"{temperature}°C: It is cold.")
# else:
#     print(f"{temperature}°C: Warning, frost.")








# number_of_hours = int(input('Enter number of hours: '))
# price = 0

# if number_of_hours >= 1 and number_of_hours <= 2:
#   price = 5
# elif number_of_hours >= 3 and number_of_hours <= 6:
#   price = 15
# else:
#   price = 20
  
# print(f'Price for the parking: {price}')






# age = int(input('Enter your age: '))

# if age < 13:
#   print('A child')
# elif age >= 13 and age <= 19:
#   print('A teen')
# elif age >= 20 and age <= 64:
#   print('An adult')
# else:
#   print('A senior')



# ###
# # Checking if both people are adults
# #
# person1_name = input('Enter first person name: ')
# person1_age = int(input('Enter first person age: '))
# person2_name = input('Enter second person name: ')
# person2_age = int(input('Enter second person age: '))
# if person1_age >= 18 and person2_age >= 18:
#     print(f'Both {person1_name} and {person2_name} are adults')
# else:
#     print(f'Either {person1_name} or {person2_name} is not an adult')







# name = input('Enter female Polish name: ')

# if name[-1].lower() == 'a':
#   print(f'{name} -- Polish female name')
# else:
#   print(f'{name} -- Not typical Polish female name')






# human_years = float(input("Enter the dog's age in human years: "))

# if human_years <= 2:
#     dog_years = human_years * 10.5
# else:
#     dog_years = (2 * 10.5) + (human_years - 2) * 4

# print(f"The dog's age in dog's years is {dog_years:.0f} years.")









# current_product_price = 140
# previous_product_price = 200

# reduction = 100 - ((current_product_price / previous_product_price) * 100)

# if reduction >= 10:
#   print(f'Current product price: {current_product_price}')
#   print(f'Previous product price: {previous_product_price}')
#   print('Buy the product!')
#   print(f'Product price reduced by {int(reduction)} %')
# else:
#   print('Reduction is less then 10 %')







# number_of_products_purchased = int(input('Enter the number of products purchased: '))
# product_price = int(input('Enter the product price: '))

# if number_of_products_purchased <= 2:
#   amount_to_pay = number_of_products_purchased * product_price
# else:
#   discount = product_price - (product_price * 0.25)
#   discounted_products = number_of_products_purchased - 2
#   amount_to_pay = (2 * product_price) + (discounted_products * product_price * 0.75)
  
# print(f'Amount to pay: {amount_to_pay}')  







# car_speed = int(input('Enter car speed: '))
# speed_limit_min = 40
# speed_limit_max = 140

# if car_speed >= speed_limit_min and car_speed <= speed_limit_max:
#   print('Speed limit exceeded')
# else:
#   print('Warning: Invalid car speed')






# facebook = True
# twitter = False
# instagram = True

# if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):
#   print('You are a good influencer')
# else:
#   print('You are not a good influencer')







# EAN_number = input('Enter EAN-13 number: ')

# if EAN_number.isdigit() and len(EAN_number) == 13:
#   print('Article number is correct')
#   if EAN_number[0:3] == '590':
#     print('Article manufactured in Poland')
# else:
#   print('Article number is not correct')







# ###
# # Calculates and prints the total washing time.
# #
# # A washing machine allows you to wash a jacket, which takes
# # 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# # which takes 20 minutes. In addition, it is possible to program
# # an additional rinse (15 minutes) and an additional spin (9 minutes).
# #
# total_washing_time = 0
# program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')
# extra_rinse = input('Extra rinse? (y/n): ')
# extra_spin = input('Extra spin? (y/n): ')

# if program == 'j':
#   total_washing_time += 40
#   if extra_rinse == 'y':
#     total_washing_time += 15
#   if extra_spin == 'y':
#     total_washing_time += 9
# if program == 'u':
#   total_washing_time += 70
#   if extra_rinse == 'y':
#     total_washing_time += 15
#   if extra_spin == 'y':
#     total_washing_time += 9
# if program == 's':
#   total_washing_time += 20
#   if extra_rinse == 'y':
#     total_washing_time += 15
#   if extra_spin == 'y':
#     total_washing_time += 9
    

# print(f'Total washing time: {total_washing_time}')







# twenty_four_hour_format = input('Enter time (24-hour format): ')

# first_two_digits = int(twenty_four_hour_format[0:2])

# if first_two_digits < 12:
#   print(f'Time in 12-hour format: {first_two_digits}{twenty_four_hour_format[2:5]} AM')
# elif first_two_digits >= 12:
#   print(f'Time in 12-hour format: {first_two_digits - 12}{twenty_four_hour_format[2:5]} PM')










# x = int(input('Enter x: '))
# y = int(input('Enter y: '))

# if x == 0 and y == 0:
#   print(f'Point P({x},{y}) is in the center of the coordinate system')
# elif x >= 0 and y >= 0:
#   print(f'Point P({x},{y}) is in the first quadrant of the coordinate system')
# elif x >= 0 and y <= 0:
#   print(f'Point P({x},{y}) is in the fourth quadrant of the coordinate system')
# elif x <= 0 and y <= 0:
#   print(f'Point P({x},{y}) is in the third quadrant of the coordinate system')
# elif x <= 0 and y >= 0:
#   print(f'Point P({x},{y}) is in the second quadrant of the coordinate system')













# first_question = input('Are you interested in computer science? (y/n): ')
# second_question = input('Do you like playing computer games? (y/n): ')
# third_question = input('Do you have an Instagram account? (y/n): ')

# if first_question == 'y':
#   first_question = 'Yes'
# if first_question == 'n':
#   first_question = 'No'
# if second_question == 'y':
#   second_question = 'Yes'
# if second_question == 'n':
#   second_question = 'No'
# if third_question == 'y':
#   third_question = 'Yes'
# if third_question == 'n':
#   third_question = 'No'

# print(f'Interested in computer science: {first_question}')
# print(f'Playing computer games: {second_question}')
# print(f'Has an Instagram account: {third_question}')









# decimal_number = int(input("Enter decimal number: "))

# original_decimal_number = decimal_number

# binary_number = ""
# while decimal_number > 0:
#     remainder = decimal_number % 2
#     binary_number = str(remainder) + binary_number 
#     decimal_number //= 2  

# print(f"{original_decimal_number}(10) = {binary_number}(2)")












# amount = int(input("Enter the amount in PLN: "))

# five_pln_coins = 0
# two_pln_coins = 0
# one_pln_coins = 0

# five_pln_coins = amount // 5
# amount %= 5 

# two_pln_coins = amount // 2
# amount %= 2 

# one_pln_coins = amount

# print(f"The amount of PLN {sum([five_pln_coins * 5, two_pln_coins * 2, one_pln_coins])} in coins:")
# print(f"5 PLN coins: {five_pln_coins}")
# print(f"2 PLN coins: {two_pln_coins}")
# print(f"1 PLN coins: {one_pln_coins}")









# for i in range(1,31):
#   if i % 3 == 0:
#     print('Three')   
#   elif i % 5 == 0:
#     print('Five')
#   elif i % 3 == 0 and i % 5 == 0:
#     print('Bingo')
#   else:
#     print(i)







# number = int(input('Enter number: '))

# for i in range(1,11):
#   print(f'{number} x {i} = {number * i}')





# for i in range(1,6):
#   print('*' * i)
# for i in range(4, 0, -1):
#   print('*' * i)





# for i in range(1,10):
#   print(str(i) * i)









# correct_PIN = '0805'
# attempts = 3

# while attempts > 0:
#   pin = input('Enter the PIN code: ')
#   if pin != correct_PIN:
#     attempts -= 1
#     if attempts > 0:
#       print('Incorrect...')
#     else:
#       print('Sorry, your payment card has been blocked.')
#   else:
#     print('Correct PIN. Access granted.')
#     break










# for i in range(6,-1,-3):
#     for j in range(1,4):
#         print(f'{i+j}',end=' ')
#     print()
    
# print()

# i = 6
# while i >= 0:
#   j = 1
#   while j < 4:
#     print(f'{i+j}',end=' ')
#     j += 1
#   print()
#   i -= 3
    








# n_terms = 20
# a = 0
# b = 1


# for i in range(n_terms):
#  print(a, end = ' ')
#  a,b = b, a+b






# N = int(input('Enter a value of N: '))

# for i in range(2, N + 1): 
#     is_prime = True  
#     for j in range(2, i):  
#         if i % j == 0:  
#             is_prime = False  
#             break 
#     if is_prime:  
#         print(i)








# for i in range(7):
#   for j in range(1,49,7):
#     print(j + i, end= ' ')
#   print()
    



# import random

# for i in range (21):
#   print(random.randint(5,10), end = ' ')






  



























  


  






  
  
  
  
























