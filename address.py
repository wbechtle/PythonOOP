#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 2/19/2023
#Project: Address Class
#--------------------------------------------------------------------------------------------
#PROGRAMMING TASK
#-----------------
#"Implement a class Address. An address has a house number, a street, an optional apartment 
#number, a city, a state and a postal code. Define the constructor such that an object can be 
#created in one of two ways: with our without an apartment number. Supply a print method that 
#prints the address with the street on one line and the city, state and postal code on the 
#next line. Supply a method def comesBefore(self, other) that tests whether this address comes 
#before other when compared by postal code. This method should return a boolean value. Develop 
#your class in one file, and create a test file for testing your class."
#--------------------------------------------------------------------------------------------
#UML Class Diagram
#-----------------
#See accompanying UML Class Diagram.
#--------------------------------------------------------------------------------------------
# Create structure for Address class.
class Address:

    # CONSTUCTURE...
    # Initialization for each instance. The constructer uses the validation code within the 
    # setters to reduce code redundancy and valid parameters passed to constructer.
    def __init__(self, house_number, street, city, state, postal_code, apartment_number):
        # Call associated method and pass parameter.
        self.set_house_number(house_number)
        self.set_street(street)
        self.set_apartment_number(apartment_number)
        self.set_city(city)
        self.set_state(state)
        self.set_postal_code(postal_code)

    # SETTERS...

    # Sets the attribute. If empty string, assign 'N\A' value.
    def set_house_number(self, house_number):
        if house_number != '':
            self._house_number = house_number
        else:
            self._house_number = 'N/A'
    def set_street(self, street):
        if street != '':
            self._street = street
        else:
            self._street = 'N/A'
    def set_apartment_number(self, apartment_number):
        if apartment_number != '':
            self._apartment_number = apartment_number
        else:
            self._apartment_number = 'N/A'
    def set_city(self, city):
        if city != '':
            self._city = city
        else:
            self._city = 'N/A'
    def set_state(self, state):
        self._state = state
        if state != '':
            self._state = state
        else:
            self._state = 'N/A'
    def set_postal_code(self, postal_code):
        self._postal_code = postal_code
        if postal_code != '':
            self._postal_code = postal_code
        else:
            self._postal_code = 'N/A'

    # Getters...

    # Returns the associated attribute.
    def get_house_number(self):
        return self._house_number
    def get_street(self):
        return self._street
    def get_apartment_number(self):
        return self._apartment_number
    def get_city(self):
        return self._city
    def get_state(self):
        return self._state
    def get_postal_code(self):
        return self._postal_code

    # PRINT STATEMENT...
    # Prints the address in two line EXAMPLE:
    # 123 Pine St Apt 14
    # Foley, MN 59012
    # Omites APT if none.
    def print_address(self):
        if self._apartment_number != None:
            print(self._house_number, self._street, self._apartment_number)
        else:
            print(self._house_number, self._street)
        print(self._city + ',', self._state, self._postal_code)

    # comes_before method is used to return bolean value pending if the self postal code comes before
    # the other postal code.
    def comes_before(self, other):
        return self._postal_code < other._postal_code