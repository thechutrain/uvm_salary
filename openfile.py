__author__ = 'alanchu'
#
# This function opens new file and cleans the
# data and returns a list containing employee name, salaries, position

############################# DEBUGGING   ###################################
# import os
# print "hello world"
# print os.getcwd()

############################# IMPORT #############################
import pprint       #to print things pretty
import csv          #to read csv files

def open_cleanfile(filename):
    #f = open(filename, 'rU')
    try: #see if you can open file/if file exists
        f = open(filename, 'rU')
        reader = csv.reader(f)
        e = [] #temporary employee row, holds employee data
        try:
            for row in reader: #each row is a 3-element list
                if (row[1]==""):
                    print row[1]
                else:
                    print row
                    print type(row)
                    break
        finally: #assumes you opened the finally, b/c no IOError, so close file!
            f.close()
    except IOError:
        print "file not found - please check if the file exists"

##### TESTING ######
# call function
#something different

open_cleanfile("uvm_employee_salary_project/uvmSalary15.csv") #getting error, b/c this file isn't in uvmemployee_salary_project
