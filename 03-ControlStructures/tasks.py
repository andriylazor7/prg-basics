#------------------------------------------ Section 1


# ###
# # Checking whether a car exceeded the speed limit
# #
# speed_limit = 140
# car_speed = int( input('Enter car speed (km/h): ') )

# if car_speed <=140:
#     print(f'Your speed is {car_speed} km/h')
# else:
#     print('Warning: speed limit exceeded!!')





# ###
# # Credit card payment 
# #
# account_balance = 500
# total_payment = float(input("Enter total payment: "))

# if total_payment <= account_balance:
#     print('Payment completed!')
# else:
#     print('No funds')





# ###
# # Checking whether the test is passed
# # Test is passed when the number of correctly completed
# # tasks is at least 50%
# #
# total_tasks = 20
# tasks_ok = int(input("Enter a number correct tasks: "))
# test_passed = False

# if tasks_ok >= total_tasks/2:
#     test_passed = True
    
# if test_passed:
#     print('Congratulations! You passed the test.')
# else:
#     print('Unfortunately, you failed the test.')






# ###
# # Checking whether the number
# # entered from the keyboard is even or odd 
# #
# number = int(input('Enter number: '))

# if number % 2 == 0:
#     print(f'{number} is even')
# else:
#     print(f'{number} is odd')




# ###
# # Program that calculates the employee's salary,
# # taking into account the possibility of receiving a bonus.
# #
# basic_salary = 4000
# total_salary = 0
# is_bonus = True # does the employee receive a bonus
# bonus = 0.15 # 15%

# if basic_salary <=5000:
#     total_salary = (basic_salary * bonus) + basic_salary
# else:
#     total_salary = basic_salary
#     is_bonus = False

# print(f'Basic salary: {basic_salary}')
# print(f'Bonus included? {is_bonus}')
# print(f'Total salary: {total_salary}')







#------------------------------------------ Section 2




# ###
# # A program for checking clothing sizes
# # S: Small size, M: Medium size, L: Large size
# # XL: Extra large size or Incorrect symbol (if entered symbol
# # dirrerent than S, M, L, XL)
# #
# size = input('Enter size symbol: ')

# if size == 'S' or size == 's':
#     print('S: Small size')
# elif size == 'M' or size == 'm':
#     print('M: Medium size')
# elif size == 'L' or size == 'l':
#     print('L: Large size')
# elif size == 'XL' or size == 'xl':
#     print('XL: X-Large size')
# else:
#   print("Not a size")











# ###
# # The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# # In each of these three modes, the average fuel consumption in liters
# # per 100 km is 7, 9 and 6 respectively. Write a program that calculates
# # total fuel consumption for a given distance in km and a given
# # driving mode.
# #
# driving_mode = input('Enter driving mode (A/M/E): ')
# distance = int(input('Enter distance in km: '))

# if driving_mode == 'A':
#     fuel_consumption = 7 # liters per 100km
# elif driving_mode == 'M':
#     fuel_consumption = 9 # liters per 100km
# elif driving_mode == 'E':
#     fuel_consumption = 6 # liters per 100km
# ...

# total_consumption = int(fuel_consumption * distance / 100)
# print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')



# ###
# # Simple calculator
# # Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# # and two numbers. The program should perform the appropriate
# # mathematical operation on the given numbers and return the result.   
# # 
# result = 0
# number1 = int(input('Enter the first number: '))
# number2 = int(input('Enter the second number: '))
# operator = input('Enter an operator (+, -, *, /): ')

# if operator == '+':
#   result = number1 + number2
# elif operator == '-':
#   result = number1 - number2
# elif operator == '*':
#   result = number1 * number2
# elif operator == '/':
#   result = number1 / number2
# else:
#   print('Not an operator!')
  
  
# print(f'Result: {result}')





# ###
# # Calculates and prints the quarter of the year for a given
# # month number (1..12)
# #
# month = int(input('Enter month number (1..12): '))

# if month >= 10:
#     quarter = 4
# elif month >= 7:
#     quarter = 3
# elif month >= 4:
#     quarter = 2
# else:
#     quarter = 1

# print(f'Month {month} is in quarter {quarter}')







# number = int(input('Enter a number: '))

# if number ==0:
#   print('Number is 0')
# if number > 0:
#   print(f'Number {number} is positive')
# if number < 0:
#   print(f'Number {number} is negative')




#------------------------------------------ Section 3



# ###
# # Checking login and password
# #
# login = 'joe'
# password = 'abcd'
# entered_login = input('Login: ')
# entered_password = input('Password: ')
# if login == entered_login and password == entered_password:
#     print('You are logged in')
# else:
#     print('Incorrect login or password!!')






# ###
# # Checking if discount is available
# # The discount is available to children under 18,
# # or people 65 or older.
# #
# age = int(input('Enter your age: '))

# if age < 18 or age >= 65 :
#     print('Discount is available')
# else:
#     print('Discount is not available')






# ###
# # Checks whether at least one number entered
# # from the keyboard is not negative
# # 
# x = int(input('Enter first number: '))
# y = int(input('Enter second number: '))

# if not x < 0 or not y < 0:
#     print(f'At least one of the numbers {x} and {y} is not negative')
# else:
#     print(f'Both numbers {x} and {y} are negative')





# ###
# # Calculates the number of days in a month
# #
# month = int(input('Enter month number (1..12)'))

# if month==1 or month==3 or month==5 or month==7 or month == 8 or month==10 or month==12:
#     days = 31 ## months with 31 days
# elif month == 2:
#     days = 28 ## months with 30 days
# else:
#     days = 30

# print(f'Month {month} has {days} days')






# ###
# # Checks if the given day number of the month is correct
# #
# month = int(input('Enter month number (1..12): '))
# day = int(input('Enter the day number of the month: '))
# day_ok = False

# if month==1 or month==3 or month==5 or month==7 or month == 8 or month==10 or month==12:
#   if day >=1 and day <= 31:
#     day_ok = True
# elif month == 2:
#   if day >=1 and day <= 28:
#     day_ok = True
# else:
#   if day >=1 and day <= 30:
#     day_ok = True

# message = f'Day {day} for the month {month}'
# if day_ok:
#     print(f'{message} is correct')
# else:
#     print(f'{message} is incorrect')

























  
  










    







