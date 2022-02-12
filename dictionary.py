#Dictionary functions
#Dictionary Creation
def create_dict():
    Dict_init = dict() #creating empty dictionary
    number_ele_Dict = int(input("Please enter number elements to be available in Dictionary:"))  
    for element in range(number_ele_Dict):
        key_n = input("please enter the Key: ")
        val_n = input("Please enter values to the Keys:")
        Dict_init[key_n] = val_n
        #Set_init.add(element_n)
    return Dict_init

#Update a dictionary
def update_dict(Dict):
    key_val = input("Please enter key value:")
    val = input("Please enter value to key:")
    Dict.update({key_val:val})
    return Dict

#Accessing dictionary elements
def access_dict(Dict):
    key_val = input("Please enter key to access value:")
    display_value = Dict.get(key_val)
    return display_value
    #return Dict

#Getting Dictionary each key value pairs
def items_dict(Dict):
    display_items = Dict.items()
    return display_items
    #return Dict

#Getting Dictionary Keys list
def keys_dict(Dict):
    display_keys = Dict.keys()
    return display_keys
    #return Dict

#Copying a Dictionary
def copy_dict(Dict):
    copy_Dict = Dict.copy()
    return copy_Dict

#Removes element from specified key
def pop_dict(Dict):
    key_val = input("Please enter key value to Pop:")
    pop_val = Dict.pop(key_val)
    return Dict

#Removes last inserted key value pair
def popItem_dict(Dict):
    popItem = Dict.popitem()
    return Dict

#Removes all elements from the dictionary
def clear_dict(Dict):
    Dict.clear()
    return Dict

#Finding length of the dictionary
def len_dict(Dict):
    return len(Dict)

# Delete a dictionary
def del_dict(Dict):
    del Dict

#List of all values in the dictionary
def check_values(Dict):
    display_values = Dict.values()
    return display_values

#Value of the specified key
def setDefault_dict(Dict):
    key_val = input("Please enter key value:")
    val = input("Please enter value to key:")
    display_value = Dict.setdefault(key_val,val)
    return display_value
