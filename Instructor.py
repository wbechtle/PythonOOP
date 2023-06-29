#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 3/2/2023
#Project: Instructor Class (SubClass of Person Class)
#--------------------------------------------------------------------------------------------
#PROGRAMMING TASK
#-----------------
#"Using your Person class from a previous assignment as a superclass. If your Person class had 
#errors, correct them prior to using it for this project. Make two classes, Student and 
#Instructor, that inherit from Person.  A student has a major, a GPA and classification (FR, 
#SO, JR, SR) and an instructor has a salary, degree (PhD, MS) and department (CIS, CNG, CSC)."
#--------------------------------------------------------------------------------------------
#UML Class Diagram
#-----------------
#See accompanying UML Class Diagram.
#--------------------------------------------------------------------------------------------
from person import Person
# Create structure for Instructor class.
class Instructor(Person):

    # CONSTUCTURE...
    # Initialization for each instance. The constructer uses the validation code within the 
    # setters to reduce code redundancy and valid parameters passed to constructer.
    def __init__(self, first, middle, last, date, salary, degree, department):

        # Call init method of superclass and pass parameter.
        Person.__init__(self, first, middle, last, date)

        # Call the associated method and pass the associated parameter.
        self.set_salary(salary)
        self.set_degree(degree)
        self.set_department(department)

    # SETTERS...

    # Sets the attribute. If empty string, assign 'N\A' value.
    def set_salary(self, salary):
        if salary != '':
            self._salary = salary
        else:
            self._salary = 'N/A'

    def set_degree(self, degree):
        if degree != '':
            self._degree = degree
        else:
            self._degree = 'N/A'

    def set_department(self, department):
        if department != '':
            self._department = department
        else:
            self._department = 'N/A'

    # Getters...

    # Returns the associated attribute.
    def get_salary(self):
        return self._salary

    def get_degree(self):
        return self._degree

    def get_department(self):
        return self._department

    # str method.
    def __str__(self):
        unformatted_salary = self.get_salary()
        return f'Name: {Person.get_full_name(self)}\nDegree: {self.get_degree()}\nDepartment: \
{self.get_department()}\nSalary: ${unformatted_salary:,d}'
    
    # repr method.
    def __repr__(self):
        first_name = Person.get_first_name(self)
        middle_initial = Person.get_middle_initial(self)
        last_name = Person.get_last_name(self)
        date_of_birth = Person.get_date_of_birth(self)

        return f'Instructor.Instructor({first_name}, {middle_initial}, {last_name}, \
{date_of_birth}, {self.get_salary()}, {self.get_degree()}, {self.get_department()})'