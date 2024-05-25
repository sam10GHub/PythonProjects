## Assignment: IT209 – ASSIGNMENT 6 (A6)
# Purpose:Department/Person/Student/Faculty Classes and  Student/Faculty Polymorphism
# Name: Samuel Essandoh

class Person:
    personCount = 0
    currentYear = 2022

    def __init__(self, name, address, telephone, email):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.email = email
        Person.personCount += 1

    def __str__(self):
        return f'Person: {self.g_num} {self.name} {self.address}'

    def equals(self, other_person):
        return self.name == other_person.name and self.g_num == other_person.g_num

    def updateCurrentYear(self, newYear):
        self.currentYear = newYear

class Student(Person):
    totalEnrollment = 0
    def __init__(self, name, address, telephone, email, major='IST', enrolled='y', credits=0, qpoints=0):
        super().__init__(name, address, telephone, email)
        self.major = major
        self.enrolled = enrolled
        self.credits = credits
        self.qpoints = qpoints
        self.g_num = "G" + str(Person.personCount).zfill(4 - len(str(Person.personCount)))

        Student.totalEnrollment += 1  # Increases totalEnrollment each time a new student is created

    def __str__(self):
        return f'{self.name}, {self.major}, active: {self.enrolled}, credits = {self.credits}, gpa = {self.qpoints / self.credits if self.credits > 0 else 0}'

    def gpa(self):
        if self.credits == 0:  # This way, if a student has 0 credits, their GPA will be returned as 0 instead of causing a Zero Division Error.
            return 0
        else:
            gpa = self.qpoints / self.credits
            return gpa

    def addGrade(self, letter_grade, num_credits):
        if letter_grade in ['A', 'B', 'C', 'D', 'F'] and 0 <= num_credits <= 4:
            grade_values = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
            self.credits += num_credits
            self.qpoints += grade_values[letter_grade] * num_credits
            return True
        else:
            return False

    def isActive(self):
        if self.enrolled == 'y' or self.enrolled == 'Y':
            return True
        else:
            return False

    def classLevel(self):
        if self.credits >= 90:
            return 'Senior'
        elif self.credits >= 60:
            return 'Junior'
        elif self.credits >= 30:
            return 'Sophomore'
        else:
            return 'Freshman'

    def setMajor(self, newMajor):  # Department provides its d_code as parameter
        self.major = newMajor
        return True

    def equals(self, student):
        return self.name == student.name and self.major == student.major and self.enrolled == student.enrolled and self.credits == student.credits and self.qpoints == student.qpoints


    def case_summary(self):
        return f"Summary:{self.name} is a student at GMU, with g-number {self.g_num}\\nThey are a {self.classLevel()} majoring in {self.major}\\nTheir gpa is {self.gpa()} and they are currently {'enrolled' if self.isActive() else 'not enrolled'}"

    def activate(self):
        self.enrolled = 'y'

    def deactivate(self):
        self.enrolled = 'n'

    def getStatus(self):
        return f"{self.name} is {'enrolled' if self.isActive() else 'not enrolled'} and they are a {self.classLevel()}"

class Faculty(Person):
    def __init__(self, name, address, telephone, email, rank, active, teach_load, specialty, yearStarted):
        super().__init__(name, address, telephone, email)
        self.rank = rank
        self.active = active
        self.teach_load = teach_load
        self.specialty = specialty
        self.yearStarted = yearStarted

    def __str__(self):
        return f'{self.name}, {self.rank}, {self.specialty}, {self.yearStarted}'

    def tenure(self):
        return self.currentYear - self.yearStarted


    def case_summary(self):
        return f"Summary:{self.name} is a faculty member at GMU with g-number {self.g_num}\\nTheir rank is {self.rank} specializing in {self.specialty}\\nTheir teaching load is {self.teach_load} credit hours per year"

    def activate(self):
        self.active = 'y'

    def deactivate(self):
        self.active = 'n'

    def getStatus(self):
        return f"{self.name} is {'active' if self.isActive() else 'not active'} and their rank is {self.rank}"

