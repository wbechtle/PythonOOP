#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 2/19/2023
#Project: Address Class Tester
#--------------------------------------------------------------------------------------------
#PROGRAMMING TASK
#-----------------
#"Create a test file for testing your class."
#--------------------------------------------------------------------------------------------
#Algorithm
#-----------------
#Step 1) Display welcome and program greeting.
#Step 2) Initialize an instance of the address class to verify the constructor functions properly.
#Step 3) Call on all getters to verify the function without error.
#Step 4) Call the print method and comes_before to verify they function without error.
#Step 5) Call on all setters to verify they function without error.
#Step 6) Iterate steps 1 - 4 as many times as specified as user.
#Step 7) Display good-bye.
#--------------------------------------------------------------------------------------------
import address
import random

#CONSTANTS

SMALLEST_POSSIBLE_POSTAL_CODE = 1

LARGEST_POSSIBLE_POSTAL_CODE = 99950

HOUSE_NUMBER_TUPLE = (4310, 8994, 14, 125, 3549, 19700, 160, 294, 1055, 39270, 3575, 1354, 613, 4601, 3309)

APARTMENT_NUMBER_TUPLE = ('Apt 310', 'Apt 94', 'Apt 14', 'Apt 125', 'Apt 49', 'Apt 97', 'Apt 160', 'Apt 294',
                'Apt 55', 'Apt 270', 'Apt 575', 'Apt 54', 'Apt 13', 'Apt 1', 'Apt 3309', None, None, None,
                None, None, None, None, None, None, None, None, None, None, None, None)

STREET_TUPLE = ('Isle Of Pines Dr', 'Alderson Ave', 'Patuxent Pl', 'W Rice Ave', 'Fourth St', 'Hancock St', 
            'Bryant Irvin Rd', 'E Anaheim St', 'Ottawa Ave', '17th St', 'Clarks Ferry Rd', 'E Lassen Ave',
            'Heatherbrook Dr', 'Audubon Rd', 'W Moyamensing Ave', '57th Ave SW', 'Hawthorn Hill Ct')

CITY_TUPLE = ('Aberdeen', 'Albany', 'Amarillo', 'Barnstable', 'Bellevue', 'Cedar Rapids', 'Coral Springs', 
            'Clearwater', 'Clarksville', 'Philadelphia', 'Pittsburgh',  'New York City', 'Madison', 
            'Grand Rapids', 'Green Bay', 'Denver', 'Phoenix', 'Panama City', 'Miami', 'Little Rock', 
            'Kalamazoo', 'Fort Collins', 'Duluth', 'Detroit')

STATE_TUPLE = ('AL', 'AZ', 'CA', 'CO', 'DE', 'FL', 'GA', ' ID', 'IL', 'IA', 'KS', 'MN',  'WY', 'MO', 'TX', 'WA', 'WI')

# The display_greeting function is used to display an explanation of the purpose of the program.
# This function uses formatted f string to display a heading.
def display_greeting():
    line_1 = 'This program is used to test the Address class contained inside of "address.py".'
    print()
    print('-' * 90)
    print('|' + f'{"Address Class Tester":^88}' + '|')
    print('-' * 90)
    print('|' + f'{line_1:<88}' + '|')
    print('-' * 90)

#The get_user_input function is used to get input and validate it.
def get_user_input(title):

    # Set flag variable to True.
    not_done = True

    # While loop used to iterate input validation.
    while not_done:

        # Prompt user to enter a valid input.
        user_input = input(title)

        # Print statement for esthetics.
        print('-' * 90)
            
        # If the input is not empty string and greater than or equal to 0, exit while loop.
        if user_input != '' and int(user_input) >= 0:

            # Assign not_done False.
            not_done = False

        # If input is string or negative value, display error.
        else:
            print('ERROR. No empty strings or negative values. Please re-enter.')
            print('-' * 90)

    # Return valid user input.
    return int(user_input)

