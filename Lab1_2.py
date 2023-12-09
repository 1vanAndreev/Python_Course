def calculate_number_of_books(disk_size_mb, pages_amount, lines_amount, symbols_amount):
  disk_size_b = disk_size_mb * 1048576
  book_size_b = pages_amount * lines_amount * symbols_amount * 4
  amount_books = disk_size_b // book_size_b
  return amount_books

disk_size_mb = 1.44
pages_amount = 100
lines_amount = 50
symbols_amount = 25
amount_books = calculate_number_of_books(disk_size_mb, pages_amount, lines_amount, symbols_amount)
print(f"На дискету можно поместить {amount_books} книг.")
