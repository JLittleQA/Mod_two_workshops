books = []
num = 0 
while num < 8:
    book_input = input("Please enter a book title: ")
    books.append(book_input)
    num += 1

print(books)

# Loop through the list and add this into a string format Stretch goal 
for book in books: 
    new_string = ", ".join(books)

print(new_string)

# A user selects a book to take out and put this in the form of an F string. 
customer = input("Please enter customers name: ")

book_name = input("Please enter book name: ")

if book_name in books: 
    print(f"{customer} has checked out {book_name}")