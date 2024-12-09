# mobile = {
#   "OS": "IOS",
#   "Brand": "Apple",
#   "Year": 2022,
#   "DisplayDiagonal": "6 inch",
#   "StorageCapacity": "128GB",
#   "CameraResolution": "12MP"
# }

# for key,value in mobile.items():
#    print(f"{key} : {value}")







# person = {
#    "name": "Marek",
#    "surname": "Banach",
#    "age": 25,
#    "hobby": ["swimming","excursions"],
#    "married": True,
#    "phone":{"landline":"123444321","mobile":"777888999"}
# }


# print(person['name'])
# print(person['hobby'])

# for key, value in person.items():
#   print(f"{key}: {value}")
  
# person['surname'] = 'Nowak'

# person["married"] = False

# person['gender'] = 'male'

# person["hobby"].append('bicycle')

# person['phone']['workphone'] = '313131444'

# for key, value in person.items():
#   print(f"{key}: {value}")










# countries = [
#     {"name": "Poland", "population": 38000000},
#     {"name": "Germany", "population": 83100000},
#     {"name": "France", "population": 67000000},
#     {"name": "Italy", "population": 59000000},
#     {"name": "Spain", "population": 47000000}
# ]

# print("COUNTRY   POPULATION")
# for country in countries:
#     print(f"{country['name']:<10} {country['population']}")









# phone_book = {
#   'John': '555-1234',
#   'David': '555-5678',
#   'Bob': '555-8765',
#   'Charlie': '555-4321',
#   'Diana': '555-9876',
#   'Eve': '555-6543',
#   'Frank': '555-3456',
#   'Grace': '555-7890',
#   'Hank': '555-1111',
#   'Ivy': '555-2222',
#   'Jack': '555-3333',
#   'Daniel': '555-4444',
#   'Liam': '555-5555',
#   'Mia': '555-6666',
#   'Nina': '555-7777',
#   'Oscar': '555-8888',
#   'Paul': '555-9999',
#   'Dominic': '555-1010',
#   'Rachel': '555-2020',
#   'Sam': '555-3030'
# }



# for name in phone_book.keys():
#   if name.startswith('D'):
#     print(f"{name}: {phone_book[name]}")






    
# products = {
#   'Laptop': 15,
#   'Desktop PC': 10,
#   'Monitor': 25,
#   'Keyboard': 50,
#   'Mouse': 60,
#   'External Hard Drive': 30,
#   'Printer': 12,
#   'Router': 20,
#   'USB Flash Drive': 100,
#   'Graphics Card': 8
# }


# total = 0
# for key, value in products.items():
#   print(f"{key}: {value}")
#   total += value
  
# print()
# print("Total: ", total)







# price_list = {
#    'T-shirt': 19.99,
#    'Jeans': 49.99,
#    'Jacket': 89.99,
#    'Sneakers': 59.99,
#    'Hat': 15.99
# }

# total = 0
# for key, value in price_list.items():
#   print(f"{key}: {value}")
#   total += value
  
# print("Total value of the products before the discount: ", total)

# total = 0
# for key in price_list.keys():
#   price_list[key] = price_list[key] * 0.9
#   total += price_list[key]

  

# print(price_list)
# print("Total value of the products after the discount: ", total)










# emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]
# unique_emails = set(emails)  # Removes duplicates
# print(unique_emails)





# all_students = {"Alice", "John", "Sara", "Bob"}
# attended_students = {"Alice", "Bob"}

# absent_students = all_students - attended_students  # Difference
# print(absent_students)







# emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}
# spam_list = {"spam1@example.com", "spam2@example.com"}

# spam_emails = emails_received & spam_list  # Intersection
# print("Spam emails:", spam_emails)







# contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}
# contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}

# merged_contacts = set(contacts_A | contacts_B)  # Union
# print("Merged contacts:", merged_contacts)






# required_permissions = {"read", "write", "execute"}
# user_permissions = {"read", "write"}

# has_permissions = user_permissions.issubset(required_permissions)
# print(has_permissions)  # Will return False because "execute" is missing.




# import queue

# expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
# expression2 = "[(2+3]/4)"                 # brackets not correct
# expression3 = "(2-3*4+(5/6)"              # brackets not correct

# def brackets_ok(expression):
#     # Stack to keep track of opening brackets
#     stack = queue.LifoQueue()

#     # Define matching pairs for brackets
#     matching_brackets = {')': '(', '}': '{', ']': '['}

