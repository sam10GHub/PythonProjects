## Assignment: IT209 – ASSIGNMENT 5 (A5)
# Purpose:Department/Person/Student/Faculty Classes
# Name: Samuel Essandoh



class Person:
    personCount = 0
    currentYear = 2022  # set as per requirement

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

    def setMajor(self, newMajor):  # Note: Department provides its d_code as parameter
        self.major = newMajor
        return True

    def equals(self, student):
        return self.name == student.name and self.major == student.major and self.enrolled == student.enrolled and self.credits == student.credits and self.qpoints == student.qpoints

        # ... rest of Student methods ...


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


class Department:
    def __init__(self, d_code, d_name, capacity, minGPA):
        self.d_code = d_code
        self.d_name = d_name
        self.capacity = capacity
        self.minGPA = minGPA
        self.univ_students = 0
        self.avgGPA = 0.0
        self.directory = []

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


            print([str(student) for student in self.directory if isinstance(student, Student)])
        elif rosterType == 'f':
            print([str(faculty) for faculty in self.directory if isinstance(faculty, Student)])
        elif rosterType == 'b':
            print([str(person) for person in self.directory])

print('\nStart of A5 Test Script ********************************')

#====================================================================
input('\nTest1. Hit "Enter" to create 16 student, 2 Faculty objects for use in the demo ')

s1 = Student('David Miller', '321 Maple Lane, Vienna, VA',
      '571-285-4567', 'dmiller8@gmu.edu',major = 'Hist', enrolled = 'y',
      credits = 30, qpoints = 90)
s2 = Student('Emma Maria Vicente', '53A Sautier Str, Burke, VA',
      '571-235-7911', 'emvicente@aol.com', major = 'Math',
      enrolled = 'y', credits = 90, qpoints = 315)
s3 = Student('Chris Squire', '4567 Park Lane, London, UK',
      '425-285-4567', 'csquire8@gmu.edu', major = 'Musc', enrolled = 'y',
      credits = 45, qpoints = 160)
s4 = Student('Tal Wilkenfeld', '423 Outback Way, Sydney, AU',
      '524-485-5674', 'twilkenfeld@AU.gov', major = 'Musc', enrolled = 'y',
      credits = 75, qpoints = 250)
s5 = Student('Larry Graham', '66 pacific Coast Hwy, Los Angeles, CA',
      '231-44-2596', 'dholland@jazz.net', major = 'CHHS', enrolled = 'y',
      credits = 105, qpoints = 320)
s6 = Student('Dave Holland', '6 Stable Way, Leeds, UK',
      '416-223-1967', 'johnwho@apple.com', major = 'CSci', enrolled = 'y',
      credits = 15, qpoints = 35)
s7 = Student('Esperanza Spalding', '9122 King Hwy, Upper Marlboror, MD',
      '310-247-1954', 'esperanza@jazzy.org', major = 'ENGR', enrolled = 'y',
      credits = 65, qpoints = 250)
s8 = Student('Tim Bogert', '2713 Santa Monica Blvd, Venice, CA',
      '912-333-1968', 'vfudge@yahoo.net', major = 'Hist', enrolled = 'y',
      credits = 45, qpoints = 160)
s9 = Student('Gordon Sumner', '145 Nigel Path, Manchester, U.K.',
      '011-11-0203-2202', 'sting@police.com', major = 'Musc', enrolled = 'y',
      credits = 15, qpoints = 45)
s10 = Student('Paul McCartney', '422 Hagis Road, Edinburgh, U.K.',
      '481-221-1970', 'paullinda@wings.org', major = 'ARTS', enrolled = 'y',
      credits = 110, qpoints = 275)
s11 = Student('Tin Weymouth', '2215 Yonge Street, Toronto, CA',
      '416-676-2983', 'esmythe12@ontario.gov', major = 'ENGR', enrolled = 'y',
      credits = 85, qpoints = 250)
s12 = Student('John McVie', '27 Casino Lane, Monte Carlo, Monaco',
      '011-56-2233-9945', 'johnmac@blues.net', major = 'Hist', enrolled = 'y',
      credits = 45, qpoints = 120)
s13 = Student('Nawt Enrolled', '13 Failed Street, Cantenroll, AZ',
      '320-445-2938', 'nenrolled@gmu.ed', major = 'Hist', enrolled = 'n',
      credits = 45, qpoints = 120)
s14 = Student('Toolow G. Peyay', '1313 LowGrade Drive, Mustwait, NE',
      '678-901-2345','Toolowgpa@gmu.edu', major = 'Undc', enrolled = 'y',
      credits = 20, qpoints = 38)
s15 = Student('Stanley Clark', '13 Main St., Blandon, PA',
              '610-926-4987', 'sclarke@verizon.net', major = 'Chem', enrolled = 'y',
              credits = 95, qpoints = 295)
s16 = Student('Geddy Lee', '251 Younge St., Toronto, Ont',
              '416-221-1131', 'glee@gmail.com', major = 'Chem',enrolled = 'y',
              credits = 58, qpoints = 143)
f1 = Faculty('Paul Shuman', '3062 Covington Street, Fairfax, VA',
             '571-235-2345', 'pshuman@gmu.edu', 'Assistant Professor', 'y',
             18, 'teaching', 2017)
f2 = Faculty('A. Einstein', '2741 University Blvd, Priceton, NJ',
             '212-346-3456', 'aeinstein@gmu.edu', 'Professor', 'y',
             6, 'research', 1938)