#The create_object_list function is used to create a list of objects that are all instances
#of the same class. The functions task is to make as many unique atributes as possible.
def create_object_list():

    #Create object_list to contain each instance of a class.
    object_list = []

    #Iterations counts each iteration as an instance. Each iteration = one instance.
    iterations = 0

    #Let the user decide how many instances to create and test.
    max_instances = get_user_input('Enter "0" to quit or enter how many instances to create and test: ')

    #If user does not want to quit.
    if max_instances != 0:
        
        #While loop used to control the count of instances to create and test.
        while iterations < (max_instances + 1):

            #Pick a random values in the associatted tuples or valid range.
            random_house_number = HOUSE_NUMBER_TUPLE[random.randint(0, len(HOUSE_NUMBER_TUPLE) - 1)]
            random_street = STREET_TUPLE[random.randint(0, len(STREET_TUPLE) - 1)]
            random_apartment_number = APARTMENT_NUMBER_TUPLE[random.randint(0, len(APARTMENT_NUMBER_TUPLE) - 1)]
            random_city = CITY_TUPLE[random.randint(0, len(CITY_TUPLE) - 1)]
            random_state = STATE_TUPLE[random.randint(0, len(STATE_TUPLE) - 1)]
            random_postal_code = random.randint(SMALLEST_POSSIBLE_POSTAL_CODE, LARGEST_POSSIBLE_POSTAL_CODE)
            
            #Initialize an object and pass the associated parameters.
            address_object = address.Address(random_house_number, random_street, random_city, random_state, 
                                            random_postal_code, random_apartment_number)

            #Append the newly created instance to the object list.
            object_list.append(address_object)

            #Add one to the iterations.
            iterations += 1

        #Call test_objects_inside_list_display_results function.
        test_objects_inside_list_display_results(object_list)

#The test_objects_inside_list_display_results iterates through the list of objects, while testing each element.
#This function displays the results to the screen.
def test_objects_inside_list_display_results(object_list):

    #Iterations used to keep count of how many objects are inside the list and which one is currently
    #being tested.
    iterations = 1

    #For loop is used to iterate through the list of objects, while testing each element.
    for element in (object_list):

        # if not last element iterate again.
        if iterations != len(object_list):

            #line variables for formatting and ease of use in future.
            line_1 = f'Testing Object {iterations}'
            line_2 = f'Testing Getters...'
            line_3 = f'Test Complete.'
            line_4 = f'Testing Print Statement and Comes Before method'
            line_5 = f'Testing Setters...'
            line_6 = f'Mutated Attributes'

            #Print header.
            print('|' + f'{line_1:^88}' + '|')
            print('-' * 90)

            #Print Testing Getters...
            print('|' + f'{line_2:^88}' + '|')
            print('-' * 90)

            #Testing Getters...
            print('.get_house_number():', element.get_house_number())
            print('.get_street():', element.get_street())
            print('.get_apartment_number():', element.get_apartment_number())
            print('.get_city():', element.get_city())
            print('.get_state():', element.get_state())
            print('.get_postal_code():', element.get_postal_code())

            #Print complete.
            print('-' * 90)
            print('|' + f'{line_3:^88}' + '|')
            print('-' * 90)

            #Print testing Print Statement and comes_before method.
            print('|' + f'{line_4:^88}' + '|')
            print('-' * 90)

            #Create a variable to compare postal codes.
            next_element = object_list[iterations]

            #Call print_address method and comes_before method to verify they function properly.
            element.print_address()
            print('\nComes Before\n')
            next_element.print_address()
            print('\nThis is ', end = '')
            print(element.comes_before(next_element))


            #Print complete.
            print('-' * 90)
            print('|' + f'{line_3:^88}' + '|')
            print('-' * 90)

            #Print testing Setters...
            print('|' + f'{line_5:^88}' + '|')
            print('-' * 90)

            #Testing Setters...
            element.set_house_number(HOUSE_NUMBER_TUPLE[random.randint(0, len(HOUSE_NUMBER_TUPLE) - 1)])
            element.set_street(STREET_TUPLE[random.randint(0, len(STREET_TUPLE) - 1)])
            element.set_apartment_number(APARTMENT_NUMBER_TUPLE[random.randint(0, len(APARTMENT_NUMBER_TUPLE) - 1)])
            element.set_city(CITY_TUPLE[random.randint(0, len(CITY_TUPLE) - 1)])
            element.set_state(STATE_TUPLE[random.randint(0, len(STATE_TUPLE) - 1)])
            element.set_postal_code(random.randint(SMALLEST_POSSIBLE_POSTAL_CODE, LARGEST_POSSIBLE_POSTAL_CODE))
            
            #Print Complete.
            print('|' + f'{line_3:^88}' + '|')
            print('-' * 90)

            #Print the string "Mutated attributes".
            print('|' + f'{line_6:^88}' + '|')
            print('-' * 90)

            #Print Mutated attributes.
            print('_house_number:', element.get_house_number())
            print('_street:', element.get_street())
            print('_apartment_number:', element.get_apartment_number())
            print('_city:', element.get_city())
            print('_state:', element.get_state())
            print('_postal_code:', element.get_postal_code())
            print('-' * 90)

            #Add one to iterations.
            iterations += 1

# The display_good_bye_message is used to display good bye to the screen.
def display_good_bye_message():
    print('|' + f'{"Good-Bye!":^88}' + '|')
    print('-' * 90)

# The main function is used to call all function needed to complete the programming task.
def main():
    display_greeting()
    create_object_list()
    display_good_bye_message()

# If program loaded as main, run main function.
if __name__ == '__main__':
    main()