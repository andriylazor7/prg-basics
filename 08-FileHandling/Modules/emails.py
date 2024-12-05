def match_in_email(regex, content):
  import re
  return re.search(regex, content)