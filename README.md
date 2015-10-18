# uvm_salary
The purpose of this project is to look at the raw salaries of UVM employees and to compare the trend over a 15+ year span.
As part of my first real data science project, I am hoping to learn a lot about python's visual tools & working with larger
data sets. Thanks for stopping by!

# Work Flow
1.) Data cleaning of all school files <br />
2.) open_clean file - returns a master list of employees (name, position, salary) <br />
3.) count_positions  # returns a sorted list of the all the employee positions <br />
4*.) Create a class for EmployeePosition (flds: name, count, type, salary_list) <br />
5.) Create class schoolYearData (flds: year_of_data, raw_file_link, clean_file_link, unique_position,
list_of_fEmployeePosition_objects) <br />