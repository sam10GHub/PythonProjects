# Assignment: IT209 – LAB ASSIGNMENT 3 (LA3)
# Purpose:1.	Protect all attributes from direct “dot notation” access from outside the class
# 2.	Add accessor/mutator (getter/setter) methods to return or change the object’s job_title and annual_salary – return the value for accessor methods and ‘True’ for successful mutator methods.  Also add a getter (accessor) method for name
# 3.	Add an equals method to determine whether an input object is the same as the ‘self’ object.  Equality is assumed when the object parameter is type ‘Employee’, and ‘employee_id’ and ‘name’ are the same for both objects.
# Name: Samuel Essandoh
class Employee:
    def __init__(self, employee_id, name, birth_year, birth_month, job_title, annual_salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__birth_year = birth_year
        self.__birth_month = birth_month
        self.__job_title = job_title
        self.__annual_salary = annual_salary

    # The Employee class is defined with the __init__ method initializing the attributes of the class such as employee_id, name, birth_year, birth_month, job_title, and annual_salary.
    def __str__(self):
        return ("Employee Identification: " + self.__employee_id + "\n"
                + "Name: " + self.__name + "\n"
                + "Year of Birth: " + str(self.__birth_year) + "\n"
                + " Birth Month: " + str(self.__birth_month) + "\n"
                + "Job Title: " + self.__job_title + "\n"
                + "Annual Salary: " + str(self.__annual_salary))

    # Displays a readable version of the Employee object

    def hourly_rate(self):
        return self.__annual_salary / 2028

    # Calculates and returns the employee’s hourly rate of pay – divides salary by 2080

    def age(self):
        import datetime  # this line should be the first executable line in your code
        dateTime = datetime.datetime.now().__str__()
        month = dateTime[5] + dateTime[6]
        year = dateTime[0:4]
        if self.__birth_month < int(month):
            return int(year) - self.__birth_year
        else:
            return int(year) - self.__birth_year - 1

    # Returns the employee’s current age in years: subtracts the employee’s birth year from the current year, but accounts for month differences
    def can_retire(self):
        if self.age() > 70:
            return True
        else:
            return False

    def getName(self):
        return self.__name

    def getJob_title(self):
        return self.__job_title

    def setJob_title(self, newJob):
        self.__job_title = newJob
        return True
    def getAnnual_salary(self):
        return self.__annual_salary
    def setAnnual_salary(self, salary):
        self.__annual_salary = salary
        return True
    def eqEmployee(self, otherObject):
        if not isinstance(otherObject, Employee):
            return False
        return self.__name == otherObject.__name and self.__employee_id == otherObject.__employee_id





# Global Code to test the class definition ----------------------------------------

print('\nStart of Lab 3 Employee class test')
print('\n------------------------------------------------------------------------')
input('Hit "Enter" to run a regression test of existing features from Lab #2')
# The followng are a "regression test" that tests the previous (existing)
# functions of the Employee class that were part of Lab #2.
# The purpose is to show that the new functions didn't break what previously
# worked.
e1 = Employee('E34568', 'David Miller', 1980, 1, 'Accountant', 65000)
e2 = Employee('E22154', 'Margarete Smith', 1972, 10, 'Vice President', 115000)
e3 = Employee('E43344', 'Chase Smedley', 1996, 8, 'Salesman', 75000)
e4 = Employee('E12157', 'Daniel Arledge', 1953, 2, 'Lawyer', 92000)
e5 = Employee('E00001', 'Abe Lincoln', 1940, 2, 'Former POTUS', 10000)
print('\nList of employee objects created: ')
print('e1 = ', e1)
print('e2 = ', e2)
print('e3 = ', e3)
print('e4 = ', e4)
print('e5 = ', e5)
# Various method tests follow, numbered 1 - 8
print('\nTest of various methods follows.....1 - 4 are regression tests\n')
print('\nT1. Hourly rate for ', e1.getName(), ' is ', e1.hourly_rate())
print('\nT2. Age of ', e2.getName(), ' is ', e2.age())
print('\nT3. Age of ', e3.getName(), ' is ', e3.age())
print('\nT4. Retirement eligibility for ', e2.getName(), ' is ', e2.can_retire())
print('\nT5. Retirement eligibility for ', e5.getName(), ' is', e5.can_retire())

# Tests of new Lab#3 features follow.....
print('\n\n\nLab#3 Features tests ---------------------------------------------------')
input('Hit "Enter" to test new features - methods and protection - #5 and above\n')
print('\n\nT6. ', e4.getName(), ' job description is ', e4.getJob_title())
e4.setJob_title('Dentist')
print('\n\t', e4.getName(), ' job description was changed to ', e4.getJob_title())
print('\n\nT6. ', e5.getName(), ' salary is ', e5.getAnnual_salary())
print('\tResetting ', e5.getName(), ' salary. Return value is ', e5.setAnnual_salary(500000))
print('\t', e5.getName(), ' salary was changed to ', e5.getAnnual_salary())
print('\n\nT8.Are ', e1.getName(), ' and ', e5.getName(), ' the same? ', e1.eqEmployee(e5))
e6 = Employee ('E43344', 'Chase Smedley', 1984, 9, 'IT Support', 64000)
print('\n\nT9. Are ', e3.getName(), ' and ', e6.getName(), ' the same? ', e3.eqEmployee(e6))
print('\n\nT10. Try to reset salary of ', e1.getName(), ', currently ', e1.getAnnual_salary())
print('      to 150,000 using direct dot notation (should fail): ')
e1.annual_salary = 150000
print('      Salary after attempted direct reset: ', e1.getAnnual_salary())
print('      Value of new attribute "annual_salary": ', e1.annual_salary)
print('\n   note: Employee ', e1.getName(), ' now has two salary attributes: one protected, one not ')
print('      Only the "__annual_salary" protected attribute is the official one. ')

print('\nEnd of Lab 3 Employee class test')

