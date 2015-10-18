############################# IMPORT #############################
import pprint       #to print things pretty
import csv          #to read csv files

__author__ = 'alanchu'


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
#open_cleanfile("uvm_employee_salary_project/uvmSalary15.csv")

############################# DEBUGGING   ########################
# import os
# print "hello world"
# print os.getcwd()
