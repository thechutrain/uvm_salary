import pprint       #to print things pretty
import csv          #to read csv files

from open_cleanfile import open_cleanfile  # imports open_cleanfile function

__author__ = 'alanchu'

################### READ ME #####################
# this function count_positions will accept the master
# list of employees and return a dictionary of the counts of
# unique employee positions, and can have it sorted



def count_positions(employee_list):
    e_pos_dict = {} # dictionary of the employee positions
    try:
        for e in employee_list:
            if (e[1] in e_pos_dict):
                e_pos_dict[e[1]] += 1
            else:
                e_pos_dict[e[1]] = 1
    finally:
        pprint.pprint(e_pos_dict)
        # return e_pos_dict

##### TESTING ######
clean_employee_list = open_cleanfile("uvmSalary15.csv")
count_positions(clean_employee_list)
