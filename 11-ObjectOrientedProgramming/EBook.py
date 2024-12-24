class EBook:
  def __init__(self, title, author, number_of_pages):
    self.title = title
    self.author = author
    self.number_of_pages = number_of_pages
    self.current_page = 1
    self.is_opened = False
  
  def open_ebook(self):
    self.is_opened = True
    print('Ebook is opened')
    
  def close_ebook(self):
    self.is_opened = False
    print('Ebook is closed')
    
  def show_ebook_status(self):
    print('\nTitle: ', self.title)
    print('Author: ', self.author)
    print('Number of pages: ', self.number_of_pages)
    print('Current page number: ', self.current_page, '\n')
    
  def read_pages(self, count_of_pages):
    if self.is_opened: 
      print(f'{count_of_pages} pages was read')
      self.current_page += count_of_pages
    else:
      print('Can not read because ebook is closed')
      
  def to_next_page(self):
    self.current_page += 1
    
  def to_previous_page(self):
    self.current_page -= 1
    
  
    

