#local copy

import pprint       #  to print things pretty
import operator     #  used to sort the dictionary

from open_cleanfile import open_cleanfile  # imports open_cleanfile function

__author__ = 'alanchu'

################### READ ME #####################
# this function count_positions will accept the master
# list of employees and return a dictionary of the counts of
# unique employee positions, and can have it sorted
# first parameter = list of employees
# second parameter = A or D (assending or descending)
# RETURNS: sorted list of positions



def count_positions(employee_list, order):
    e_pos_dict = {} # dictionary of the employee positions
    sorted_e_pos_list = None
    try:
        for e in employee_list:
            if (e[1] in e_pos_dict):
                e_pos_dict[e[1]] += 1
            else:
                e_pos_dict[e[1]] = 1
        # See if user wants the list sorted by ascending or descending order
        user_choice = order[0].upper()
        if (user_choice == "A"):
            sorted_e_pos_list = sorted(e_pos_dict.items(), key=operator.itemgetter(1), reverse=False)
        elif (user_choice == "D"):
            sorted_e_pos_list = sorted(e_pos_dict.items(), key=operator.itemgetter(1), reverse=True)
        else:
            print "Please enter either 'A' or 'D' as the second argument in count_positions to get the positions sorted "
    finally:
        return sorted_e_pos_list
        # pprint.pprint(sorted_e_pos_list)
        # return e_pos_dict

##### TESTING ######
clean_employee_list = open_cleanfile("uvmSalary15.csv")
sorted_position_list = count_positions(clean_employee_list, "a")
# see how many unique positions there are
# print type(sorted_position_list)
print "This is how many unique positions of employement there are at UVM: ", len(sorted_position_list)