class Department:
    def __init__(self, d_code, d_name, capacity, minGPA):
        self.d_code = d_code
        self.d_name = d_name
        self.capacity = capacity
        self.minGPA = minGPA
        self.univ_students = 0
        self.avgGPA = 0.0
        self.directory = []

    def add(self, person_object):
        if isinstance(person_object, Student):
            return self.addStudent(person_object)
        elif isinstance(person_object, Faculty):
            return self.addFaculty(person_object)

    def addFaculty(self, faculty_object):
        if isinstance(faculty_object, Faculty):
            self.directory.append(faculty_object)

    def addStudent(self, student_object):
        if self.isQualified(student_object) and len(self.directory) < self.capacity:
            self.directory.append(student_object)
            self.univ_students += 1
            student_list = []
            for students in self.directory:
                if isinstance(student_object, Student):
                    student_list.append(student_object)
            self.avgGPA = sum([student.gpa() for student in self.directory if isinstance(student, Student)]) / len(student_list)
            return True, "Student successfully added."
        else:
            return False, "Failed to add student."

    def isQualified(self, student_object):
        return student_object.gpa() >= self.minGPA and student_object.isActive()

    def listRoster(self, rosterType="b"):
        if rosterType == 's':
            print([student.case_summary() for student in self.directory if isinstance(student, Student)])
        elif rosterType == 'f':
            print([faculty.case_summary() for faculty in self.directory if isinstance(faculty, Faculty)])
        elif rosterType == 'b':
            print([person.case_summary() for person in self.directory])



class Person:
    personCount = 0
    currentYear = 2022

    def __init__(self, name, address, telephone, email):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.email = email
        Person.personCount += 1

    def __str__(self):
        return f'Person: {self.name} {self.address}'

class Student(Person):
    totalEnrollment = 0

    def __init__(self, name, address, telephone, email, major='IST', enrolled='y', credits=0, qpoints=0):
        super().__init__(name, address, telephone, email)
        self.major = major
        self.enrolled = enrolled
        self.credits = credits
        self.qpoints = qpoints
        self.g_num = "G" + str(Person.personCount).zfill(4 - len(str(Person.personCount)))
        Student.totalEnrollment += 1

    def __str__(self):
        return f'{self.name}, {self.major}, active: {self.enrolled}, credits = {self.credits}, gpa = {self.qpoints / self.credits if self.credits > 0 else 0}'


    def gpa(self):
        if self.credits == 0:  # This way, if a student has 0 credits, their GPA will be returned as 0 instead of causing a Zero Division Error.
            return 0
        else:
            gpa = self.qpoints / self.credits
            return gpa

    def addGrade(self, letter_grade, num_credits):
        if letter_grade in ['A', 'B', 'C', 'D', 'F'] and 0 <= num_credits <= 4:
            grade_values = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
            self.credits += num_credits
            self.qpoints += grade_values[letter_grade] * num_credits
            return True
        else:
            return False

    def isActive(self):
        if self.enrolled == 'y' or self.enrolled == 'Y':
            return True
        else:
            return False

    def classLevel(self):
        if self.credits >= 90:
            return 'Senior'
        elif self.credits >= 60:
            return 'Junior'
        elif self.credits >= 30:
            return 'Sophomore'
        else:
            return 'Freshman'

    def setMajor(self, newMajor):  # Department provides its d_code as parameter
        self.major = newMajor
        return True

    def equals(self, student):
        return self.name == student.name and self.major == student.major and self.enrolled == student.enrolled and self.credits == student.credits and self.qpoints == student.qpoints


    def case_summary(self):
        return f"Summary:{self.name} is a student at GMU, with g-number {self.g_num}\n\nThey are a {self.classLevel()} majoring in {self.major}\n\nTheir gpa is {self.gpa()} and they are currently {'enrolled' if self.isActive() else 'not enrolled'}"

    def activate(self):
        self.enrolled = 'y'

    def deactivate(self):
        self.enrolled = 'n'

    def getStatus(self):
        return f"{self.name} is {'enrolled' if self.isActive() else 'not enrolled'} and they are a {self.classLevel()}"


