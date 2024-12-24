# import EBook


# def main():
#   ebook = EBook.EBook('The Journey Beyond', 'Alex Carter', 320)
  
#   ebook.open_ebook()
#   ebook.show_ebook_status()
#   ebook.read_pages(20)
#   ebook.show_ebook_status()
#   ebook.close_ebook()
#   ebook.read_pages(20)
  
  
  
  
# if __name__ == "__main__":
#   main()






# import random

# class Thermometer:
#   def __init__(self):
#     self.temperature = 0
    
#   def turn_on_thermometer(self):
#     print('Thermometer is turned on')
    
#   def turn_off_thermometer(self):
#     print('Thermometer is turned off')
    
#   def set_temperature(self):
#     self.temperature = random.randint(34, 42)
  
#   def show_temperature(self):
#     if self.temperature >= 37:
#       print('Temperature: ', self.temperature, '(fever)')
#     if self.temperature >= 41:
#       print('CRITICAL TEMPERATURE!!!')
#     else:
#       print('Temperature: ', self.temperature)
      
      


# thermometer = Thermometer()
# thermometer.turn_on_thermometer()
# thermometer.set_temperature()
# thermometer.show_temperature()
# thermometer.turn_off_thermometer()



# import random
# class BankAccount:
#   def __init__(self, account_number):
#     self.bank_account_number = account_number
#     self.balance = 0
  
#   def deposit(self, amount):
#     self.balance += amount
    
#   def withdraw(self, amount):
#     if self.balance >= amount:
#       self.balance -= amount
#     else:
#       print('Insufficient funds on the account')
      
#   def show_bank_account(self):
#     print('Bank Account No: ', self.bank_account_number)
#     print('Balance: ', self.balance)
    
    


# bank_account = BankAccount('12 3456 5555 9090 1111 0000 7722')

# bank_account.show_bank_account()
# bank_account.deposit(25.30)
# bank_account.show_bank_account()
# bank_account.withdraw(31.70)
# bank_account.show_bank_account()
# bank_account.withdraw(14)
# bank_account.show_bank_account()








# import statistics
# class Statistics:
#   def __init__(self, array):
#     self.array = array
    
#   def add_number(self, number):
#     self.array.append(number)
    
#   def show_number(self):
#     for i in self.array:
#       print(i, end=' ')
    
#   def max_number(self):
#     return max(self.array)
  
#   def min_number(self):
#     return min(self.array)
  
#   def avg_number(self):
#     return sum(self.array) / len(self.array)
  
#   def median(self):
#     return statistics.median(self.array)
  
#   def show_info(self):
#     print('Min number: ', self.min_number())
#     print('Max number: ', self.max_number())
#     print('Arithmetic mean: ', self.avg_number())
#     print('Median: ', self.median())
    
    
  
  
  
  
  
# my_statistics = Statistics([12, 37, 6, 9, 17])

# my_statistics.show_info()









# class Contact:
#   def __init__(self, name, email, telephone):
#     self.name = name
#     self.email = email
#     self.telephone = telephone
    
#   def show_contact(self):
#     print('Name: ', self.name)
#     print('Email: ', self.email)
#     print('Telephone: ', self.telephone)
     
    
# class ContactList:
#   def __init__(self, contacts):
#     self.contacts = contacts
    
#   def add_contact(self, contact):
#     self.contacts.append(contact)
    
#   def show_contacts(self):
#     for i in self.contacts:
#       i.show_contact()
#       print()






# class C:
#   def __init__(self, name, surname, age, seniority):
#     self.name = name
#     self.surname = surname
#     self.age = age
#     self.seniority = seniority
  
#   def __str__(self):
#     if self.age <= 18:
#       return f"{self.surname.lower()}{self.name[0].lower()}{self.seniority}"
#     else:
#       return f"{self.surname.upper()}{self.name[0].upper()}{self.seniority}"
    
    
    

# c1 = C("Anna", "May", 17, 7)
# c2 = C("George", "Brown", 21, 4)

# print(c1)
# print(c2)









# class C:
#   def __init__(self, points):
#     self.points = points
    
#   def m(self, n):
#     count = sum(1 for x, y in self.points if x > 0 and y > 0)
#     return count >= n
  
  
  
# c = C([[2,3],[1,8],[-6,4],[3,-7]])
# print(c.m(2)) 
# print(c.m(3))







# class C:
#   def __init__(self, data):
#     self.data = data
    
#   def m1(self, s, n):
#     self.data[s] = n
      
#   def m2(self, s):
#     sum = 0
#     for sector in s:
#       if sector in self.data:
#         sum += self.data[sector]
#     return sum
  
  
# stadium = C({"A":120,"D":150,"G":90,"K":110})

# stadium.m1("G", 130)
# print(stadium.m2("GD"))
# print(stadium.m2("KEJ"))

      
  



      




     
      
    
    




    


  
  



  
  

