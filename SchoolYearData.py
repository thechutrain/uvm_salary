__author__ = 'alanchu'
#  This python file will call multiple functions that I am working on, and
#  test to see that they are working.  This file will also be a sort of coding playground

################# IMPORT #######################
from open_cleanfile import open_cleanfile  # imports open_cleanfile function
from count_positions import count_positions  # imports open_cleanfile function
import matplotlib.pyplot as plt
from sumSalary import sumSalary
import numpy as np
from decimal import Decimal
from re import sub

import pprint
import operator


########### Class #########
class SchoolYearData:
    # employeeMasterList = None  #  Have a master list of each employee
    def __init__(self, yearInt, cleanFileStr):
        self.dataYear = yearInt
        self.cleanFileName = cleanFileStr
        self.employeeMasterList = open_cleanfile(self.cleanFileName)  #  list of e_list
        self.uniquePositions = count_positions(self.employeeMasterList, "d")  # uniquePositions is sorted from highest f; list of tuples
        #simple stats per year
        self.uniquePositionsCount = len(self.uniquePositions)
        self.totalSalary = sumSalary(self.employeeMasterList)
        # self.list_of_EmployeePosition = []  #  this will store all the positions & salaries

    def averageSalary(self):
        return "$" + format(self.totalSalary / len(self.employeeMasterList), '.2f')  #  is a str!! includes unpaid leave staff!!

    def getAllSalariesPosition(self):
        self.dict_Position_listSalaries = {}  ### this contains a Dict of Position vs List_of_salaries
        for i in range(self.uniquePositionsCount):
            position = self.uniquePositions[i][0]  # this gets the name of the position, i index, [0] element is pos.
            # print position
            year = str(self.dataYear)
            # print position + year
            temp_list_salaries = []
            #for loop to go through master list to find all salaries associated with an employement position
            for employee in self.employeeMasterList:
                if (employee[1] == position):  # checks to see if the position for employee matches current position dic
                    if (employee[2] != None):   #  this excludes employees with unpaid leave etc.
                        salary = int(employee[2])
                        # salary = float(employee[2])
                        # salary = "%.2f" % salary  # format the salary so it has .00
                    temp_list_salaries.append(salary)
                else:
                    pass
            self.dict_Position_listSalaries[position] = np.asarray(temp_list_salaries)
            # print type(self.dict_Position_listSalaries[position])
            # break
            # self.dict_Position_listSalaries[position + year] = temp_list_salaries  # to specify year
        return self.dict_Position_listSalaries


    def makeBoxPlot(self):
        dict_of_pos_vs_salaryList = self.getAllSalariesPosition()
        for x in dict_of_pos_vs_salaryList:
            print "this is the box plot for: ", x
            data = dict_of_pos_vs_salaryList[x]
            plt.boxplot(data)
            plt.ylabel("Salary (USD)")
            plt.show()
            break

    def boxPlotAllEmployees(self):
        employee_list = self.employeeMasterList
        employee_total_salary = []  # list of all the salaries of all employees
        for e in employee_list:
            if (e[2] != None):   #  this excludes employees with unpaid leave etc.
                employee_total_salary.append(int(e[2]))
            else:
                pass
        data = np.array(employee_total_salary)
        print "this is the box plot for all employees"
        plt.boxplot(data)
        plt.ylabel("Salary (USD)")
        plt.ylim([0,200000])
        plt.xlabel("All employees hired by UVM")
        plt.show()

       # return np_employee_total_salary
            # print e[2]
            # break

        # for x in self.dict_of_pos_vs_salaryList:
        #     all_salary_np.append(x[1])
        # pprint.pprint(all_salary_np)


    # def makeBoxPlot(self):
    #     for x in self.dict_Position_listSalaries:
    #         print "This is the box plot for: ", x
    #         data = self.dict_Position_listSalaries[x]
    #         plt.boxplot(data)
    #         break


# class EmployeePosition:
#     def __init__(self, yearInt, position):
#         self.dataYear = yearInt
#         self.employeePosition = position
#         self.position_list = []
#     def getAllSalariesPosition(self):




######### TEST ############
e = SchoolYearData(2015, "uvmSalary15.csv")
# e.makeBoxPlot()  # works
# e.boxPlotAllEmployees()
e.boxPlotAllEmployees()

# print "data year of this object: ", e.dataYear
# print "gets data from this clean file: ", e.cleanFileName
# print "total count of employees", e.uniquePositionsCount
# print "get total salaries of all employees at UVM", e.totalSalary
# print "average salary of UVM employee: ", e.averageSalary()
# pprint.pprint(e.getAllSalariesPosition())


# dict_of_pos_vs_salaryList = e.getAllSalariesPosition()
#
# for x in dict_of_pos_vs_salaryList:
#     print "this is the box plot for: ", x
#     data = dict_of_pos_vs_salaryList[x]
#     plt.boxplot(data)
#     plt.ylabel("Salary (USD)")
#     plt.show()
#     break

    #     for x in self.dict_Position_listSalaries:
    #         print "This is the box plot for: ", x
    #         data = self.dict_Position_listSalaries[x]
    #         plt.boxplot(data)
    #         break

# e.makeBoxPlot()



