###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

def printArr(array):
  for i in range(len(array)):
    print(array[i])
  print()

# def addSpace(arr):
#   for i in range(len(arr)):
#     arr[i] = str(arr[i]) + ' '
#   return arr

# print(arr)
# print('Number of elements', len(arr))
# print('First value', arr[0])
# print('Second value', arr[1])
# print('Last value', len(arr) - 1)
# print('Last but one value', len(arr) - 2)
# print('Sum of the first and last value', (arr[0] + len(arr) - 1))
# print('Middle value', len(arr) / 2)
# print('Value separated by spaces', addSpace(arr))






# arr = [1,2,3,4,5]

# printArr(arr)

# arr[0] -= 1

# printArr(arr)

# arr[-1] += 4

# printArr(arr)

# arr[-3] *= 2

# printArr(arr)







# ###
# # Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
# #
# def weekday(n):
#   weekdays = ["Monday", "Tuesday", "Wednesday",
#       "Thursday", "Friday", "Saturday", "Sunday"]
#   return weekdays[n-1]


# print(weekday(1))
# print(weekday(2))




# ###
# # Prints shopping list
# #
# shopping_list = [
#    "milk", "bread", "eggs", "butter", "cheese",
#    "tomatoes", "potatoes", "carrots", "onions", "garlic"
# ]
# for item in shopping_list:
#    print(item)
   







# computer_games = [
#    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
#    "League of Legends", "Valorant", "Grand Theft Auto V", 
#    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
# ]
 
# i = 0
# while i < len(computer_games):  
#   print(f"{i+1} {computer_games[i]}")
#   i += 1 
  
# print("Sorted alphabetically: ")
# print()

# computer_games.sort()

# printArr(computer_games)
 





# ###
# # Prints vehicle registration numbers from Krakow
# #
# polish_license_plates = [
#    'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
#    'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
#    'KK54985', 'LU4864U'
# ]
# counter = 1
# for car_number in polish_license_plates:
#    if car_number[:2] == 'KR' or car_number[:2] == 'KK':
#       print(counter, car_number)
#       counter += 1




    
# ###
# # Prints test statistics
# #
# test_results = [
#    False, True, False, True, True,
#    True, True, False, True, True,
#    False, True, True, True, False
# ]

# # calculates the number of test questions
# question_number = len(test_results)

# # calculates the number of correct answers
# correct_answers = 0
# for answer in test_results:
#    if answer == True:
#       correct_answers += 1

# # calculates the number of incorrect answers
# incorrect_answers = 0
# for answer in test_results:
#    if answer == False:
#       incorrect_answers += 1

# # calculates the percentage of correct answers
# correct_percentage = (correct_answers / question_number) * 100

# print('TEST STATISTICS')
# print('===============')
# print('Number of questions:', question_number)
# print('Number of correct answers:', correct_answers)
# print(f'Percentage of correct answers: {int(correct_percentage)} %')




# ###
# # The weather station report
# #
# temperatures = [
#  3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
#  4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
#  -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
# ]

# # number of mesaurements
# mesaurements = len(temperatures)

# # calculates average temperature
# temp_total = 0
# for temp in temperatures:
#    temp_total = sum(temperatures)
# avg_temp = temp_total / mesaurements

# # calculates min and max temperatures
# min_temp = min(temperatures)
# max_temp = max(temperatures)

# # calculates number of days with negative temp
# negative_temp = 0
# i = 0
# while i < len(temperatures):
#    if temperatures[i] < 0:
#       negative_temp += 1
#    i += 1 

# # prints out month report
# print('TEMPERATURE REPORT')
# print('Month: March')
# print('Number of measurements: ', mesaurements)
# print('Average temperature in the month: ', avg_temp)
# print('Minimum temperature: ', min_temp)
# print('Maximum temperature: ', max_temp)
# print('Number of days with negative temperature: ', negative_temp)






# categories = ["Food", "Transport", "Rent", "Entertainment"]
# expenses = [500, 150, 1000, 200]

# most_expensive = max(expenses)

# index = 0
# for i in range(len(expenses)):
#   if expenses[i] == most_expensive:
#     index = i
    
# print(categories[index])




# # Prices of 10 products in the computer store (in currency units)
# product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# # Number of units available for each product
# product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

# result = 0
# for i in range(len(product_prices)):
#   for j in range(len(product_quantities)):
#     result += product_prices[i] * product_quantities[j]
    
    
# print(result)  
  
  
  
  
  
  
  
  
  
# def bubbleSort(arr):
#   n = len(arr)
#   for i in range(n - 1):  
#     for j in range(n - i - 1):  
#       if arr[j] > arr[j + 1]:
#         arr[j], arr[j + 1] = arr[j + 1], arr[j]
#   return arr



# car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
# bank_transactions = [-150, -20, 300, -45, -60, 500, -120]


# car_fuel_consumption = bubbleSort(car_fuel_consumption)
# bank_transactions = bubbleSort(bank_transactions)


