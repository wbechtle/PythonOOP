#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 3/2/2023
#Project: Student Class (SubClass of Person Class)
#--------------------------------------------------------------------------------------------
#PROGRAMMING TASK
#-----------------
#"Using your Person class from a previous assignment as a superclass. If your Person class 
#had errors, correct them prior to using it for this project. Make two classes, Student and 
#Instructor, that inherit from Person.  A student has a major, a GPA and classification (FR, 
#SO, JR, SR) and an instructor has a salary, degree (PhD, MS) and department (CIS, CNG, CSC)."
#--------------------------------------------------------------------------------------------
#UML Class Diagram
#-----------------
#See accompanying UML Class Diagram.
#--------------------------------------------------------------------------------------------
from person import Person
# Create structure for Student class.
class Student(Person):

    # CONSTUCTURE...
    # Initialization for each instance. The constructer uses the validation code within the 
    # setters to reduce code redundancy and valid parameters passed to constructer.
    def __init__(self, first, middle, last, date, major, gpa, classification):

        # Call init method of superclass and pass parameter.
        Person.__init__(self, first, middle, last, date)

        # Call the associated method and pass the associated parameter.
        self.set_major(major)
        self.set_gpa(gpa)
        self.set_classification(classification)

    # SETTERS...

    # Sets the attribute. If empty string, assign 'N\A' value.
    def set_major(self, major):
        if major != '':
            self._major = major
        else:
            self._major = 'N/A'

    def set_gpa(self, gpa):
        if gpa != '':
            self._gpa = gpa
        else:
            self._gpa = 'N/A'

    def set_classification(self, classification):
        if classification != '':
            self._classification = classification
        else:
            self._classification = 'N/A'

    # Getters...

    # Returns the associated attribute.
    def get_major(self):
        return self._major

    def get_gpa(self):
        return self._gpa

    def get_classification(self):
        return self._classification

    # str method.
    def __str__(self):
        unformatted_gpa = self.get_gpa()
        return f'Name: {Person.get_full_name(self)}\ngpa: {unformatted_gpa:.2f}\nclassification: \
{self.get_classification()}\nmajor: {self.get_major()}'
    
    # repr method.
    def __repr__(self):
        first_name = Person.get_first_name(self)
        middle_initial = Person.get_middle_initial(self)
        last_name = Person.get_last_name(self)
        date_of_birth = Person.get_date_of_birth(self)
        unformatted_gpa = self.get_gpa()

        return f'Student.Student({first_name}, {middle_initial}, {last_name}, \
{date_of_birth}, {self.get_major()}, {unformatted_gpa:.2f}, {self.get_classification()})'