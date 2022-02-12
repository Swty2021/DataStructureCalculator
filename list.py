#List Module
from statistics import mean,median
#List Functions
#Creation of List
def create_list():
    List_init = [] #creating empty list
    number_ele_List = int(input("Please enter number elements to be available in list:"))  
    for element in range(number_ele_List):
        element_n = int(input("please enter the element: "))
        List_init.append(element_n)
    return List_init

#add element into the list
def append_list(List):
    element_to_be_inserted = int(input("Please enter the element to be inserted: "))
    List.append(element_to_be_inserted)
    return List

#pop element
def pop_list(List):
    #Two different types of pop operations
    element_to_be_poped = int(input("Please enter the position of the element to be pop:"))
    List.pop(element_to_be_poped)
    return List

#Finding length    
def len_list(List):
    return len(List)

#Finding sum of the List
def sum_list(List):
    return sum(List)

#Finding Max element in the list
def max_list(List):
    return max(List)

#Finding Min element in the list
def min_list(List):
    return min(List)

#Sort the list
def sort_list(List):
    return sorted(List)

#Finding Mean of the list
def mean_list(List):
    return mean(List)

#Finding Median of the list
def median_list(List):
    return median(List)

#Finding the occurances of an element
def count_list(List):
    freq_ele_num = int(input("Enter the element to find its frequency:"))
    return List.count(freq_ele_num)

#Inserting element into the List
def insert_list(List):
    insert_position = int(input("Enter the position where element is to be added:"))
    insert_element = int(input("Enter the element you want to add:"))
    List.insert(insert_position,insert_element)
    return List

#Concatenation of Lists
def concate_list(List):
    List_new = []
    number_ele_NList = int(input("Please enter number elements to be available in new list:"))  
    for element in range(number_ele_NList):
        element_n = int(input("please enter the element: "))
        List_new.append(element_n)
        List.extend(List_new)
    return List

#Reverse the list
def reverse_list(List):
    List.reverse()
    return List

#Slicing of the List
def slice_list(List):
    starting_point = int(input("Enter your starting point of list:"))
    ending_point = int(input("Enter end point:"))
    return List[starting_point:ending_point]
    #return List

#Clear List
def clear_list(List):
    List.clear()
    return List

#Copy the list
def copy_list(List):
    New_List = List.copy()
    return New_List