#     for char in expression:
#         if char in "({[":  # If the character is an opening bracket
#             stack.put(char)
#         elif char in ")}]":  # If the character is a closing bracket
#             if stack.empty():  # Stack is empty, no opening bracket to match
#                 return False
#             top = stack.get()
#             if top != matching_brackets[char]:  # Check for mismatch
#                 return False

#     # If stack is empty, all brackets matched; otherwise, not balanced
#     return stack.empty()

# # Check the expressions
# if brackets_ok(expression1):
#     print("Expression 1 is correctly bracketed.")
# else:
#     print("Expression 1 is not correctly bracketed.")

# if brackets_ok(expression2):
#     print("Expression 2 is correctly bracketed.")
# else:
#     print("Expression 2 is not correctly bracketed.")

# if brackets_ok(expression3):
#     print("Expression 3 is correctly bracketed.")
# else:
#     print("Expression 3 is not correctly bracketed.")




# from collections import deque

# def to_binary_stack(number):
#   stack = deque()
  
#   while number > 0:
#     remainder = number % 2
#     stack.append(remainder)
#     number //= 2
    
#   binary_number = ''
#   while stack:
#     binary_number += str(stack.pop())
#   return binary_number

# number = int(input("Enter natural number: "))


# print(f"The binary representation of {number} is {to_binary_stack(number)}")










# import queue

# # creates a queue of files to print
# files_to_print = queue.Queue()

# while True:
#   print('1. Add file to print')
#   print('2. Print file')
#   print('0. Quit')
#   menu = input('Select an option: ')

#   if menu == '1':
#     file_name = input('Enter file name to print: ')
#     files_to_print.put(file_name)

#   elif menu == '2':
#     if not files_to_print.empty():
#         file_to_print = files_to_print.get()
#         print(f'File {file_to_print} is currently being printed. Please wait!')
#     else:
#         print("Files queue is empty!")

#   elif menu == '0':
#     break
















# translations = {
#    'computer': 'komputer',
#    'mouse': 'myszka',
#    'keyboard': 'klawiatura',
#    'printer': 'drukarka'
# }

# word = input("Enter a word to translate to Polish: ")

# print("Translation: ", translations[word])






# winter_semester = {
#    "math":60,
#    "programming":30,
#    "history":15
# }

# print("Total number of hours: ", winter_semester["math"] + winter_semester["programming"] + winter_semester["history"])



# from collections import Counter

# def count_word_frequency(paragraph):
#   paragraph = paragraph.split()
  
#   word_count = Counter(paragraph)
  
#   return word_count

# paragraph = "cat dog mouse cat rat cat mouse"

# print("Count of each word in paragraph\n")

# word_frequency = count_word_frequency(paragraph)

# for key, value in word_frequency.items():
#   print(f"{key}: {value}")








# basic_data = {
#    "name":"Barbara",
#    "age":21
# }

# advanced_data = {
#    "status":"student",
#    "married":False,
#    "interest":["reading","swimming"]
# }

# basic_data.update(advanced_data)

# for key, value in basic_data.items():
#   print(f"{key}: {value}")











# hotels_in_Krakow = [
#    {"name":"Sky","price":320.00},
#    {"name":"Metropol","price":480.00},
#    {"name":"New Port","price":420.00},
#    {"name":"Aparthotel","price":390.00}
# ]

# hotels_in_Sopot = [
#    {"name":"Focus","price":510.00},
#    {"name":"Aqua","price":345.00},
#    {"name":"La Boutique","price":390.00},
#    {"name":"Marina","price":410.00}
# ]

# def hotel_list(hotels):
#   separated = ''
#   for i in range(len(hotels)):
#     for key in hotels[i].keys():
#       if key == 'name':
#         separated += f"{(hotels[i][key])}, "
#   return separated[:-2]

# def avg_price(hotels):
#   sum_of_prices = 0
#   for i in range(len(hotels)):
#     for key in hotels[i].keys():
#       if key == 'price':
#         sum_of_prices += hotels[i][key]
#   return sum_of_prices/len(hotels)

# print("Hotels in Krakow: ", hotel_list(hotels_in_Krakow))
# print("Average hotel price in Krakow: ", avg_price(hotels_in_Krakow))
# print("Hotels in Sopot: ", hotel_list(hotels_in_Sopot))
# print("Average hotel price in Sopot: ", avg_price(hotels_in_Sopot))

# if avg_price(hotels_in_Krakow) > avg_price(hotels_in_Sopot):
#   print("Cheaper hotels in Sopot")
# else:
#   print("Cheaper hotels in Krakow")







