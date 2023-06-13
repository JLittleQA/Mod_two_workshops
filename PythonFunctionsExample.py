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