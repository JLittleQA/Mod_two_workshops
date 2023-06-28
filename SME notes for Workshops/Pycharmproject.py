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
    entry = 0
    name = ""
    while counter < 5:
        print(addItem(entry, name))
        counter+=1



addItem(12,2)