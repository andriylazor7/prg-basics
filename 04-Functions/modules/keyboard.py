def input_string(message):
  result = input(message)
  return result

def input_integer(message):
  result = int(input(message))
  return result

def input_real(message):
  input_string(message)

def input_boolean(message):
  result = bool(input(message))
  return result