############################# IMPORT #############################
import pprint       #to print things pretty
import sys          #  to determine what version python is running
import csv          #to read csv files
from decimal import Decimal
from re import sub

__author__ = 'alanchu'

########## NEXT STEP #################
#  save each employee data as a tuple??

# This function opens new file and cleans the
# data and returns a list containing employee name, salaries, position

############################# FUNCTION  #############################

def open_cleanfile(filename):
    employee_list = [] #  master row of all employees
    try:  # see if you can open file/if file exists
        f = open(filename, 'rU')
        reader = csv.reader(f)
        try:
            for row in reader:  # each row is a 3-element list of one employee
                e = []  # temporary employee row, holds employee data
                for i in row:
                    e.append(i)
                try:
                    e[2] = Decimal(sub(r'[^\d.]', '', e[2]))
                except:
                    e[2] = None #  for unpaid leave employees
                employee_list.append(e)  # add employee row data to master list of all employees
        finally:  # assumes you opened the finally, b/c no IOError, so close file!
            # pprint.pprint(employee_list)
            f.close()
    except IOError:
        print "file not found - please check if the file exists"
    return employee_list

##### TESTING ######
# call function

# pprint.pprint(open_cleanfile("uvm_employee_salary_project/uvmSalary15.csv"))  # this file in wrong directory, can't change!
employee_list = open_cleanfile("uvm_employee_salary_project/uvmSalary15.csv")
# for e in employee_list:
#     if (e[2] == None):
#         print e[0]

# pprint.pprint(employee_list)

############################# DEBUGGING   ########################
# import os
# print "hello world"
# print os.getcwd()
# print (sys.version)
