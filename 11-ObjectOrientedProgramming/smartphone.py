import contact
import ContactList

contact1 = contact.Contact('John Brown', 'brown@onet.pl', 555234000)      
contact2 = contact.Contact('Anna May', 'am@o2.pl', 232000199)      
contact3 = contact.Contact('George Small', 'smallg@google.pl', 222999100)

contacts = [contact1, contact2, contact3]


contact_list = ContactList.ContactList(contacts)

contact_list.add_contact(contact.Contact('Paola Big', 'bigpaola@poczta.pl', 100200300))

contact_list.show_contacts()