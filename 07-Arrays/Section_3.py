# import random

# arr1 = [3,7,1,0,4]
# arr2 = [[2,3],[7,1],[0,4]]
# arr3 = [7 for i in range(5)]
# arr4 = [i for i in range(1,10)]
# arr5 = [i*2 for i in range(1,10)]
# arr6 = [random.randint(1,20) for i in range(10)]
# arr7 = [[] for i in range(5)]
# arr8 = [[1 for i in range(2)] for j in range(4)]
# arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]

# print(arr1)
# print(arr2)
# print(arr3)
# print(arr4)
# print(arr5)
# print(arr6)
# print(arr7)
# print(arr8)
# print(arr9)





# arr = [34, 7, 19, 4, 21, 8]

# i = 0
# count = 0
# while i < len(arr):
#   if arr[i] % 2 == 0:
#     count += 1
#   i += 1
  
# print("Number of even value in array: ", count)








# arr = [15, 8, 31, 47, 2, 19]

# reversed = []

# for i in range(len(arr)):
#   reversed.append(arr[-(i + 1)])
  
# print("Existed array: ", arr)
# print("Reversed array: ", reversed)




# arr = [8, 2, 5, 1, 9]

# powered = []

# for i in range(len(arr)):
#   powered.append((arr[i])**2)
  
# print("Array: ", arr)
# print("2nd power: ", powered)






# arr = [-15, 8, -31, 47, -2, 19]

# max = arr[0]
# for i in range(len(arr)):
#   if arr[i] > max:
#     max = arr[i]
    
# min = arr[0]
# for i in range(len(arr)):
#   if arr[i] < min:
#     min = arr[i]
    

    
# print("Max value: ", max)
# print("Min value: ", min)







def printArr(arr):
  for i in arr:
    print(i, end=' ')
  print()





# arr = [15, 8, 31, 47, 2, 19]
   
# sum = 0 
# for i in range(len(arr)):
#   sum += arr[i]
  
# printArr(arr)
# print("Arithmetic mean: ", sum/len(arr))



# arr = [15, 8, 31, 47, 2, 19]

# sum = 0
# i = 0
# while i < len(arr):
#   sum += arr[i]
#   i += 1

# printArr(arr)
# print("Arithmetic mean: ", sum/len(arr))





# polish_names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

# longest_name = max(polish_names, key=len)
# print("Longest name: ", longest_name)







# arr = [2, 6, 4, 9, 7]

# def count(n):
#   res = []
#   for i in range(n):
#     res.append('*')
#   return "".join(res)

# for i in range(len(arr)):
#   print(f"{arr[i]}: {count(arr[i])}")





# def compare(array1, array2):
#   print("Array 1: ", array1)
#   print("Array 2: ", array2)
#   if len(array1) == len(array2) and array1 == array2:
#     return "Comparison: arrays are the same\n"
#   return "Comparison: arrays are not the same\n"



# print(compare(["water","book","sky"], ["water","book","sky"]))
# print(compare([True,False], [True,False,True]))
# print(compare([5,3,1], [5,3,1]))
# print(compare([3,2,1], [3,2]))




# def numbers_not_appear(arr1, arr2):
#   result = []
#   for i in range(len(arr2)):
#     if arr2[i] not in arr1:
#       result.append(arr2[i])
#   return result
  

# arr1 = [4, 36, 12, 28, 9, 44, 5]
# arr2 = [5, 1, 36]


# print(numbers_not_appear(arr1, arr2))






# def bubbleSort(arr):
#   n = len(arr)
#   for i in range(n - 1):  
#     for j in range(n - i - 1):  
#       if arr[j] > arr[j + 1]:
#         arr[j], arr[j + 1] = arr[j + 1], arr[j]
#   return arr



# arr1 = [6, 78, 9, 14, 5]
# arr2 = [12, -3, 7, -65, 2]
# arr3 = [10, 5, 34, 20, 9]

# bubbleSort(arr1)
# bubbleSort(arr2)
# bubbleSort(arr3)

# printArr(arr1)
# printArr(arr2)
# printArr(arr3)





# def unique_elements(arr):
#   unique = []
#   for i in arr:
#     if arr.count(i) == 1:
#       unique.append(i)
#   return unique


# arr = [2, 3, 2, 5, 8, 1, 9, 8]


# print(unique_elements(arr))







# arr = [15, 38, 7, 23, 14]

# def occurs(number, array):
#   for i in range(len(array)):
#     if arr[i] == number:
#       return True
#   return False


# number = int(input("Enter number: "))
# if occurs(number, arr): print(f"Number {number} appears in the array")
# else: print(f"Number {number} does not appear in the array")





# single_word_tuple = ('computation',)

# print(type(single_word_tuple))






# number_tuple = (10,20,30,40,50)

# print("Reverse order: ", number_tuple[::-1])






# tuple_ = ("Seven", [10, 20, 30], (5, 15, 25))

# print(tuple_[0])
# print(tuple_[1][2])





  
  
  
# import MyArrays  

# numbers = [7,3,8,5,2]

# print("Numbers: ", numbers)

# print("Second largest number ", MyArrays.second_largest_number_in_array(numbers))
# print("Median: ", MyArrays.median(numbers))
# print("Smallest and largest number: ", MyArrays.smallest_largest_number(numbers))
# print("Numbers as a string: ", MyArrays.numbers_as_string(numbers))







# arr = [34, 5, 6, 7, -4, 15, 8]

# def greater_than(arr, number):
#   count = 0
#   for i in range(len(arr)):
#     if arr[i] > number:
#       count += 1
#   return count


# number = int(input("Enter number: "))
# print("Numbers that are greater than the given value: ", greater_than(arr, number))






# arr = [34, 5, 6, 7, -4, 15, 8]


# def even_separation(arr):
#   even = [arr[i] for i in range(len(arr)) if arr[i] % 2 == 0]
#   return even

# def odd_separation(arr):
#   odd = [arr[i] for i in range(len(arr)) if arr[i] % 2 != 0]
#   return odd


# print("Even numbers: ", even_separation(arr))  
# print("Odd numbers: ", odd_separation(arr))  





















  

  
  