print('\nList of Students anf aculty created----------------------------:\n ')
print('s1=  ',s1)
print('s2=  ',s2)
print('s3=  ',s3)
print('s4=  ',s4)
print('s5=  ',s5)
print('s6=  ',s6)
print('s7=  ',s7)
print('s8=  ',s8)
print('s9=  ', s9)
print('s10= ',s10)
print('s11= ',s11)
print('s12= ',s12)
print('s13= ',s13)
print('s14= ',s14)
print('s15= ', s15)
print('s16= ', s16)
print('f1=  ', f1)
print('f2=  ', f2)

#==================================================================================
input('\n\nTest2. Hit "Enter" to see the list of 3 Department objects created ')
print('\n\nDepartments established---------------------------------:')
d1 = Department('ENGR', 'Engineering', 5, 3.0)
d2 = Department('ARTS', 'Art and Architecture', 5, 2.5)
d3 = Department('CHHS', 'College of Health and Human Sevrices', 3, 2.75)
d4 = Department('Hist', 'History Department', 5, 2.50)

print(d1)
print(d2)
print(d3)
print(d4)

#========================================================================================
input('\n\n\nTest3. Hit "Enter" to add s1 - s5, f1, f2 to ENGR Department- print student list\n')
d1.addStudent(s1)
d1.addStudent(s2)
d1.addStudent(s3)
d1.addStudent(s4)
d1.addStudent(s5)
d1.addFaculty(f1)
d1.addFaculty(f2)
d1.listRoster()

#==========================================================================================
print('\n\n\nTest4. Hit "Enter" to create+add  Turing and Von Neuman to ARTS and CHHS faculty,')
input('     then display their rosters:\n')
d2.addFaculty(Faculty('Alan Turing', '6 Stable Way, Bletchly Park, U.K.',
             '9-56-4955', 'aturing@UK.gov', 'Associate Professor', 'y',
             6, 'research', 1943))
d3.addFaculty(Faculty('J. Von Neuman', '71 Kovaletch Prad, Budapest, Hungary',
             '9-56-4955', 'hvneuman@gmail.com', 'Professor', 'y',
             6, 'research', 1948))
d2.listRoster()
d3.listRoster()

#==========================================================================================
input('\n\n\n\nTest5. Hit "Enter" to add additional students to various departments ---------:')
a, b = d1.addStudent(s6)
print('\nAttempting to add ', s6.name, ' to ', d1.d_code, '.  Should fail: over capacity.  Result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
print('\nDepartment ', d1.d_name, ' student list is now: ')
d1.listRoster()

#=========================================================================================
input('\n\n\n\nTest6. Hit "Enter" to add two students to the ARTS Department ')
a, b = d2.addStudent(s6)
print('\nAttempting to add ', s6.name, ' to ', d2.d_code, '.  Should fail: low GPA. Result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
a, b = d2.addStudent(s7)
print('\nAttempting to add ', s7.name, ' to ', d2.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
d2.listRoster()

#========================================================================================
input('\n\n\n\nTest7. Hit "Enter" to add two students to the CHHS Department' )
a, b = d3.addStudent(s8)
print('\nAttempting to add ', s8.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
a, b = d3.addStudent(s9)
print('\nAttempting to add ', s9.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
d3.listRoster()

#=========================================================================================
input('\n\n\n\nTest8. Hit "Enter" to try adding a student with low GPA to CHHS')
a, b = d3.addStudent(s14)
print('\nAttempting to add ', s14.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)

#=========================================================================================
input('\n\n\n\nTest9. Hit "Enter" to try to add a non-enrolled student to the CHHS Department')
a, b = d2.addStudent(s13)
print('\nAttempting to add ', s13.name, ' to ', d2.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)

#========================================================================================
input('\n\n\n\nTest10. Hit "Enter" to try adding a duplicate student ')
a, b = d3.addStudent(s8)
print('\nAttempting to add ', s8.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)

#========================================================================================
input('\n\n\n\nTest11. Hit "Enter" to add s10 to ENGR, s11 to ARTS, s12 to CHHS.')
print('  then print all 3 department student lists')
a, b = d1.addStudent(s10)
print('\nAttempting to add ', s10.name, ' to ', d1.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
a, b = d2.addStudent(s11)
print('\nAttempting to add ', s11.name, ' to ', d2.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
a, b = d3.addStudent(s12)
print('\nAttempting to add ', s12.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)

#=========================================================================================
print('\n\n\n\nTest12. Hit "Enter" to try to add s16, ' + s16.name + ', to ' + d2.d_name)
input('    which will fail for low gpa, which is ' + str(round(s16.gpa(), 2)))
print('\nProfile of Student ' + s16.name + ': ')
print(s16)
a, b = d2.addStudent(s16)
print('\nResult of attempt to add ', s16.name, ' gpa: ', str(round(s16.gpa(),2)), ' to ', d2.d_code)
print('\tis ', a, ', with reson code: ', b)

#==========================================================================================
print('\n\n\n\nTest13. Adding 3 credit course with grade of "A" to ' + s16.name )
input('    which raises the GPA and also moves him up a class level' )
s16.addGrade("A", 3)
print('\nStudent profile is now: ', s16)

#==========================================================================================
input('\n\n\n\nTest14.  Attempt to add ' + s16.name + ' to ' + d2.d_name + ' again')
a, b = d2.addStudent(s16)
print('\nResult of second attempt to add ', s16.name, ' to ', d2.d_code)
print('\tis ', a, ', with reason code:  ', b)
print('\nNote: ', s16.name, ' is now a ', s16.classLevel(), ' with gpa ', str(round(s16.gpa(),2)))

#==========================================================================================
input ('\n\n\n\nTest15.  Hit "Enter" to see the final list of students and faculty for all departments')

d1.listRoster('s')
d1.listRoster('f')
d2.listRoster('s')
d2.listRoster('f')
d3.listRoster('s')
d3.listRoster('f')

print('\n\n\n***** End of A5 S24 Output **********')


