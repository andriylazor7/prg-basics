class Contact:
  def __init__(self, name, email, telephone):
    self.name = name
    self.email = email
    self.telephone = telephone
    
  def show_contact(self):
    print('Name: ', self.name)
    print('Email: ', self.email)
    print('Telephone: ', self.telephone)