class Faculty(Person):
    def __init__(self, name, address, telephone, email, rank, active, teach_load, specialty, yearStarted):
        super().__init__(name, address, telephone, email)
        self.rank = rank
        self.active = active
        self.teach_load = teach_load
        self.specialty = specialty
        self.yearStarted = yearStarted
        self.g_num = "G" + str(Person.personCount).zfill(4 - len(str(Person.personCount)))

    def __str__(self):
        return f'{self.name}, {self.rank}, {self.specialty}, {self.yearStarted}'


    def tenure(self):
        return self.currentYear - self.yearStarted

    def isActive(self):
        if self.active == 'y' or self.active == 'Y':
            return True
        else:
            return False


    def case_summary(self):
        return f"Summary:{self.name} is a faculty member at GMU with g-number {self.g_num} \n\n Their rank is {self.rank} specializing in {self.specialty}  \n\nTheir teaching load is {self.teach_load} credit hours per year"

    def activate(self):
        self.active = 'y'

    def deactivate(self):
        self.active = 'n'

    def getStatus(self):
        return f"{self.name} is {'active' if self.active == 'y' else 'not active'} and their rank is {self.rank}"

class Department:

    def __init__(self, d_code, d_name, capacity, minGPA):
        self.d_code = d_code
        self.d_name = d_name
        self.capacity = capacity
        self.minGPA = minGPA
        self.univ_students = 0
        self.avgGPA = 0.0
        self.directory = []

    def add(self, person_object):
        if isinstance(person_object, Student):
            return self.addStudent(person_object)
        elif isinstance(person_object, Faculty):
            return self.addFaculty(person_object)

    def addFaculty(self, faculty_object):
        if isinstance(faculty_object, Faculty):
            self.directory.append(faculty_object)

    def addStudent(self, student_object):
        if self.isQualified(student_object) and len(self.directory) < self.capacity:
            self.directory.append(student_object)
            self.univ_students += 1
            student_list = []
            for students in self.directory:
                if isinstance(student_object, Student):
                    student_list.append(student_object)
            self.avgGPA = sum([student.gpa() for student in self.directory if isinstance(student, Student)]) / len(student_list)
            return True, "Student successfully added."
        else:
            return False, "Failed to add student."

    def isQualified(self, student_object):
        return student_object.gpa() >= self.minGPA and student_object.isActive()

    def listRoster(self, rosterType="b"):
        if rosterType == 's':
            print([student.case_summary() for student in self.directory if isinstance(student, Student)])
        elif rosterType == 'f':
            print([faculty.case_summary() for faculty in self.directory if isinstance(faculty, Faculty)])
        elif rosterType == 'b':
            print([person.case_summary() for person in self.directory if
                   isinstance(person, Student) or isinstance(person, Faculty)])


print('\nStart of A6 test script *****************************\n')
print('\nTest 1.  Creating 7 Student objects, 3 Faculty objects, ')
print(' and one Department object - Engineering - for use in this testscript.')
print('---------------------------------------------------------------------------')
s1 = Student('David Miller', '321 Maple Lane, Vienna, VA',
      '571-285-4567', 'dmiller8@gmu.edu',major = 'Hist', enrolled = 'y',
      credits = 30, qpoints = 90)
s2 = Student('Bonnie Bonilla', '123 Oak Street, Potomac, MD',
      '301-285-4567', 'bbonilla@gmu.edu',major = 'Math',enrolled = 'y',
      credits = 90, qpoints = 315)
s3 = Student('Chris Squire', '4567 Park Lane, London, UK',
      '425-285-4567', 'csquire8@gmu.edu', major = 'Musc', enrolled = 'y',
      credits = 45, qpoints = 160)
s4 = Student('Tal Wilkenfeld', '423 Outback Way, Sydney, AU',
      '524-485-5674', 'twilkenfeld@AU.gov', major = 'Musc', enrolled = 'y',
      credits = 75, qpoints = 250)
