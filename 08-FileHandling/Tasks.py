# ###
# # Reads the entire contents of a file
# #
# def read_from_file(name):
#    with open(name, 'r') as file:
#       content = file.read()
#    return content

# # reads the entire file
# file_content = read_from_file('countries.txt')

# # splits the entire file contents into lines
# # and stores them in an array
# file_lines = file_content.splitlines()

# file_lines = sorted(file_lines)

# # prints the array
# for line in file_lines:
#    print(line)





# ###
# # Reads the entire contents of a file
# #
# def read_from_file(name):
#    with open(name) as file:
#       content = file.read()
#    return content

# # reads the entire file and splits lines into array
# file_content = read_from_file('car_park.txt')
# file_lines = file_content.splitlines()

# # calculates the total number of cars parked
# total = 0
# for line in file_lines:
#    total += int(line)

# print('Total cars parked:', total)




# def read_from_file(name):
#   with open(name) as file:
#     content = file.read()
#   return content


# file_content = read_from_file('pets.txt')

# file_content = file_content.split()

# count = 0
# for i in range(len(file_content)):
#   count += 1
  
# print("Total number of words: ", count)






# ###
# # Prints employees employed in a specified position.
# #

# # Employee List
# file_name = 'it_company.csv'

# # Position
# job_title = 'Software Engineer'

# with open(file_name) as file:
#    for i, line in enumerate(file):
#       if job_title in line:
#          print(f"{i}. {line}")





# ###
# # Writes Seven Wonders of the World to a file
# #
# seven_wonders = [
#    "Great Wall of China",
#    "Petra",
#    "Christ the Redeemer",
#    "Machu Picchu",
#    "Chichen Itza",
#    "Roman Colosseum",
#    "Taj Mahal"
# ]

# # Name of the file to write to
# file_name = 'seven_wonders.txt'

# # Sort data alphabetically
# seven_wonders = sorted(seven_wonders)

# # Write data to the file
# with open(file_name, 'w') as file:
#   for item in seven_wonders:
#     file.write(f"{item}""\n")
    
    
    
    
    
    
    
    
    
    
    
# def read_from_file(file_name):
#   with open(file_name, 'r') as file:
#     content = file.read()
#   return content



# healthy_lifestyle_content = read_from_file('healthy_lifestyle.txt')

# copy = "copy_healthy_lifestyle.txt"

# with open(copy, 'w') as file:
#   file.write(healthy_lifestyle_content)







# # Saves to a file a list of employees working at a specified position.

# # file names
# employees_file = 'it_company.csv'
# position_file = 'software_engineer.txt'

# # Position
# job_title = 'Software Engineer'

# # write selected employees to a file
# with open(employees_file, 'r') as infile:
#     with open(position_file, 'w') as outfile:
#         for line in infile:
#             if job_title in line:
#                 outfile.write(line)








# ###
# # Creates a shopping list based on product names
# # entered from the keyboard.
# #

# # shopping list file name
# shopping_list = 'shopping_list.txt'

# # adds product name at the end of a shopping list
# def add_product(file_name, product_name):
#    with open(file_name,'a') as file:
#       file.write(f"{product_name}\n")

# # Takes next product name from the keyboard
# product = ""
# while product != "0":
#    product = input('Enter product name (0 stops): ')
#    if product == '0':
#       break
#    else:
#       add_product(shopping_list, product)






# import re

# email_file = 'report.txt'

# with open(email_file, 'r') as file:
#     email = file.read()

# pattern = r'[\$€¥]?\d{1,3}(?:,\d{3})*(?:\.\d+)?'

# amounts = re.findall(pattern, email)

# total = 0.0

# for match in amounts:
#     cleaned_number = match.replace(',', '')
    
#     cleaned_number = re.sub(r'[^\d.]', '', cleaned_number)
    
#     try:
#         total += float(cleaned_number)
#     except ValueError:
#         print(f"Skipping invalid match: {match}")

# # Output the result
# print(f"Total money spent: ${total:.2f}")






# ###
# # Checks the correctness of username and password
# #
# import re

# # read username and password from keyboard
# username = input("Enter username: ")
# password = input("Enter password: ")

# # pattern (criteria) for username and password
# username_pattern = r'^[a-z]{6,}$'
# password_pattern = r'^[A-Za-z0-9_]{8,}$'

# # check if username and password are ok
# username_match = re.match(username_pattern,username)
# password_match = re.match(password_pattern, password)

# # print results
# if username_match and password_match:
#    print("Username and password meet the requirements")
# else:
#    print("Username and password do not meet the requirements")




# def display_file_in_chuncks(file_name, lines_per_chunk):
#     try:
#         lines = ''
#         with open(file_name, 'r') as file:
#             while True:
#                 lines = [file.readline() for _ in range(lines_per_chunk)]
                
#                 if not any(lines):
#                     print("End of file reached.")
#                     break
                
