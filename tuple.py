#Tuple Functions
#Tuple creation
def create_tuple():
    tuple_init = () #create empty tuple
    Li_Tup = list(tuple_init)
    number_ele_Tuple = int(input("Please enter number elements to be available in Tuple:"))  
    for element in range(number_ele_Tuple):
        key_n = input("Please enter the elements to your Tuple: ")
        Li_Tup.append(key_n)
        tuple_init = tuple(Li_Tup)
    return tuple_init

#Finding occurances of an element
def count_tuple(Tuple):
    count_element = input("Enter the Element to find out its frequency:")
    Count = Tuple.count(count_element)
    return Count

#Finding index of an element
def index_tuple(Tuple):
    count_element = input("Enter the Element to find out its Index of First Occurance:")
    Index = Tuple.index(count_element)
    return Index

#Concatenation of two tuples
def concate_tuple(Tuple):
    Tuple_new = ()
    List_new = list(Tuple_new)
    number_ele_NTuple = int(input("Please enter number elements to be available in new Tuple:"))  
    for element in range(number_ele_NTuple):
        element_n = input("Please enter the element: ")
        List_new.append(element_n)
        Tuple_new = tuple(List_new)
        T = Tuple + Tuple_new
    return T

#length of tuple
def len_tuple(Tuple):
    return len(Tuple)

#Delete tuple
def del_tuple(Tuple):
    del Tuple
    #return Tuple
'''
def update_tuple(Tuple):
    tuple_new = ()
    Li_tuple_new = list(tuple_new)
    number_ele_Tuple = int(input("Please enter number elements to be available in Tuple:"))  
    for element in range(number_ele_Tuple):
        key_n = input("please enter the elements to your Tuple: ")
        Li_tuple_new.append(key_n)
        tuple_new = tuple(Li_tuple_new)
    return Tuple
'''
