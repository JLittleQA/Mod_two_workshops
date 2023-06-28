lib_catagory_num = []

def addItem(number, name): 
    if number > 1000: 
        return "The value is too high"
    elif number <= 0: 
        return "Needs to be a whole value"
    elif number in lib_catagory_num:
        return "Needs to be a number that doesn't exist"
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