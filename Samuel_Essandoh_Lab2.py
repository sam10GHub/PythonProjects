#Assignment: IT209 – LAB ASSIGNMENT 2 (LA2)
# Purpose:Write a Python program to define a class to model the characteristics of a generic employee of some organization.
#Name: Samuel Essandoh
class Employee:
    def __init__(self, employee_id, name, birth_year,birth_month, job_title, annual_salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__birth_year = birth_year
        self.__birth_month = birth_month
        self.__job_title = job_title
        self.__annual_salary = annual_salary
#The Employee class is defined with the __init__ method initializing the attributes of the class such as employee_id, name, birth_year, birth_month, job_title, and annual_salary.
    def __str__(self):
        return ("Employee Identification: " + self.__employee_id + "\n"
            +"Name: " + self.__name + "\n"
            + "Year of Birth: " + str(self.__birth_year)+ "\n"
            + " Birth Month: " + str(self.__birth_month) + "\n"
            + "Job Title: " + self.__job_title + "\n"
            + "Annual Salary: " + str(self.__annual_salary))
#Displays a readable version of the Employee object

    def hourly_rate(self):
        return self.annual_salary/2028
#Calculates and returns the employee’s hourly rate of pay – divides salary by 2080

    def age(self):
        import datetime  # this line should be the first executable line in your code
        dateTime = datetime.datetime.now().__str__()
        month = dateTime[5] + dateTime[6]
        year = dateTime[0:4]
        if self.birth_month < int(month):
            return int(year) - self.__birth_year
        else:
            return int(year) - self.__birth_year - 1
#Returns the employee’s current age in years: subtracts the employee’s birth year from the current year, but accounts for month differences
    def can_retire(self):
        if self.__age() > 70:
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

#If age > 70, returns ‘True’ – employee is eligible to retire.  Otherwise, ‘False’.  Use the self.age() method to retrieve the Employee object’s age.
print('\nStart of Employee class demo')

e1 = Employee('E34568', 'David Miller', 1996, 1, 'Accountant', 82000)
e2 = Employee('E22154', 'Margarete Smith', 1972, 10, 'Vice President', 115000)
e3 = Employee('E43344', 'Chase Snidley', 1992, 8, 'Salesman', 75000)
e4 = Employee('E12157', 'Roone Arledge', 1979, 11, 'Lawyer', 92000)
e5 = Employee('E00001', 'Abe Lincoln', 1940, 2, 'Former POTUS', 85000)

print('e1 = ', e1)
print('e2 = ', e2)
print('e3 = ', e3)
print('e4 = ', e4)
print('e5 = ', e5)
print('Hourly rate for ', e1.name, ' is $', e1.hourly_rate())
print('Age of ', e1.name, ' is ', e1.age())
print('Age of ', e3.name, ' is ', e3.age())
print('Job description of ',e4.name,'is ',e4.job_title)
print('Retirement eligibility for ', e2.name, ' is ', e2.can_retire())
print('Retirement eligibility for ', e5.name, ' is', e5.can_retire())

print('\nEnd of Employee class demo') # End of program
