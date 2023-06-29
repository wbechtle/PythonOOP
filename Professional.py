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
# Create structure for Professional class.
class Professional(Employee):

    # CONSTUCTURE...
    # Initialization for each instance. The constructer uses the validation code within the 
    # setters to reduce code redundancy and valid parameters passed to constructer.
    def __init__(self, first, middle, last, date, salary, department, credentials):

        # Call init method of superclass and pass parameter.
        Employee.__init__(self, first, middle, last, date, salary, department)

        # Call the associated method and pass the associated parameter.
        self.set_salary(salary)
        self.set_credentials(credentials)
        
    # SETTERS...

    # Sets the salary attribute. If empty string, assign 'N\A' value.
    def set_salary(self, salary):
        if salary != '':
            self._salary = salary
        else:
            self._salary = 'N/A'

    # Sets the credentials attribute. If empty string, assign 'N\A' value.
    def set_credentials(self, credentials):
        if credentials != '':
            self._credentials = credentials
        else:
            self._credentials = 'N/A'

    # Getters...

    # Returns the salary attribute.
    def get_salary(self):
        return self._salary

    # Returns the credentials attribute.
    def get_credentials(self):
        return self._credentials
    
    # str method.
    def __str__(self):
        unformatted_salary = self.get_salary()
        return f'Name: {Employee.get_full_name(self)}\nCredentials: {self.get_credentials()}\nSalary: \
${unformatted_salary:,d}'
    
    # repr method.
    def __repr__(self):
        first_name = Employee.get_first_name(self)
        middle_initial = Employee.get_middle_initial(self)
        last_name = Employee.get_last_name(self)
        date_of_birth = Employee.get_date_of_birth(self)

        return f'Professional.Professional({first_name}, {middle_initial}, {last_name}, {date_of_birth}, \
{self.get_salary()}, {Employee.get_department(self)}, {self.get_credentials()})'