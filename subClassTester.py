#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 3/2/2023
#Project: SubClass Tester (Instructor, Student, Employee, Admin, and Professional)
#--------------------------------------------------------------------------------------------
#PROGRAMMING TASK
#-----------------
#"Supply a separate test program that tests these two classes and all the methods. You must 
#create at least 3 different objects of each class for testing."
#--------------------------------------------------------------------------------------------
#Algorithm
#-----------------
#Step 1) Initialize an instance of each class to verify the constructor functions properly.
#Step 2) Call on all getters to verify the function without error.
#Step 3) Call on all setters to verify they function without error.
#Step 4) Iterate steps 1 - 3 as many times as specified as user.
#--------------------------------------------------------------------------------------------
from Instructor import Instructor
from Student import Student
from Employee import Employee
from Admin import Admin
from Professional import Professional
import random

#CONSTANTS

FIRST_NAME_TUPLE = ('Aaren', 'Aarika', 'Abagail', 'Benedicta', 'Benetta', 'Bennie', 'Carole', 'Caroline',
                'Caroljean', 'Carolyn', 'Caron', 'Carri', 'Christian', 'Cody', 'Darelle',
                'Eda', 'Eddy', 'Edee', 'Edeline', 'EdenFifi', 'Fifine', 'Filia', 'Filippa', 'Fina',)

MIDDLE_INITIAL_TUPLE = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',  'L', 'M', 'N', 'O', 'P',
                    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

LAST_NAME_TUPLE = ('Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez',
                'Fionna', 'Fionnula',  'Fiorenze', 'Fleur', 'Fleurette', 'Ginger', 'Ginnie',
                'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor')

DEGREE_TUPLE = ('PHD', 'MS')

DEPARTMENT_TUPLE = ('CIS', 'CNG', 'CSC')

MAJOR_TUPLE = ('Computer Science', 'Information Science', 'Computer Animation', 'Information System', 
               'Computer Engineering', 'Cybersecurity', 'Software Engineering')

CLASSIFICATION_TUPLE = ('FR', 'SO', 'JR', 'SR')

CREDENTIALS_TUPLE = ('DrPH', 'DNS', 'EdD', 'DNP', 'BS', 'BA', 'AD')

# The display_greeting function is used to display an explanation of the purpose of the program.
# This function uses formatted f string to display a heading.
def display_greeting():
    line_1 = 'This program is used to test the Instuctor, Student, Employee, Admin, and Professional'
    line_2 = 'SubClasses. This program will create one instance of each class as many times as'
    line_3 = 'specified.'
    print()
    print('-' * 90)
    print('|' + f'{"Instuctor, Student, Admin, and Professional SubClass Tester":^88}' + '|')
    print('|' + f'{"Admin and Professional are SubClass of Employee which is a ":^88}' + '|')
    print('|' + f'{"SubClass to person SuperClass.":^88}' + '|')
    print('-' * 90)
    print('|' + f'{line_1:<88}' + '|')
    print('|' + f'{line_2:<88}' + '|')
    print('|' + f'{line_3:<88}' + '|')
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

