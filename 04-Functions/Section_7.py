import modules.month
import modules.letter_counter
import modules.within_range
import modules.hide_card_number
import modules.is_binary


# month_number = int(input('Enter month number: '))
# print(f'The name of the month {month_number} is {modules.month.month(month_number)}')







# text = input('Enter text: ')
# letter = input('Enter the letter: ')

# print(f"The number of letter '{letter}': {modules.letter_counter.letter_counter(text, letter)}")







# number = int(input('Enter a number: '))
# x = int(input('Enter min value in range:'))
# y = int(input('Enter max value in range:'))


# print(f'Number {number} in range <{x}, {y}>: {modules.within_range.is_within_range(x,y,number)}')






# card_number = input('Enter card number: ')

# print(f'Hided card number: {modules.hide_card_number.hide(card_number)}')





# number = input('Enter a number: ')

# print(f'Is binary: {modules.is_binary.is_binary(number)}')






# def f(amount_to_pay):
#   coins = [5, 2, 1]  
#   count = 0  

#   for coin in coins:
#       count += amount_to_pay // coin 
#       amount_to_pay %= coin 

#   return count



# print(f(23))
# print(f(8))
# print(f(2))
# print(f(0))








# def f(number, even):
#   if even == True:
#     sum_even = 0
#     for i in str(number):
#       if int(i) % 2 == 0:
#         sum_even += int(i)
#     return sum_even
#   else:
#     sum_odd = 0
#     for i in str(number):
#       if int(i) % 2 != 0:
#         sum_odd += int(i)
#     return sum_odd
  
  
# print(f(3124, True))  
# print(f(3124, False))  
# print(f(20576, False))  
# print(f(20576, True))  
# print(f(13115, True))  
  




# def f(x,y):
#   count = 0
#   for i in range(x, y):
#     if i % 2 == 0 and i < 0:
#       count += 1
#   return count


# print(f(-7, 8))
# print(f(-1, 11))








# def f(n1,n2,n3):
#   if n1 < 0 or n2 <0 or n3 < 0:
#     return True
#   else:
#     return False
  


# print(f(11,6,-4))
# print(f(5,4,14))




# def f(n):
#   result = ''
#   for i in range(n):
#     result += '*'
#     if i < n - 1:
#       result += '/'
#   return result



# print(f(4))
# print(f(1))







# def f(n):
#   result = ''
#   for i in range(n):
#     result += f'{i+1}'
#   return result


# print(f(11))
# print(f(4))
  
  







# def f(n1,n2,operator):
#   if operator == '+':
#     return n1 + n2
#   elif operator == '%':
#     return n1 % n2
#   elif operator == '**':
#     return n1**n2
#   elif operator == '*':
#     return n1*n2
#   elif operator == '-':
#     return n1-n2
  
  
  
# print(f(2,3,'+'))
# print(f(2,3,'%'))
# print(f(2,3,'**'))
# print(f(2,3,'*'))
# print(f(2,3,'-'))










# def f(detector):
#   if '---' in detector:
#     return True
#   else:
#     return False
  
  

# print(f("+-+++-+---"))
# print(f("+-+-+-+-")) 
# print(f("+-++-+--")) 
# print(f("+-++-++-+---")) 







# def f(n):
#   if n == 0: return 0
#   if n == 1: return 1
  
#   a,b = 0,1
#   for _ in range(3, n + 1):
#     a, b = b, a+b
#   return b



# print(f(5))
# print(f(9))










# def f(palindrome):
#   reversed = palindrome[::-1]
#   if palindrome == reversed: return True
#   else: return False
  
  
  

# print(f("radar")) 
# print(f("12-11-21")) 
# print(f("book") )










# def f (sentence):
#   result = ''
#   for i in sentence:
#     if i == ' ':
#       i = ''
#     else:
#       result += i
#   return result
  
  



# print(f("Integrated development environment"))
# print(f("A programming language is a system of notation for writing computer programs"))









# def f(number):
#     str_number = str(number)
#     repeated_sum = 0
    
#     for digit in set(str_number):  
#         count = str_number.count(digit)
#         if count > 1:
#             repeated_sum += int(digit) * count  
#     return repeated_sum


# print(f(1027))       
# print(f(230335))     
# print(f(513553007)) 








# def is_prime(num):
#   if num <= 1:
#     return False
#   for i in range(2, num):
#     if num % i == 0:
#       return False
#   return True

# def f(n):
#   count = 0  
#   num = 1    
  
#   while count < n:
#     num += 1
#     if is_prime(num):
#       count += 1
          
#   return num


# print(f(1))
# print(f(5))







# def f(n1, n2, n3):
#   numbers = set()
#   numbers.add(n1)
#   numbers.add(n2)
#   numbers.add(n3)

#   max_value = max(numbers)
#   min_value = min(numbers)
  
#   return max_value - min_value


# print(f(7,4,9))
# print(f(2,12,8))









# def f(name):
#   result = ''
#   separated = name.split(' ')
#   for i in range(len(separated)):
#     result += separated[i][0]
    
#   return result


# print(f("Internet of Things"))
# print(f("For Your Information"))
# print(f("Python"))
    
    
    
    
    
    
    
    
# def f(password):
#   if len(password) < 6:
#     return False
  
#   for i in password:
#     if password.count(i) > 1:
#       return False
    
#   return True
  
  
  
# print(f("ax15")) 
# print(f("book123")) 
# print(f("A2water3")) 
# print(f("qwerty")) 
# print(f("")) 









# def f(expression):
#   return eval(expression)




# print(f("2+3"))
# print(f("3+8+1")) 
# print(f("2+3-4+5-0"))
  
  
  
  
  
  
  

  
  
# def f(x,y):
#   sum = 0
#   for i in range(x,y + 1):
#     if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:
#       sum += i
#   return sum


# print(f(1,20))
# print(f(10,30))









# def f(text):
#   if len(text) == 0 or len(text) == 1:
#     return text
  
#   result = ''
#   for i in text:
#     result += f'{i}-'
    
#   return result[:-1]



# print(f("Univesity")) 
# print(f("UE")) 
# print(f("x")) 
# print(f("")) 

  



  
# def f(product_code):
#   sum_of_three_digits = 0
#   for i in range(len(product_code) - 1):
#     sum_of_three_digits += int(product_code[i])
    
#   control_digit = int(product_code[3])
  
#   remainder = sum_of_three_digits % 7
#   return control_digit == remainder




# print(f("1082")) 
# print(f("2035")) 
# print(f("1114")) 
# print(f("7071")) 











# import statistics

# def f(dice):
#   return (statistics.mode(list(dice)))
    
    
    
# print(f("5233165554211")) 
# print(f("2133"))









# def factorial(n):

#   # 0! = 1, 1! = 1
#   if n==0 or n==1:
#       return 1

#   # n! = n * (n-1)!
#   if n > 1:
#     return n * factorial(n-1)
  
  
  
# print(factorial(5))








# def sum(n):
#   if n <= 0:
#     return 0
#   else:
#     return n + sum(n - 1)
    
    
    
    
# print(sum(10))
      
    
    
    




# def power(x,n):
#   if n == 0:
#     return 1
#   return x * power(x, n-1)



# print(power(5,3))
  
  
  












    
    
  
  
  
  
  
  

















