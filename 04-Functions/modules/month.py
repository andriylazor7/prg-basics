def month(n):
  """Returns the name of the month for a given number 1-12."""
  months = [
      "",  # Placeholder for index 0, as months are 1-12
      "January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"
  ]
  
  if 1 <= n <= 12:
      return months[n]
  else:
      return 'Invalid month number'