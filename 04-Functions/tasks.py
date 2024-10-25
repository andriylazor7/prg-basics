# ###
# # Calculates the area of a triangle based on the lengths
# # of the triangle's sides
# #
# import math
# def triangle_area(a,b,c):
#     p = 0.5 * (a + b + c)
#     s = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     return int(s)

# print(f'The area of ​​a triangle with sides 3,4,5 is {triangle_area(3,4,5)}')
# print(f'The area of ​​a triangle with sides 5,12,13 is {triangle_area(5,12,13)}')
# print(f'The area of ​​a triangle with sides 7,24,25 is {triangle_area(7,24,25)}')





# ###
# # Calculates the sum of the digits in a number
# #
# def sum_digits(number):
#     sum = 0
#     number = abs(number)
#     for i in str(number):
#       sum += int(i)
#     return sum

# any_number = int(input('Enter integer number: '))
# result = sum_digits(any_number)
# print(f'The sum of the digits in the number {any_number} is {result}')






# ###
# # Calculates the final grade for a test based
# # on the number of points obtained
# #
# def pts_to_grade(points):
#     grade = ''
#     if points >= 18:
#         grade = 'Excellent'
#     elif points >= 14:
#         grade = 'Good'
#     elif points >= 10:
#         grade = 'Satisfactory'
#     elif points >= 10:
#         grade = 'Fail'
#     return grade

# test_result = int(input('Enter your test result: '))
# final_grade = pts_to_grade(test_result)
# print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')







# ###
# # Function that returns the full name of a day of the week
# # based on its number
# #
# def day_name(day_number):
#     result = ''
#     if day_number == 1:
#         result = 'Monday'
#     elif day_number == 2:
#         result = 'Tuesday'
#     elif day_number == 3:
#         result = 'Wednesday'
#     elif day_number == 4:
#         result = 'Thursday'
#     elif day_number == 5:
#         result = 'Friday'
#     elif day_number == 6:
#         result = 'Saturday'
#     elif day_number == 7:
#         result = 'Sunday'
#     return result

# # Function usage
# print('The name of day 5 in the week is', day_name(5))
# print('The name of day 3 in the week is', day_name(3))
# print('The name of day 7 in the week is', day_name(7))





# def time_string(hours, minutes, time_format):
#   if time_format == 12:
#     if int(hours) >= 12 : 
#       return f'{hours}:{minutes} PM'
#     if int(hours) < 12:
#       return f'{hours}:{minutes} AM'
#   elif time_format == 24:
#     return f'{hours}:{minutes}'
#   else:
#     return 'Incorrect time format'
  
  
# time = input('Enter time (hh:mm): ')
# time_format = int(input('Enter time format (12/24): '))

# print(time_string(time[0:2], time[3:5], time_format))






# ###
# # Allows to enter and print employee data. Due to personal
# # data protection, you can determine whether information about
# # the employee's salary will be printed
# #
# import modules.keyboard

# # Reads employee's data from keyboard
# first_name = modules.keyboard.input_string('Enter name: ')
# last_name = modules.keyboard.input_string('Enter surname: ')
# age = modules.keyboard.input_integer('Enter age: ')
# salary = modules.keyboard.input_real('Enter salary: ')
# is_salary_hidden = modules.keyboard.input_boolean('Hide salary? (y/n)')

# # Prints employee's record
# print('DATA RECORD')
# print('===========')
# print(f'Name: {first_name}')
# print(f'Surname: {last_name}')
# print(f'Age: {age}')
# print(f'Salary: {salary}')
# print(f'Is salary hidden: {is_salary_hidden}')
# if is_salary_hidden == False:
#     print('Salary')
# else:
#     print('Salary is hidden')











  

      
  




