__author__ = 'alanchu'
#  This python file will call multiple functions that I am working on, and
#  test to see that they are working.  This file will also be a sort of coding playground

################# IMPORT #######################
from open_cleanfile import open_cleanfile  # imports open_cleanfile function
from count_positions import count_positions  # imports open_cleanfile function
from sumSalary import sumSalary
from decimal import Decimal
from re import sub

import pprint
import operator


########### Class #########
class SchoolYearData:
    # employeeMasterList = None  #  Have a master list of each employee
    def __init__(self, yearInt,cleanFileStr):
        self.dataYear = yearInt
        self.cleanFileName = cleanFileStr
        self.employeeMasterList = open_cleanfile(self.cleanFileName)  #  list of e_list
        self.uniquePositions = count_positions(self.employeeMasterList, "d")  # uniquePositions is sorted from highest f; list of tuples
        #simple stats per year
        self.uniquePositionsCount = len(self.uniquePositions)
        self.totalSalary = sumSalary(self.employeeMasterList)
    def averageSalary(self):
        return "$" + format(self.totalSalary / len(self.employeeMasterList), '.2f')  #  is a str!! includes unpaid leave staff!!
    # def convertDecimalObject(self):
    #     self.convertedEmployeeList_Decimals = []
    #     for employee in self.employeeMasterList:
    #         temp_list = []
    #         temp_list.append(employee[0])
    #         temp_list.append(employee[1])
    #         value = Decimal(sub(r'[^\d.]', '', employee[2]))
    #         temp_list.append(value)



######### TEST ############
e = SchoolYearData(2015, "uvmSalary15.csv")
print "data year of this object: ", e.dataYear
print "gets data from this clean file: ", e.cleanFileName
print "total count of employees", e.uniquePositionsCount
print "get total salaries of all employees at UVM", e.totalSalary
print "average salary of UVM employee: ", e.averageSalary()