s5 = Student('Geddy Lee', '1240 Pacific Road, Loa Angeles, CA',
      '231-44-2596', 'grahamcentralsta@gmail.com', major = 'CHHS', enrolled = 'y',
      credits = 105, qpoints = 320)
s6 = Student('John Entwistle', '6 Stable Way, Leeds, UK',
      '416-223-1967', 'johnwho@apple.com', major = 'CSci', enrolled = 'y',
      credits = 15, qpoints = 45)
s7 = Student('John Entwistle', '6 Stable Way, Leeds, UK',
      '416-223-1967', 'johnwho@apple.com', major = 'CSci', enrolled = 'y',
      credits = 15, qpoints = 48)
s8 = Student('Tim Bogert', '423 Outback Way, Sydney, AU',
      '524-485-5674', 'twilkenfeld@AU.gov', major = 'Musc', enrolled = 'y',
      credits = 75, qpoints = 250)
f1 = Faculty('Amanda Shuman', '3062 Covington Street, Fairfax, VA',
             '571-235-2345', 'ashuman@gmu.edu', 'Assistant Professor', 'y',
             18, 'teaching', 2017)
f2 = Faculty('A. Einstein', '2741 University Blvd, Priceton, NJ',
             '212-346-3456', 'aeinstein@gmu.edu', 'Professor', 'y',
             6, 'research', 1938)

d1 = Department('ENGR', 'Engineering', 6, 3.0)
d1.add(Faculty('Alan Turing', '6 Stable Way, Bletchly Park, U.K.',
             '9-56-4955', 'aturing@UK.gov', 'Associate Professor', 'y',
             6, 'research', 1943))

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)
print(f1)
print(f2)
print('Faculty #3 is Alan Turing\n')
print(d1)

print('\n\n\nTest 2.  After "Enter": 4 students, 3 faculty in Engineering Dept.: ')
input('---------------------------------------------------------------------------------\n')
d1.add(s1)
d1.add(s2)
d1.add(s3)
d1.add(s4)
d1.add(f1)
d1.add(f2)
d1.listRoster()

print('\n\n\nTest 3.  Hit "Enter" to add 5th student plus attempt to add one dupe to Engineering Dept.: ')
input('---------------------------------------------------------------------------------\n')
print(d1.add(s6))
s7.g_num = s6.g_num
print(d1.add(s7))
d1.listRoster()

print('\n\n\nTest 4.  Hit "Enter" to add 6th, attempt to add 7th student, will fail: over capacity: ')
input('----------------------------------------------------------------------------------\n')
print(d1.add(s5))
print(d1.add(s8))


#--------------------------------------------------------------------------------------------
input('\n\n\nTest 5.  Hit "Enter" to see Engineering Dept. Student case summaries - 6 students: ')
print('---------------------------------------------------------------------------------\n')
d1.listRoster('s')

#--------------------------------------------------------------------------------------------
input('\n\n\nTest 6.  Hit "Enter" to see Engineering Dept. All case summaries - 6 students and 3 faculty: ')
print('---------------------------------------------------------------------------------\n')
d1.listRoster('b')

#--------------------------------------------------------------------------------------------
input('\n\n\nTest 8.  Hit "Enter" to deactivate  '+ s1.name + ' and ' + f2.name)
print('---------------------------------------------------------------------------------\n')
print(s1.name, ' current status is ', s1.getStatus())
print(f2.name, ' current status is ', f2.getStatus())
print(s1.name, ' deactivation result: ', s1.deactivate())
print(f2.name, ' deactivation result: ', f2.deactivate())
print(s1.name, ' updated status is ', s1.getStatus())
print(f2.name, ' updated status is ', f2.getStatus())

#--------------------------------------------------------------------------------------------
input('\n\n\nTest 9.  Hit "Enter" to activate  ' + s1.name)
print('---------------------------------------------------------------------------\n')
print(s1.name, ' activation result: ', s1.activate())

print('\n\n\n***** End of A6 test **********')

