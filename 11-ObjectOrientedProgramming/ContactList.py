class ContactList:
  def __init__(self, contacts):
    self.contacts = contacts
    
  def add_contact(self, contact):
    self.contacts.append(contact)
    
  def show_contacts(self):
    for i in self.contacts:
      i.show_contact()
      print()