#The create_object_list function is used to create a list of objects that are instances
#of the Student and Instructor subclass. The functions task is to make as many unique 
#atributes as possible.
def create_object_list():

    #Create object_list to contain each instance of my Person class.
    object_list = []

    #Iterations counts each iteration as an instance. Each iteration = one instance.
    iterations = 0

    #Let the user decide how many instances to create and test.
    max_instances = get_user_input('Enter "0" to quit or enter how many instances to create and test: ')

    #If user does not want to quit.
    if max_instances != 0:
        
        #While loop used to control the count of instances to create and test.
        while iterations < max_instances:

            #Pick a random first, middle, and last name from the NAME_TUPLEs available.
            random_first_name = FIRST_NAME_TUPLE[random.randint(0, len(FIRST_NAME_TUPLE) - 1)]
            random_middle_initial = MIDDLE_INITIAL_TUPLE[random.randint(0, len(MIDDLE_INITIAL_TUPLE) - 1)]
            random_last_name = LAST_NAME_TUPLE[random.randint(0, len(LAST_NAME_TUPLE) - 1)]
            
            #Pick a random date of birth.
            date_of_birth = str(random.randint(1, 12)) + '-' + str(random.randint(1, 28)) + '-' + \
                            str(random.randint(1950, 2007))
            
            #Pick a random salary. 
            random_salary = random.randint(20000, 80000)

            #Pick a random degree and department from the associated tuples available.
            random_degree = DEGREE_TUPLE[random.randint(0, len(DEGREE_TUPLE) - 1)]  
            random_department = DEPARTMENT_TUPLE[random.randint(0, len(DEPARTMENT_TUPLE) - 1)]  
    

            #Initialize a instructor_object and pass the associated parameters.
            instructor_object = Instructor(random_first_name, random_middle_initial, random_last_name, \
                                                  date_of_birth, random_salary, random_degree, random_department)

            #Append the newly created instance to the object list.
            object_list.append(instructor_object)

            #Pick a GPA. 
            random_gpa = random.uniform(1.5, 4.9)

            #Pick a random major and classification from the associated tuples available.
            random_major = MAJOR_TUPLE[random.randint(0, len(MAJOR_TUPLE) - 1)]  
            random_classification = CLASSIFICATION_TUPLE[random.randint(0, len(CLASSIFICATION_TUPLE) - 1)]

            #Pick a random first, middle, and last name from the NAME_TUPLEs available.
            random_first_name = FIRST_NAME_TUPLE[random.randint(0, len(FIRST_NAME_TUPLE) - 1)]
            random_middle_initial = MIDDLE_INITIAL_TUPLE[random.randint(0, len(MIDDLE_INITIAL_TUPLE) - 1)]
            random_last_name = LAST_NAME_TUPLE[random.randint(0, len(LAST_NAME_TUPLE) - 1)]
            
            #Pick a random date of birth.
            date_of_birth = str(random.randint(1, 12)) + '-' + str(random.randint(1, 28)) + '-' + \
                            str(random.randint(1950, 2007))

            #Initialize a student_object and pass the associated parameters.
            student_object = Student(random_first_name, random_middle_initial, random_last_name, \
                                                  date_of_birth, random_major, random_gpa, random_classification)

            #Append the newly created instance to the object list.
            object_list.append(student_object)

            #Pick a random first, middle, and last name from the NAME_TUPLEs available.
            random_first_name = FIRST_NAME_TUPLE[random.randint(0, len(FIRST_NAME_TUPLE) - 1)]
            random_middle_initial = MIDDLE_INITIAL_TUPLE[random.randint(0, len(MIDDLE_INITIAL_TUPLE) - 1)]
            random_last_name = LAST_NAME_TUPLE[random.randint(0, len(LAST_NAME_TUPLE) - 1)]
            
            #Pick a random date of birth.
            date_of_birth = str(random.randint(1, 12)) + '-' + str(random.randint(1, 28)) + '-' + \
                            str(random.randint(1950, 2007))
            
            #Pick a random salary. 
            random_salary = random.randint(20000, 80000)

            #Pick a random department from the associated tuples available.
            random_department = DEPARTMENT_TUPLE[random.randint(0, len(DEPARTMENT_TUPLE) - 1)]  

            #Initialize a employee_object and pass the associated parameters.
            employee_object = Employee(random_first_name, random_middle_initial, random_last_name, \
                                        date_of_birth, random_salary, random_department)

            #Append the newly created instance to the object list.
            object_list.append(employee_object)

            #Pick a random first, middle, and last name from the NAME_TUPLEs available.
            random_first_name = FIRST_NAME_TUPLE[random.randint(0, len(FIRST_NAME_TUPLE) - 1)]
            random_middle_initial = MIDDLE_INITIAL_TUPLE[random.randint(0, len(MIDDLE_INITIAL_TUPLE) - 1)]
            random_last_name = LAST_NAME_TUPLE[random.randint(0, len(LAST_NAME_TUPLE) - 1)]
            
            #Pick a random date of birth.
            date_of_birth = str(random.randint(1, 12)) + '-' + str(random.randint(1, 28)) + '-' + \
                            str(random.randint(1950, 2007))
            
            #Pick a random hourly_salary. 
            random_hourly_salary = random.uniform(20, 70)

            #Pick a random degree and department from the associated tuples available.
            random_reports_to = FIRST_NAME_TUPLE[random.randint(0, len(FIRST_NAME_TUPLE) - 1)]  
            random_department = DEPARTMENT_TUPLE[random.randint(0, len(DEPARTMENT_TUPLE) - 1)]  
    
            #Initialize a admin_object and pass the associated parameters.
            admin_object = Admin(random_first_name, random_middle_initial, random_last_name, date_of_birth, \
                                 random_hourly_salary, random_department, random_reports_to)

            #Append the newly created instance to the object list.
            object_list.append(admin_object)

