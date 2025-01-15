# ###
# # Calculates arithmetic mean of two integer numbers
# #
# def mean(x,y):
#    return (x+y)/2

# # takes two numbers from keyboard
# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))

# # calculates arightmtic mean and print result
# result = mean(n1,n2)
# print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')






# # takes two numbers from keyboard
# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))

# # define an anonymous function
# mean = lambda x,y: (x+y)/2


# # calculates arightmtic mean and print result
# result = mean(n1,n2)
# print(f"The arithmetic mean of {n1} and {n2} is {result}")




# def ms_to_kmh(ms):
#   return ms * 3.6


# ms = float(input("Enter meters per second (m/s): "))

# print("Kilometers per hour: ", ms_to_kmh(ms))






# ms = float(input("Enter meters per second (m/s): "))

# ms_to_kmh = lambda ms: ms*3.6

# print("Kilometers per hour: ", ms_to_kmh(ms))








# def avg_speed(distance, hours, minutes):
#   total_time_hours = hours + (minutes / 60)
  
#   average_speed = distance / total_time_hours
#   return average_speed



# distance = int(input("Enter distance in km: "))
# hours = int(input("Enter number of travel hours: "))
# minutes = int(input("Enter number of travel minutes: "))
# print("Average speed: ", avg_speed(distance, hours, minutes))








# distance = int(input("Enter distance in km: "))
# hours = int(input("Enter number of travel hours: "))
# minutes = int(input("Enter number of travel minutes: "))

# avg_speed = lambda distance, hours, minutes: distance / (hours + (minutes / 60))



# print("Average speed: ", avg_speed(distance, hours, minutes))








# number = int(input("Enter a number: "))

# is_even = lambda number: number % 2 == 0

# if is_even(number):
#   print(f"The {number} is even")
# else:
#   print("The number is not even")





# name = input("Enter name: ")
# surname = input("Enter surname: ")

# initials = lambda name, surname: f"{name[0]}{surname[0]}"

# print("Initials:", initials(name, surname))









# names = [
#    'James',
#    'Emily',
#    'William',
#    'Olivia',
#    'Benjamin',
#    'Sophia',
#    'Henry']



# names = sorted(names, key=lambda name: len(name))

# print(names)






# transactions_in_eur = [15.90,38.47,4.07,132.70,9.15]
# transactions_in_pln = list(map(lambda x:x*4.5, transactions_in_eur))

# for i in transactions_in_pln:
#   print(i)




# text = "I completely agree with you"

# words = text.split()

# letter_counts = list(map(lambda word: len(word), words))

# print("Text:", text)

# print("No. of letters in words: ", letter_counts)






# stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]

# sum_arr = list(map(lambda product: product[0] * product[1], stock))

# print("Products in stock:", stock)
# print("Total value: ", sum(sum_arr))







# employees = ["SMITH Lucy", "JONES Janet", "LEE Jerry", "JACKSON Peter", "JOHNSON Rick", "LEWIS Terry", "CLARKE Robin"]

# filtered_array = list(filter(lambda surname: surname[0] == "J", employees))

# print(filtered_array)





# speeds = [48, 47, 54, 50, 42, 68, 39, 46]

# exceeded_speeds = list(filter(lambda speed: speed > 50, speeds))

# print(exceeded_speeds)





import statistics

grades_obtained = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

filtered_grades = list(filter(lambda grade: grade > 2.0, grades_obtained))

print("Arithmetic mean for grades <> 2.0 is:", round(statistics.mean(filtered_grades), 2))







# from functools import reduce

# # Function to add two numbers
# def add(x, y):
#    return x + y

# numbers = [1, 2, 3, 4, 5]

# # Using reduce to sum the numbers
# result = reduce(add, numbers)
# print(result)  # Output: 15










# from functools import reduce
# numbers = [2,4,6,3,7,5]
# filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# sum_numbers = reduce(lambda x, y: x + y, filtered_numbers)
# print(sum_numbers)  








# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# to_third_power = list(map(lambda x: x**3, array))

# print(to_third_power)










# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# filtered_array = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, array))

# print(filtered_array)









# employees = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
#    ("Jackson","Peter"),("Johnson","Rick"),
#    ("Lewis","Terry"),("Clarke","Robin")]



# new_employees = list(map(lambda employee: f"{employee[0].upper()}, {employee[1]}\n", employees))

# print("".join(new_employees))










# points = [(17,15,16,17,15),
#  (16,18,19,17,19),
#  (19,15,15,19,18),
#  (18,17,19,15,16)]


# updated_points = []
# for i in points:
#   point_list = list(i)
#   point_list.remove(min(i))
#   point_list.remove(max(i))
#   updated_points.append(point_list)
  


# updated_points = list(map(lambda points: sum(points), updated_points))

# print(updated_points)





# results = [37, 51, 44, 23, 78, 92, 39, 84, 83, 51]

# def min_pts(limit):
#   return list(filter(lambda pts: pts>=limit, results))


# print(min_pts(70))
# print(min_pts(40))
# print(min_pts(30))





# temperatures = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

# temperatures = list(filter(lambda item: item[1] > 0, temperatures.items()))

# print(temperatures)







# test_results = [
#    {"name":"Peter","result":27},
#    {"name":"Anna","result":63},
#    {"name":"Robert","result":92},
#    {"name":"Paul","result":46},
#    {"name":"Barbara","result":52}]

# test_results = list(filter(lambda item: item["result"] >= 50 and item["result"] <= 70, test_results))

# print(test_results)






# medal_classification = [{"country":"Denmark","gold":2,"silver":4,"bronze":6},
#                         {"country":"Finland","gold":5,"silver":0,"bronze":4},
#                         {"country":"USA","gold":12,"silver":5,"bronze":11},
#                         {"country":"Peru","gold":0,"silver":1,"bronze":7}]


# medal_classification = list(filter(lambda country: country["gold"] + country["silver"] + country["bronze"] >= 10, medal_classification))

# print(medal_classification)







# bottle_capacity = 500
# tolerance = 0.02  
# filled_bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]

# min_fill = bottle_capacity * (1 - tolerance)
# max_fill = bottle_capacity * (1 + tolerance)

# incorrect_bottles = list(filter(lambda fill: fill < min_fill or fill > max_fill, filled_bottles))

# incorrect_percentage = (len(incorrect_bottles) / len(filled_bottles)) * 100

# print(f"Bottle capacity:    {bottle_capacity}ml")
# print(f"Filling tolerance:  {int(tolerance * 100)}%")
# print(f"Filled bottles:     {','.join(map(str, filled_bottles))}")
# print(f"Incorrectly filled: {int(incorrect_percentage)}%")