# print(car_fuel_consumption)
# print(bank_transactions)





# # Sort the data from lowest to highest value
# distances_traveled = [120, 150, 180, 90, 200, 175, 160]
# # Sort the data in descending order, from highest to lowest value
# daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
# # Sort the data in ascending order
# file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
#    "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]

# distances_traveled = sorted(distances_traveled)

# daily_temperatures = sorted(daily_temperatures, reverse=True)

# file_names = sorted(file_names)


# print(distances_traveled)
# print(daily_temperatures)
# print(file_names)
  
    


  



# # 3x3 Tic-Tac-Toe board
# tic_tac_toe_board = [
#    ['X', 'O', 'X'],
#    [' ', 'X', 'O'],
#    ['O', ' ', 'X']
# ]

# for row in tic_tac_toe_board:
#    for column in row:
#       print(column, end=" ")
#    print()





# # Weekly expenses for different categories
# # [Food, Transport, Utilities]
# monthly_expenses = [
#    [200, 50, 100],  # Week 1
#    [180, 60, 110],  # Week 2
#    [220, 55, 105],  # Week 3
#    [210, 65, 95]    # Week 4
# ]

# # Calculates expenses
# # Use loop statements
# food_expenses = 0
# transport_expenses = 0
# utilities_expenses = 0

# week1 = 0
# week2 = 0
# week3 = 0
# week4 = 0


# for i in monthly_expenses:
#   food_expenses += i[0]
#   transport_expenses += i[1]
#   utilities_expenses += i[2]
  

#   week1 = sum(monthly_expenses[0])
#   week2 = sum(monthly_expenses[1])
#   week3 = sum(monthly_expenses[2])
#   week4 = sum(monthly_expenses[3])
  

# # Print expenses
# print('MONTHLY EXPENSES')
# print('----------------')
# print('Food:', food_expenses)
# print('Transport:', transport_expenses)
# print('Utilities:', utilities_expenses)
# print('Week 1:', week1)
# print('Week 2:', week2)
# print('Week 3:', week3)
# print('Week 4:', week4)
# print('---------------')
# print('TOTAL:', food_expenses + transport_expenses + utilities_expenses + week1 + week2 + week3 + week4)









# # Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
# meal_plan = [
#    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
#    ["Pancakes", "Sandwich", "Steak"],
#    ["Smoothie", "Chicken Wrap", "Salmon"],
#    ["Eggs", "Pasta", "Soup"],
#    ["Toast", "Burrito", "Pizza"],
#    ["Cereal", "Salad", "Fish Tacos"],
#    ["Bagel", "Rice and Beans", "Stir-fry"]
# ]

# # Returns a week day name
# def weekday(n):
#    weekdays = ["Monday", "Tuesday", "Wednesday",
#       "Thursday", "Friday", "Saturday", "Sunday"]
#    return weekdays[n-1]

# # Returns a string with day meal names
# # separated by comma
# def day_meal_plan(meal_plan_index):
#    return f"{weekday(meal_plan_index)}: {meal_plan[meal_plan_index]}"

# # Prints weekly meal plan
# for i in range(7):
#   print(day_meal_plan(i))







# # 5x5 cinema seating
# # A = Available, B = Booked
# cinema_seats = [
#    ['A', 'A', 'B', 'A', 'A'],
#    ['A', 'B', 'B', 'A', 'A'],
#    ['A', 'A', 'A', 'A', 'B'],
#    ['B', 'A', 'A', 'A', 'A'],
#    ['A', 'B', 'A', 'A', 'A']
# ]

# def seats_total(seats):
#   total = 0
#   for i in seats:
#     total += len(i)
#   return total

# def seats_available(seats):
#   count = 0
#   for i in range(len(seats)):
#     for j in range(len(seats)):
#       if seats[i][j] == 'A':
#         count += 1
#   return count

# def seats_booked(seats):
#   count = 0
#   for i in range(len(seats)):
#     for j in range(len(seats)):
#       if seats[i][j] == 'B':
#         count += 1
#   return count

# def seat_status(seats, row, place):
#   if seats[row - 1][place - 1] == 'A':
#     return "Available"
#   if seats[row - 1][place - 1] == 'B':
#     return "Booked"

# print('CINEMA INFORMATION TABLE')
# print('Total seats:', seats_total(cinema_seats))
# print('Seats available:', seats_available(cinema_seats))
# print('Seats booked:', seats_booked(cinema_seats))
# print('Seat in row 1, place 1:', seat_status(cinema_seats, 1,1))
# print('Seat in row 5, place 5:', seat_status(cinema_seats, 5,5))
# print('Seat in row 3, place 5:', seat_status(cinema_seats, 3,5))





# square_matrix = [
#    [0,0,0],
#    [0,0,0],
#    [0,0,0]
# ]

# print(square_matrix)

# for i in range(len(square_matrix)):
#   square_matrix[i][i] = 1

# print(square_matrix)






    



