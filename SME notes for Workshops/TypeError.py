


try:
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    book = input("Please enter your favourite books: ")
    print(name+age+book)
except TypeError:
    print("cannot concatinate integer and strings together")
    new_age = str(age)
    print(f"Fixed: {name+new_age+book}")
    