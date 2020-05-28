import csv
with open("books.csv") as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = [row['ISBN'] for row in books_reader]
  print(isbn_list)