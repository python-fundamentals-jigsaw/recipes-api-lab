
# pip install git+https://github.com/abenassi/Google-Search-API --user

from googleapi import google
num_page = 3
search_results = google.search("This is my query", num_page)