#All Modules
from statistics import mean,median
from list import *
from set import *
from dictionary import *
from tuple import *

import math
import statistics
import json


#All Variables



#All Functions
print("Welcome to Data structure calculator")

print("Please select any operation to proceed \n1.List \n2.Set \n3.Dictionary \n4.Tuple ")

data_input = int(input("please enter a number between 1 and 4: "))

if data_input == 1:
                 print("Welcome to List operations ")
                 print("Create a List for proceeding List Operations")
                 List_main = create_list()
                 print("The created list is ", List_main)
                 while True:
                     print("Please select any one List operation to proceed (Any number between 1-17)")
                     print(" 1. Append \n 2. Pop \n 3. Len \n 4. Sum \n 5. Max \n 6. Min \n 7. Sort \n 8. Mean \n 9. Median \n 10. Frequency \n 11. Insert \n 12. Concatenation \n 13. Reverse \n 14. Slicing \n 15. Clear \n 16. Copy \n 17. Exit" )
                     #input any number for performing list operations
                
                     List_operation_input = int(input("Please enter any one number between 1-17:"))
                     
                     if List_operation_input == 1:
                                        #Perform append operation
                                        output_append = append_list(List_main)
                                        print("The output after append operations is ", output_append)
                     elif List_operation_input == 2:
                                         #Perform pop operation
                                         output_len = pop_list(List_main)
                                         print("The output after pop operations is ", output_len)

                     elif List_operation_input == 3:
                                        #Perform len operation
                                        output_len = len_list(List_main)
                                        print("The output after len operations is ", output_len)

                     elif List_operation_input == 4:
                                         #perform sum operation
                                         output_len = sum_list(List_main)
                                         print("The output after Sum operations is ", output_len)
                     elif List_operation_input == 5:
                                         #perform Max operation
                                         output_len = max_list(List_main)
                                         print("The output after Max operations is ", output_len)
                     elif List_operation_input == 6:
                                         #perform Min operation
                                         output_len = min_list(List_main)
                                         print("The output after Min operations is ", output_len)
                     elif List_operation_input == 7:
                                         #perform sorting
                                         output_len = sort_list(List_main)
                                         print("The output after Sort operations is ", output_len)
                     elif List_operation_input == 8:
                                         output_len = mean_list(List_main)
                                         print("The output after Mean operations is ", output_len)
                     elif List_operation_input == 9:
                                         #Find median
                                         output_len = median_list(List_main)
                                         print("The output after Median operations is ", output_len)
                     elif List_operation_input == 10:
                                         #Find count
                                         output_len = count_list(List_main)
                                         print("The output after Count operations is ", output_len)
                     elif List_operation_input == 11:
                                         #insert an element to the list
                                         output_len = insert_list(List_main)
                                         print("The output after Insert operations is ", output_len)
                     elif List_operation_input == 12:
                                         #Concate list
                                         output_len = concate_list(List_main)
                                         print("The output after Concate operations is ", output_len)
                     elif List_operation_input == 13:
                                         #Reverse a list
                                         output_len = reverse_list(List_main)
                                         print("The output after Reverse operations is ", output_len)
                     elif List_operation_input == 14:
                                         #Slicing
                                         output_len = slice_list(List_main)
                                         print("The output after Slice operations is ", output_len)
                     elif List_operation_input == 15:
                                         #Clear List
                                         output_len = clear_list(List_main)
                                         print("The output after Clear operations is ", output_len)
                     elif List_operation_input == 16:
                                         #Copy list
                                         output_copy = copy_list(List_main)
                                         print("The output after Copy operations is ", output_copy)

                     elif List_operation_input == 17:
                                         break
                     else:
                         print("Invalid Option, Please provide operation numbers again.")
                
elif data_input == 2:
                print("Welcome to Set Operations")
                print("Create a Set for proceeding Set Operations")
                Set_main = create_set()
                print("The created Set is ", Set_main)
                while True:
                    print("Please select any one Set operation to proceed (Any number between 1-19)")
                    print("1. Add \n 2. Update \n 3. Union \n 4. Intersection \n 5. Difference \n 6. Symmetric Difference \n 7. Pop \n 8. Sum \n 9. Max \n 10. Min \n 11. Len \n 12. Intersection Update \n 13. Difference Update \n 14. Symmetric Difference Update \n 15. Clear \n 16. Discard \n 17. Disjoint \n 18. SubSet \n 19. Exit" )
             
                    Set_operation_input = int(input("Please enter any one number between 1-19:"))

                    if Set_operation_input == 1:
                                        #Add element to set
                                        output_add = add_set(Set_main)
                                        print("The output after add operations is ", output_add) 
                    if Set_operation_input == 2:
                                        #Update a set
                                        output_update = update_set(Set_main)
                                        print("The output after update operations is ", output_update) 
    
                    if Set_operation_input == 3:
                                        #Union of sets
                                        output_union = union_set(Set_main)
                                        print("The output after Union operations is ", output_union)
                    if Set_operation_input == 4:
                                        #Intersection of sets
                                        output_intersection = intersection_set(Set_main)
                                        print("The output after Intersection operations is ", output_intersection)
                    if Set_operation_input == 5:
                                        #Difference of sets
                                        output_difference = difference_set(Set_main)
                                        print("The output after Difference operations is ", output_difference)
                    if Set_operation_input == 6:
                                        #Symmetric difference of sets
                                        output_Symdifference = Symmetric_difference_set(Set_main)
                                        print("The output after Symmetric Difference operations is ", output_Symdifference)

                    if Set_operation_input == 7:
                                        #Pop element from set
                                        output_pop = pop_set(Set_main)
                                        print("The output after Pop operations is ", output_pop)
                    if Set_operation_input == 8:
                                        #Summation of set
                                        output_sum = sum_set(Set_main)
                                        print("The output after Sum operations is ", output_sum)
                    if Set_operation_input == 9:
                                        #Find max
                                        output_max = max_set(Set_main)
                                        print("The output after Max operations is ", output_max)
                    if Set_operation_input == 10:
                                        #Find min
                                        output_min = min_set(Set_main)
                                        print("The output after Min operations is ", output_min)
                    if Set_operation_input == 11:
                                        #Find len
                                        output_len = len_set(Set_main)
                                        print("The output after Len operations is ", output_len)
                    if Set_operation_input == 12:
                                        #Intersection update of set
                                        output_intersection_update = intersection_update_set(Set_main)
                                        print("The output after Intersection Update operations is ", output_intersection_update)
                    if Set_operation_input == 13:
                                        #Difference update of set
                                        output_difference_update = difference_update_set(Set_main)
                                        print("The output after Difference Update operations is ", output_difference_update)
                    if Set_operation_input == 14:
                                        #Symmetric difference update of set
                                        output_symmetric_difference_update = symmetric_difference_update_set(Set_main)
                                        print("The output after Symmetric Difference Update operations is ", output_symmetric_difference_update)
                    if Set_operation_input == 15:
                                        #Clear a set
                                        output_clear = clear_set(Set_main)
                                        print("The output after Clear operations is ", output_clear)
                    if Set_operation_input == 16:
                                        #Discard from set
                                        output_discard = discard_set(Set_main)
                                        print("The output after Discard operations is ", output_discard)
                    if Set_operation_input == 17:
                                        #Set disjoint
                                        output_disjoint = disjoint_set(Set_main)
                                        print("The output after Disjoint operations is ", output_disjoint)
                    if Set_operation_input == 18:
                                        #Check Subset
                                        output_subset = subset_set(Set_main)
                                        print("The output after Subset operations is ", output_subset)
                    if Set_operation_input == 19:
                                        break
