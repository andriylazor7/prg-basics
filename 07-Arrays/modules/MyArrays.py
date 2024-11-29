def second_largest_number_in_array(array):
  unique_array = list(set(array))
  
  unique_array = sorted(unique_array)
  
  return unique_array[-2]



def max_min_difference(array):
  return max(array) - min(array)


def median(array):
  sorted_arr = sorted(array)
    
  n = len(sorted_arr)
  mid = n // 2
  
  if n % 2 == 1:
      return sorted_arr[mid]
  else:
      return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
    
    
    
def smallest_largest_number(array):
  result = []
  result.append(min(array))
  result.append(max(array))
  return result



def numbers_as_string(array):
  return "-".join(str(num) for num in array)