# # Price list
# prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# # Shopping cart with quantities
# cart = {'juice': 3, 'bread': 1, 'milk': 2}

# # Calculate total cost
# def calculate_total_cost(prices, cart):
#   total_cost = 0
#   for key in cart.keys():
#       total_cost += prices[key] * cart[key]
#   return total_cost



# print("Total cost: ", calculate_total_cost(prices, cart))





# file_name_vehicle = 'vehicle.txt'
# file_name_province = 'province.csv'

# with open(file_name_vehicle, 'r') as file:
#     car_plates = file.readlines()

# numbers_data = [line.strip() for line in car_plates]

# regions_dict = {}

# with open(file_name_province, 'r') as file:
#     for line in file:
#         letter, name = line.strip().split(',')
#         regions_dict[letter] = name

# car_count_by_province = {region: 0 for region in regions_dict.values()}


# for plate in car_plates:
#     province_code = plate[0]
#     if province_code in regions_dict:
#         province_name = regions_dict[province_code]
#         car_count_by_province[province_name] += 1
        
        
# for province, count in car_count_by_province.items():
#     print(f"{province}: {count} cars")







# import json  

# # Read the contents of the json file
# voting = json.load(open('voting.json'))

# # Vote for a person
# person_name = input('Name of the person you are voting for:')

# for key in voting.keys():
#     if key == person_name:
#         voting[key] += 1

# with open('voting.json', 'w') as file:
#     json.dump(voting, file)
    
# print(f"Succesfully voted for {person_name}")









# from queue import LifoQueue
# text = input("Enter string: ")
# stack = LifoQueue()

# for char in text:
#     stack.put(char)
    
# reversed_string = ''
# while not stack.empty():
#     reversed_string += stack.get()
    
# print("Reversed string: ", reversed_string)








# def rpn_calculator(expression):
#     operations = {
#         '+': lambda a,b: a + b,
#         '-': lambda a,b: a - b,
#         '*': lambda a,b: a * b,
#         '/': lambda a,b: a / b,
#     }
    
#     stack = []
    
#     for key in expression.split():
#         if key == '=':
#             continue
#         if key in operations:
#             b = stack.pop()
#             a = stack.pop()
            
#             stack.append(operations[key](a,b))
#         else:
#             stack.append(float(key))
        
#     return stack.pop()



# print(rpn_calculator('2 3 +'))
# print(rpn_calculator('2 4 1 + *'))
# print(rpn_calculator('2 3 + 4 5 + *'))
# print(rpn_calculator('8 3 1 + / 3 2 - 4 + *'))





# import queue

# ticket_counter = 1
# customers_queue = queue.Queue()


# def issue_ticket():
#     global ticket_counter
#     customers_queue.put(ticket_counter)
#     print("Ticket issued ", ticket_counter)
#     ticket_counter += 1
    
# def serve_next_customer():
#     if not customers_queue.empty():
#         next_customer = customers_queue.get()
#         print("Serving customer with ticket ", next_customer)
#     else:
#         print("No customers in the queue")
        
# def display_queue():
#     if customers_queue.empty():
#         print("Queue is empty!")
#     else:
#         print(f"Customers in queue: {[customers_queue.queue[i] for i in range(customers_queue.qsize())]}")
        
        
        

# issue_ticket()
# issue_ticket()
# issue_ticket()

# serve_next_customer()
# serve_next_customer()

# display_queue()







# import json

# # Open the JSON file in read mode
# with open('computer.json', 'r', encoding='utf-8') as file:
#    # Load the data from the JSON file into a variable
#    data = json.load(file)

# # Print the JSON data
# for key , value in data.items():
#    print(key,':',value)








# import json

# with open('cities.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
    
    
# for city in data:
#     for key, value in city.items():
#         print(key,':', value)
#     print()





# import json

# with open('dogs.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
    


# for dog in data:
#     for key in dog.keys():
#         if key == 'age' and dog[key] < 5:
#             print(dog)













# import json
# file_name = 'reservations.json'

# def read_json_file(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#     return data


# def number_of_rooms(data):
#     return len(data['reservations']) 

# def number_of_paid_reservations(data):
#     paid_reservations = 0
#     for room in data['reservations']:
#         for key in room.keys():
#             if key == 'paid' and room[key] == True:
#                 paid_reservations += 1
#     return paid_reservations 

# def number_of_unpaid_reservations(data):
#     unpaid_reservations = 0
#     for room in data['reservations']:
#         for key in room.keys():
#             if key == 'paid' and room[key] == False:
#                 unpaid_reservations += 1
#     return unpaid_reservations 