#                 print(''.join(lines), end='\n')
                
#                 input("Press Enter key to continue...")
                
                
#     except FileNotFoundError:
#         print(f"Error: The file {file_name} was not found")
#     except Exception as e:
#         print(f"An error occured: {e}")
        
        
# display_file_in_chuncks('it_company.csv', 5)















# import Modules.emails as emails

# file_name = 'email.txt'

# sender_email_regex = r'(?<=From:\s).*<([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})>'
# recipient_email_regex = r'(?<=To:\s).*<([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})>'
# email_subject_regex = r'(?<=Subject:\s)(.*)'
# email_body_regex = r'(?:\r?\n\r?\n)([\s\S]*)'


# try:
#     with open(file_name, 'r') as file:
#         content = file.read()
        
#     sender_email = emails.match_in_email(sender_email_regex, content)    
#     recipient_email = emails.match_in_email(recipient_email_regex, content)    
#     email_subject = emails.match_in_email(email_subject_regex, content)    
#     email_body = emails.match_in_email(email_body_regex, content)    
        
# except FileNotFoundError:
#     print("Error: file not found")

# if sender_email:
#         print("Sender Email:", sender_email.group(1))
# else:
#     print("Sender Email: Not found")

# if recipient_email:
#     print("Recipient Email:", recipient_email.group(1))
# else:
#     print("Recipient Email: Not found")

# if email_subject:
#     print("Subject:", email_subject.group(1))
# else:
#     print("Subject: Not found")

# if email_body:
#     print("Body:\n", email_body.group(1))
# else:
#     print("Body: Not found")











# file_name = input("Enter file name: ")

# try:
#     with open(file_name, 'r') as file:
#         content = file.read()
#         file.seek(0)
#         number_of_lines = len(file.readlines())
        
#     print("Number of lines: ", number_of_lines)
#     print("Number of characters: ", len(content))
#     print("Number of words: ", len(content.split(' ')))
# except FileNotFoundError:
#     print("Error: File not found")
   
   
   
   
   
   
   
   
   
# import re

# text = input("Enter text: ")

# vowels_regex = r'[aeiouAEIOU]'

# vowels = re.findall(vowels_regex, text)

# print("Number of vowels: ", len(vowels))









# import re

# file_name = 'files.txt'

# extension_regex = r'\.[a-zA-z0-9]{4}$'

# with open(file_name, 'r') as file:
#     content = file.readlines()
    
# for i in content:
#     i = i.strip()
#     if re.search(extension_regex, i):
#         print(i)
        

\
    
    
    


# import csv

# file_name = 'it_company.csv'

# try:
#     with open(file_name, 'r') as file:
#         csv_reader = csv.DictReader(file)

#         for row in csv_reader:
#             if row['Job Title'] == 'Graphic Designer':
#                 print(f"{row['First Name']} {row['Last Name']}, {row['Email']}")

# except FileNotFoundError:
#     print(f"Error: The file '{file_name}' was not found.")





# import csv

# file_name = 'clothing.csv'

# try: 
#     with open(file_name, 'r') as file:
#         csv_reader = csv.DictReader(file)
        
#         for row in csv_reader:
#             if float(row['Price']) < 60 and int(row['Stock_Quantity']) < 40:
#                 print(row['Product_Name'])
# except FileNotFoundError:
#     print(f"Error: The file '{file_name}' was not found.")








# file_name = 'powers.txt'

# with open(file_name, 'w') as file:
#     for i in range(1, 101):
#         second_power = i ** 2
#         third_power = i ** 3
#         print(f"{i},{second_power},{third_power}")
#         file.write(f"{i},{second_power},{third_power}\n")

# print(f"The results have been saved to '{file_name}'.")










# import csv

# def read_books_from_csv(file_name):
#     books = []
#     try:
#         with open(file_name, 'r', newline='', encoding='utf-8') as file:
#             csv_reader = csv.DictReader(file)
#             for row in csv_reader:
#                 books.append(row)
#     except FileNotFoundError:
#         print(f"Error: The file '{file_name}' was not found.")
#     return books

# def write_books_to_genre_files(books):
#     genres = {
#         'Fantasy': 'books_fantasy.txt',
#         'Historical': 'books_historical.txt',
#         'Romance': 'books_romance.txt',
#         'Classic': 'books_classic.txt'
#     }
    
#     for genre, filename in genres.items():
#         with open(filename, 'w', encoding='utf-8') as file:
#             for book in books:
#                 if book['Genre'] == genre:
#                     file.write(f"{book['Title']} by {book['Author']}\n")

# def main():
#     input_file = 'books.csv'
    
#     books = read_books_from_csv(input_file)
    
#     write_books_to_genre_files(books)
    
#     print("Books have been sorted and saved into corresponding genre files.")

# if __name__ == '__main__':
#     main()

    
    
    

























