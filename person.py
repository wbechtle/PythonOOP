#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 2/15/2023
#Project: Person Class (SuperClass to Instructor, Student, Employee, Admin, and Professional)
#--------------------------------------------------------------------------------------------
#PROGRAMMING TASK
#-----------------
#"Create a Person class for storing the following instance variable data: a persons first name, 
#middle initial, last name, and date of birth. Using PowerPoint, draw a UML class diagram of 
#your person class prior to creating your program. Create a set and get for each instance 
#variable. Also, create a method to return the person's full name, which is the first name, 
#middle initial and last name concatenated together. Name this file person.py For date of birth, 
#you may utilize the Python class datetime. You'll need to read about that class here: 
#https://docs.python.org/3/library/datetime.html This will help you understand classes, and 
#use a class interface."
#--------------------------------------------------------------------------------------------
#UML Class Diagram
#-----------------
#See accompanying UML Class Diagram.
#--------------------------------------------------------------------------------------------

# Create structure for Person class.
class Person:

    # CONSTUCTURE...
    # Initialization for each instance. The constructer uses the validation code within the 
    # setters to reduce code redundancy and valid parameters passed to constructer.
    def __init__(self, first, middle, last, date):

        # Call set_first_name method and pass parameter.
        self.set_first_name(first)

        # Call set_middle_initial method and pass parameter.
        self.set_middle_initial(middle)

        # Call set_last_name method and pass parameter.
        self.set_last_name(last)

        # Call set_date_of_birth method and pass parameter.
        self.set_date_of_birth(date)
        
    # SETTERS...

    # Sets the first name attribute. If empty string, assign 'N\A' value.
    def set_first_name(self, first):
        if first != '':
            self._first_name = first
        else:
            self._first_name = 'N/A'

    # Sets the middle initial attribute. If empty string, assign 'N\A' value.
    def set_middle_initial(self,middle):
        if middle != '':
            self._middle_initial = middle
        else:
            self._middle_initial = 'N/A'

    # Sets the last name attribute. If empty string, assign 'N\A' value.
    def set_last_name(self,last):
        if last != '':
            self._last_name = last
        else:
            self._last_name = 'N/A'

    # Sets the date of birth attribute. If empty string, assign 'N\A' value.
    def set_date_of_birth(self,date):
        if date != '':
            self._date_of_birth = date
        else:
            self._date_of_birth = 'N/A'

    # Getters...

    # Returns the first name attribute.
    def get_first_name(self):
        return self._first_name

    # Returns the middle initial attribute.
    def get_middle_initial(self):
        return self._middle_initial

    # Returns the last name attribute.
    def get_last_name(self):
        return self._last_name

    # Returns the persons full name.
    def get_full_name(self):
        return str(self._first_name) + ' ' + str(self._middle_initial) + ' ' + str(self._last_name)

    # Returns the date of birth attribute.
    def get_date_of_birth(self):
        return self._date_of_birth
    
    # str method.
    def __str__(self):
        return f'Name: {self.get_full_name()}\nDate of Birth: {self.get_date_of_birth()}'
    
    # repr method.
    def __repr__(self):
        first_name = self.get_first_name()
        middle_initial = self.get_middle_initial()
        last_name = self.get_last_name()
        date_of_birth = self.get_date_of_birth()

        return f'person.Person({first_name}, {middle_initial}, {last_name}, {date_of_birth})'