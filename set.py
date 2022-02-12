#Set Functions
#Set creation
def create_set():
    Set_init = set() #creating empty set
    number_ele_Set = int(input("Please enter number elements to be available in Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_init.add(element_n)
    return Set_init

#Adding element to set
def add_set(Set):
    element_to_be_inserted = int(input("Please enter the element to be inserted: "))
    Set.add(element_to_be_inserted)
    return Set

#Updating Set
def update_set(Set):
    Set_new = set() #creating a new empty set
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
        Set.update(Set_new)
    return Set

#Union of sets
def union_set(Set):
    Set_new = set() #creating a new empty set
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
    return Set.union(Set_new)
    #return Set

#Intersection of Sets
def intersection_set(Set):
    Set_new = set()#creating a new empty set
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
    return Set.intersection(Set_new)
    #return Set

#Difference of Sets
def difference_set(Set):
    Set_new = set()#creating a new empty set
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
    return Set.difference(Set_new)
    #return Set

#Symmetric Difference
def Symmetric_difference_set(Set):
    Set_new = set()#creating a new empty set
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
    return Set.symmetric_difference(Set_new)
    #return Set

#Pop
def pop_set(Set):
    #Two different types of pop operations
    #element_to_be_poped = int(input("Please enter the position of the element to be pop:"))
    Set.pop()
    return Set
#Summation of set elements
def sum_set(Set):
    return sum(Set)

#Finding Max element
def max_set(Set):
    return max(Set)

#Finding Min element
def min_set(Set):
    return min(Set)

#Finding lenght of set
def len_set(Set):
    #return len(Set)
    length = len(Set)
    return length

#Intersection update
def intersection_update_set(Set):
    Set_new = set()
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
        Set.intersection_update(Set_new)
    return Set

#Difference Update
def difference_update_set(Set):
    Set_new = set()
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
        Set.difference_update(Set_new)
    return Set

#Symmetric Difference Update 
def symmetric_difference_update_set(Set):
    Set_new = set()
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
        Set.symmetric_difference_update(Set_new)
    return Set
# Clear 
def clear_set(Set):
    Set.clear()
    return Set

#Discard element
def discard_set(Set):
    discard_element = int(input("Enter the element to be removed:"))
    Set.discard(discard_element)
    return Set

#Check disjoint set
def disjoint_set(Set):
    Set_new = set()
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
        output = Set.isdisjoint(Set_new)
    return output

#Check Subset
def subset_set(Set):
    Set_new = set()
    number_ele_Set = int(input("Please enter number elements to be available in new Set:"))  
    for element in range(number_ele_Set):
        element_n = int(input("please enter the element: "))
        Set_new.add(element_n)
        output = Set.issubset(Set_new)
    return output