elif data_input == 3:
                print("Welcome to Dictionary Operations")
                print("Create a Dictionary for proceeding Dictionary Operations")
                Dict_main = create_dict()
                print("The created Dictionary is ", Dict_main)
                while True:
                    print("Please select any one Dictionary operation to proceed (Any number between 1-13)")
                    print(" 1. Insert or Update \n 2. Access \n 3. Get Items \n 4. Get Keys \n 5. Copy Dictionary \n 6. Pop \n 7. Pop Item \n 8. Clear \n 9. Len \n 10. Del \n 11. Get Dictionary Values \n 12. Set Default \n 13. Exit" )
             
                    Dict_operation_input = int(input("Please enter any one number between 1-13:"))

                    if Dict_operation_input == 1:
                                        output_update = update_dict(Dict_main)
                                        print("The output after Update operations is ", output_update)
                    if Dict_operation_input == 2:
                                        output_access = access_dict(Dict_main)
                                        print("The output after Access operations is ", output_access)
                    if Dict_operation_input == 3:
                                        output_items = items_dict(Dict_main)
                                        print("The output after Get Items operations is ", output_items)
                    if Dict_operation_input == 4:
                                        output_keys = keys_dict(Dict_main)
                                        print("The output after Get Keys operations is ", output_keys)
                    if Dict_operation_input == 5:
                                        output_copy = copy_dict(Dict_main)
                                        print("The output after Copy operations is ", output_copy)
                    if Dict_operation_input == 6:
                                        output_pop = pop_dict(Dict_main)
                                        print("The output after Pop operations is ", output_pop)
                    if Dict_operation_input == 7:
                                        output_popItem = popItem_dict(Dict_main)
                                        print("The output after Pop Item operations is ", output_popItem)
                    if Dict_operation_input == 8:
                                        output_clear = clear_dict(Dict_main)
                                        print("The output after Clear operations is ", output_clear)
                    if Dict_operation_input == 9:
                                        output_len = len_dict(Dict_main)
                                        print("The output after Len operations is ", output_len)
                    if Dict_operation_input == 10:
                                        output_del = del_dict(Dict_main)
                                        print("The output after Del operations is ", output_del)
                    if Dict_operation_input == 11:
                                        output_values = check_values(Dict_main)
                                        print("The output after Values operations is ", output_values)
                    if Dict_operation_input == 12:
                                        output_default = setDefault_dict(Dict_main)
                                        print("The output after Set Default operations is ", output_default)

                    if Dict_operation_input == 13:
                                        break

elif data_input == 4:
                print("Welcome to Tuple Operations")
                print("Create a Tuple for proceeding Tuple Operations")
                Tuple_main = create_tuple()
                print("The created Tuple is ", Tuple_main)
                while True:
                    print("Please select any one Tuple operation to proceed (Any number between 1-6)")
                    print(" 1. Count \n 2. Get Index \n 3. Concatenation \n 4. Len \n 5. Del \n 6. Exit " )
                    Tuple_operation_input = int(input("Please enter any one number:"))

                
                    if Tuple_operation_input == 1:
                                        output_count = count_tuple(Tuple_main)
                                        print("The output after Count operations is ", output_count)
                    if Tuple_operation_input == 2:
                                        output_index = index_tuple(Tuple_main)
                                        print("The output after Index operations is ", output_index)
                    if Tuple_operation_input == 3:
                                        output_concate = concate_tuple(Tuple_main)
                                        print("The output after Concatenation operations is ", output_concate)
                    if Tuple_operation_input == 4:
                                        output_len = len_tuple(Tuple_main)
                                        print("The output after Len operations is ", output_len)
                    if Tuple_operation_input == 5:
                                        output_del = del_tuple(Tuple_main)
                                        print("The output after Del operations is ", output_del)
                    if Tuple_operation_input == 6:
                                        break
