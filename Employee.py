#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 3/2/2023
#Project: Employee Class (SubClass to person)
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
from person import Person
# Create structure for Employee class.
class Employee(Person):

    # CONSTUCTURE...
    # Initialization for each instance. The constructer uses the validation code within the 
    # setters to reduce code redundancy and valid parameters passed to constructer.
    def __init__(self, first, middle, last, date, salary, department):

        # Call init method of superclass and pass parameter.
        Person.__init__(self, first, middle, last, date)

        # Call the associated method and pass the associated parameter.
        self.set_salary(salary)
        self.set_department(department)
        
    # SETTERS...

    # Sets the salary attribute. If empty string, assign 'N\A' value.
    def set_salary(self, salary):
        if salary != '':
            self._salary = salary
        else:
            self._salary = 'N/A'

    # Sets the department attribute. If empty string, assign 'N\A' value.
    def set_department(self, department):
        if department != '':
            self._department = department
        else:
            self._department = 'N/A'

    # Getters...

    # Returns the salary attribute.
    def get_salary(self):
        return self._salary

    # Returns the department attribute.
    def get_department(self):
        return self._department
    
    # str method.
    def __str__(self):
        unformatted_salary = self.get_salary()
        return f'Name: {Person.get_full_name(self)}\nDepartment: {self.get_department()}\nSalary: \
${unformatted_salary:,d}'
    
    # repr method.
    def __repr__(self):
        first_name = Person.get_first_name(self)
        middle_initial = Person.get_middle_initial(self)
        last_name = Person.get_last_name(self)
        date_of_birth = Person.get_date_of_birth(self)

        return f'Employee.Employee({first_name}, {middle_initial}, {last_name}, {date_of_birth}, \
{self.get_salary()}, {self.get_department()})'