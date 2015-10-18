__author__ = 'alanchu'
__author__ = 'alanchu'
#  This python file will call multiple functions that I am working on, and
#  test to see that they are working.  This file will also be a sort of coding playground

################# IMPORT #######################
from open_cleanfile import open_cleanfile  # imports open_cleanfile function
from count_positions import count_positions  # imports open_cleanfile function
from decimal import Decimal
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
        self.uniquePositionsCount = len(self.uniquePositions)


######### TEST ############
e = SchoolYearData(2015, "uvmSalary15.csv")
print "data year of this object: ", e.dataYear
print "gets data from this clean file: ", e.cleanFileName
print "Number of unique positions: ", e.uniquePositionsCount