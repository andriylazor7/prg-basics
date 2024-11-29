def number_of_words(text):
  text_splitted = text.split()
  return len(text_splitted)


def from_longest_to_shortest(text):
  text_splitted = text.split()
  return sorted(text_splitted, key=len, reverse=True)


def alphabetically_ordered(text):
  text_splitted = text.split()
  return sorted(text_splitted)