#Pick a random first, middle, and last name from the NAME_TUPLEs available.
            random_first_name = FIRST_NAME_TUPLE[random.randint(0, len(FIRST_NAME_TUPLE) - 1)]
            random_middle_initial = MIDDLE_INITIAL_TUPLE[random.randint(0, len(MIDDLE_INITIAL_TUPLE) - 1)]
            random_last_name = LAST_NAME_TUPLE[random.randint(0, len(LAST_NAME_TUPLE) - 1)]
            
            #Pick a random date of birth.
            date_of_birth = str(random.randint(1, 12)) + '-' + str(random.randint(1, 28)) + '-' + \
                            str(random.randint(1950, 2007))
            
            #Pick a random salary. 
            random_salary = random.randint(20000, 80000)

            #Pick a random credential and department from the associated tuples available.
            random_credential = CREDENTIALS_TUPLE[random.randint(0, len(CREDENTIALS_TUPLE) - 1)]  
            random_department = DEPARTMENT_TUPLE[random.randint(0, len(DEPARTMENT_TUPLE) - 1)]  
    

            #Initialize a professional_object and pass the associated parameters.
            professional_object = Professional(random_first_name, random_middle_initial, random_last_name, \
                                                  date_of_birth, random_salary, random_department, random_credential)

            #Append the newly created instance to the object list.
            object_list.append(professional_object)

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
    for element in object_list:

        #line variables for formatting and ease of use in future.
        line_1 = f'Testing Object {iterations} ' + str(type(element))
        line_2 = f'Testing SuperClass Getters...'
        line_3 = f'Test Complete.'
        line_4 = f'Testing SubClass Getters...'
        line_5 = f'Testing SuperClass Setters...'
        line_6 = f'Testing SubClass Setters...'
        line_7 = f'Mutated Attributes'

        #Print header.
        print('|' + f'{line_1:^88}' + '|')
        print('-' * 90)

        #Print Testing SuperClass Getters...
        print('|' + f'{line_2:^88}' + '|')
        print('-' * 90)

        #Testing SuperClass Getters...
        print('.get_first_name():', element.get_first_name())
        print('.get_middle_initial():', element.get_middle_initial())
        print('.get_last_name():', element.get_last_name())
        print('.get_full_name():', element.get_full_name())
        print('.get_date_of_birth():', element.get_date_of_birth())

        #Print complete.
        print('-' * 90)
        print('|' + f'{line_3:^88}' + '|')
        print('-' * 90)

        #Print Testing SubClass Getters...
        print('|' + f'{line_4:^88}' + '|')
        print('-' * 90)

        #Testing SubClass Getters...

        #Determine which getters to call(Instuctor, Student, Employee, Admin, or Professional).
        if isinstance(element, Instructor):
            unformatted_salary = element.get_salary()
            print('.get_salary():', f'${unformatted_salary:,d}')
            print('.get_degree():', element.get_degree())
            print('.get_department():', element.get_department())
            print('__str__:\n' + element.__str__())
            print('__repr__:', element.__repr__())

        #Determine which getters to call(Instuctor, Student, Employee, Admin, or Professional).
        elif isinstance(element, Student):
            print('.get_major():', element.get_major())
            print('.get_classification():', element.get_classification())
            unformatted_gpa = element.get_gpa()
            print('.get_gpa():', f'{unformatted_gpa:.2f}')
            print('__str__:\n' + element.__str__())
            print('__repr__:', element.__repr__())

        #Determine which getters to call(Instuctor, Student, Employee, Admin, or Professional).
        elif isinstance(element, Employee):
            unformatted_salary = element.get_salary()
            print('.get_salary():', f'${unformatted_salary:,.2f}')
            print('.get_department():', element.get_department())
            print('__str__:\n' + element.__str__())
            print('__repr__:', element.__repr__())

        #Determine which getters to call(Instuctor, Student, Employee, Admin, or Professional).
        elif isinstance(element, Admin):
            unformatted_salary = element.get_hourly_salary()
            print('.get_hourly_salary():', f'${unformatted_salary:,.2f}')
            print('.get_reports_to():', element.get_reports_to())
            print('__str__:\n' + element.__str__())
            print('__repr__:', element.__repr__())

        #Determine which getters to call(Instuctor, Student, Employee, Admin, or Professional).
        else:
            unformatted_salary = element.get_salary()
            print('.get_salary():', f'${unformatted_salary:,.2f}')
            print('.get_credentials():', element.get_credentials())
            print('__str__:\n' + element.__str__())
            print('__repr__:', element.__repr__())

        #Print complete.
        print('-' * 90)
        print('|' + f'{line_3:^88}' + '|')
        print('-' * 90)

        #Print testing SuperClass Setters...
        print('|' + f'{line_5:^88}' + '|')
        print('-' * 90)

        #Testing SuperClass Setters...
        element.set_first_name(FIRST_NAME_TUPLE[random.randint(0, len(FIRST_NAME_TUPLE) - 1)])
        element.set_middle_initial(MIDDLE_INITIAL_TUPLE[random.randint(0, len(MIDDLE_INITIAL_TUPLE) - 1)])
        element.set_last_name(LAST_NAME_TUPLE[random.randint(0, len(LAST_NAME_TUPLE) - 1)])
        element.set_date_of_birth(str(random.randint(1, 12)) + '-' + str(random.randint(1, 28)) + '-' + \
                                str(random.randint(1950, 2007)))

        #Print Complete.
        print('|' + f'{line_3:^88}' + '|')
        print('-' * 90)

        #Print testing SubClass Setters...
        print('|' + f'{line_6:^88}' + '|')
        print('-' * 90)

        #Testing SubClass Setters...

        #Determine which setters to call(Instuctor, Student, Employee, Admin or Professional).
        if isinstance(element, Instructor):
            element.set_salary(random.randint(20000, 80000))
            element.set_degree(DEGREE_TUPLE[random.randint(0, len(DEGREE_TUPLE) - 1)])
            element.set_department(DEPARTMENT_TUPLE[random.randint(0, len(DEPARTMENT_TUPLE) - 1)])

        #Determine which setters to call(Instuctor, Student, Employee, Admin or Professional).
        elif isinstance(element, Student):
            element.set_major(MAJOR_TUPLE[random.randint(0, len(MAJOR_TUPLE) - 1)])
            element.set_gpa(random.uniform(1.5, 4.9))
            element.set_classification(CLASSIFICATION_TUPLE[random.randint(0, len(CLASSIFICATION_TUPLE) - 1)])

        #Determine which setters to call(Instuctor, Student, Employee, Admin or Professional).
        elif isinstance(element, Employee):
            element.set_salary(random.randint(20000, 80000))
            element.set_department(DEPARTMENT_TUPLE[random.randint(0, len(DEPARTMENT_TUPLE) - 1)])

        #Determine which setters to call(Instuctor, Student, Employee, Admin or Professional).
        elif isinstance(element, Admin):
            element.set_hourly_salary(random.uniform(20, 70))
            element.set_reports_to(FIRST_NAME_TUPLE[random.randint(0, len(FIRST_NAME_TUPLE) - 1)])

        #Determine which setters to call(Instuctor, Student, Employee, Admin or Professional).
        else:
            element.set_salary(random.randint(20000, 80000))
            element.set_credentials(CREDENTIALS_TUPLE[random.randint(0, len(CREDENTIALS_TUPLE) - 1)])

        #Print the string "Mutated attributes".
        print('|' + f'{line_7:^88}' + '|')
        print('-' * 90)

        #Print Mutated attributes.
        print('_first_name:', element.get_first_name())
        print('_middle_name:', element.get_middle_initial())
        print('_last_name:', element.get_last_name())
        print('_date_of_birth:', element.get_date_of_birth())

        #Determine which attributes to print(Instuctor, Student, Employee, Admin or Professional).
        if isinstance(element, Instructor):
            unformatted_salary = element.get_salary()
            print('_salary:', f'${unformatted_salary:,d}')
            print('_degree:', element.get_degree())
            print('_department:', element.get_department())

        #Determine which attributes to print(Instuctor, Student, Employee, Admin or Professional).
        elif isinstance(element, Student):
            print('_major:', element.get_major())
            unformatted_gpa = element.get_gpa()
            print('_gpa:', f'{unformatted_gpa:.2f}')
            print('_classification:', element.get_classification())

        #Determine which attributes to print(Instuctor, Student, Employee, Admin or Professional).
        elif isinstance(element, Employee):
            unformatted_salary = element.get_salary()
            print('_salary:', f'${unformatted_salary:,d}')
            print('_department:', element.get_department())

        #Determine which attributes to print(Instuctor, Student, Employee, Admin or Professional).
        elif isinstance(element, Admin):
            unformatted_salary = element.get_salary()
            print('_salary:', f'${unformatted_salary:,d}')
            print('_reports_to:', element.get_reports_to())

        #Determine which attributes to print(Instuctor, Student, Employee, Admin or Professional).
        else:
            unformatted_salary = element.get_salary()
            print('_salary:', f'${unformatted_salary:,d}')
            print('_degree:', element.get_degree())
            print('_department:', element.get_department())

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