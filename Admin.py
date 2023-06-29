#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 2/15/2023
#Project: Employee Class (SubClass to Employee)
#--------------------------------------------------------------------------------------------
#PROGRAMMING TASK
#-----------------
#"Create an additional subclass "Employee" with a department and a salary variable. Then create 
#2 subclasses of Employee, 1 named "Admin" and the other "Professional". The Professional Class 
#will have a credential variable while the Admin Class will have a "reports to" variable showing 
#the name of direct supervisor of the employee. Both the Professional Class and the Admin Class 
#will have their own implementation of the salary. The Professional is a straight salary while 
#the Admin is hourly. Make sure to thoroughly test your implementation with your driver 
#(test program)."
#--------------------------------------------------------------------------------------------
#UML Class Diagram
#-----------------
#See accompanying UML Class Diagram.
#--------------------------------------------------------------------------------------------
from Employee import Employee
# Create structure for Admine class.
class Admin(Employee):

    # CONSTUCTURE...
    # Initialization for each instance. The constructer uses the validation code within the 
    # setters to reduce code redundancy and valid parameters passed to constructer.
    def __init__(self, first, middle, last, date, hourly_salary, department, reports_to):

        # Call init method of superclass and pass parameter.
        Employee.__init__(self, first, middle, last, date, hourly_salary, department)

        # Call the associated method and pass the associated parameter.
        self.set_hourly_salary(hourly_salary)
        self.set_reports_to(reports_to)
        
    # SETTERS...

    # Sets the hourly_salary attribute. If empty string, assign 'N\A' value.
    def set_hourly_salary(self, hourly_salary):
        if hourly_salary != '':
            self._hourly_salary = hourly_salary
        else:
            self._hourly_salary = 'N/A'

    # Sets the reports_to attribute. If empty string, assign 'N\A' value.
    def set_reports_to(self, reports_to):
        if reports_to != '':
            self._reports_to = reports_to
        else:
            self._reports_to = 'N/A'

    # Getters...

    # Returns the hourly_salary attribute.
    def get_hourly_salary(self):
        return self._hourly_salary

    # Returns the reports_to attribute.
    def get_reports_to(self):
        return self._reports_to
    
    # str method.
    def __str__(self):
        unformatted_hourly_salary = self.get_hourly_salary()
        return f'Name: {Employee.get_full_name(self)}\nreports_to: {self.get_reports_to()}\nhourly_Salary: $\
{unformatted_hourly_salary:.2f}'
    
    # repr method.
    def __repr__(self):
        first_name = Employee.get_first_name(self)
        middle_initial = Employee.get_middle_initial(self)
        last_name = Employee.get_last_name(self)
        date_of_birth = Employee.get_date_of_birth(self)
        unformatted_hourly_salary = self.get_hourly_salary()

        return f'Admin.Admin({first_name}, {middle_initial}, {last_name}, {date_of_birth}, \
{unformatted_hourly_salary:.2f}, {Employee.get_department(self)}, {self.get_reports_to()})'