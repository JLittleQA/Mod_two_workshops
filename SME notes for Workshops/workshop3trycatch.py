lib_catagory_num = []

def addItem(number, name): 
    try:
        max  = 1000
        min = 0
        if number > max:
            raise ArithmeticError("You cannot be greater than 1000")
        elif number <= min:
            raise ArithmeticError("Number cannot be less than 0")
    except ArithmeticError:
            print("This number is invalid")
    else:
        lib_catagory_num.append({"Id":number,"book":name})
        return lib_catagory_num 

def removeItem(number):
    for i in range(len(lib_catagory_num)):
        if lib_catagory_num[i]["Id"] == number:
            del lib_catagory_num[i]
            break
        
    return lib_catagory_num

def updateItem(number, newname): 
    for i in range(len(lib_catagory_num)):
        if lib_catagory_num[i]["Id"] == number: 
            lib_catagory_num[i]["book"] = newname
            break
    return lib_catagory_num
    
def main():
    counter = 0 
    while counter < 5:
        try: 
            entry = int(input("Please enter the catalog number: "))
        except ValueError:
            print("This is not a number try again")
            entry = int(input("Please enter the catalog number: "))

        name = input("Please add the name of book: ") 
        print(addItem(entry, name))
        counter+=1
    new_entry = int(input("Please enter the catalog number you wish to replace: "))

    removenumber = int(input("Please input a number to remove from list: "))
    print(removeItem(removenumber))

    number = int(input("Please enter catalogue number: "))
    new_name = input("Please enter the book name replacement: ")
    print(updateItem(number, new_name))



main()