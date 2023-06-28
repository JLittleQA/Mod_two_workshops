#while loop to populate list

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


# Loop through the list and add this into a string format Stretch goal 
for book in books: 
    new_string = ", ".join(books)

print(new_string)

#fucntions 

books = {"The Hobit": 3, "Series of Unfortunate Events": 2, "Game of Thrones": 5, "Count of Monte Cristo": 2, 
         "Dracula": 1, "Frankenstein": 1, "Animal Farm": 3, "1984":2}

def addbooks(name, amount):
    books[name] = amount
    return books

def checkout(customer_name, book_name, amount):
    
    if book_name in books: 
        books[book_name] = amount
        if books.values() == 0:
            books.popitem(book_name) 
            return f"{customer_name} has checked out {book_name} Current books remaining {books}"
        return f"{customer_name} has checked out {book_name} Current books remaining {books}"
    else: 
        return "Please enter the name of the book"

print(addbooks("Sandman", 3))

print(checkout("Victoria", "Frankenstein", 1))