# def total_value_of_paid_reservations(data):
#     total_value = 0
#     for room in data['reservations']:
#         for key in room.keys():
#             if key == 'paid' and room[key] == True:
#                 total_value += room['price_per_night']
#     return total_value 

# def total_value_of_unpaid_reservations(data):
#     total_value = 0
#     for room in data['reservations']:
#         for key in room.keys():
#             if key == 'paid' and room[key] == False:
#                 total_value += room['price_per_night']
#     return total_value 


# rooms = read_json_file(file_name)

# print(rooms)

# print("Number of rooms: ", number_of_rooms(rooms))
# print("Number of paid reservations: ", number_of_paid_reservations(rooms))
# print("Number of unpaid reservations: ", number_of_unpaid_reservations(rooms))
# print("Total value of paid reservations: ", total_value_of_paid_reservations(rooms))
# print("Total value of unpaid reservations: ", total_value_of_unpaid_reservations(rooms))








# import json

# data = {
#    "patient_record": {
#       "patient_id": "P001234",
#       "first_name": "John",
#       "last_name": "Doe",
#       "date_of_birth": "1985-05-15",
#       "gender": "Male",
#       "contact_info": {
#             "phone_number": "+1-555-123-4567",
#             "email": "johndoe@example.com",
#             "address": {
#                "street": "123 Main St",
#                "city": "New York",
#                "state": "NY",
#                "postal_code": "10001",
#                "country": "USA"
#             }
#       },
#       "medical_history": {
#             "allergies": ["Penicillin", "Peanuts"],
#             "current_medications": ["Lisinopril 10mg", "Metformin 500mg"],
#             "past_illnesses": ["Hypertension", "Type 2 Diabetes"],
#             "surgeries": [
#                {
#                   "surgery_type": "Appendectomy",
#                   "date": "2015-08-20"
#                }
#             ]
#       }
#    }
# }

# # Specify the file path and name
# file_name = "patient.json"

# # Open the file in write mode and use json.dump() to write the data to the file
# with open(file_name, 'w') as file:
#    json.dump(data, file, indent=4)

# print("Data has been written to", file_name)




# import json

# now_you_see_me = {
#     "title": "Now You See Me",
#     "release_year": 2013,
#     "genre": ["Crime", "Mystery", "Thriller"],
#     "director": "Louis Leterrier",
#     "writers": ["Ed Solomon", "Boaz Yakin", "Edward Ricourt"],
#     "cast": {
#         "Jesse Eisenberg": "J. Daniel Atlas",
#         "Mark Ruffalo": "Dylan Rhodes",
#         "Woody Harrelson": "Merritt McKinney",
#         "Isla Fisher": "Henley Reeves",
#         "Dave Franco": "Jack Wilder",
#         "Morgan Freeman": "Thaddeus Bradley",
#         "Michael Caine": "Arthur Tressler",
#         "Mélanie Laurent": "Alma Dray"
#     },
#     "synopsis": (
#         "A team of illusionists called 'The Four Horsemen' pull off bank heists during "
#         "their performances, rewarding their audiences with the money. As an FBI agent "
#         "and an Interpol detective track them, they discover a deeper mystery at play."
#     ),
#     "runtime_minutes": 115,
#     "box_office": {
#         "budget": 75000000,
#         "gross_worldwide": 351700000
#     },
#     "rating": {
#         "IMDb": 7.2,
#         "Rotten_Tomatoes": 50,
#         "Metacritic": 50
#     }
# }





# file_name = 'favourite.json'

# with open(file_name, 'w') as file:
#     json.dump(now_you_see_me, file, indent=4)

# print("Data has been written to", file_name)








# import json
# product = {}

# name = input("Enter product name: ")
# price = input("Enter product price: ")
# paid = bool(input("Enter whether product is paid (y/n): "))

# product['name'] = name
# product['price'] = price
# product['paid'] = paid


# file_name = 'product.json'
# with open(file_name, 'w') as file:
#     json.dump(product, file, indent=4)
    
# print("Product info has been written to", file_name)










# import json

# def load_euro_data(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         return json.load(file)

# def display_exchange_rates(data):
#     print("Date            Buying Rate     Selling Rate")
#     print("============================================")
#     for rate in data["rates"]:
#         print(f"{rate['effectiveDate']}      {rate['bid']:.4f}          {rate['ask']:.4f}")


# euro_data = load_euro_data("euro.json")

# display_exchange_rates(euro_data)











    




















    

            
            
            



















        

 
















    

  



















  
  








