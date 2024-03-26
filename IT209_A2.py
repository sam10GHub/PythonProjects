## Assignment: IT209 – ASSIGNMENT 2 (A2)
# Purpose:Student Class Definition
# Name: Samuel Essandoh

class Student:
    totalEnrollment = 0
    def __init__(self, name, major='IST', enrolled='y', credits=0, qpoints=0, g_num=0):
        self.name = name
        self.major = major
        self.enrolled = enrolled
        self.credits = credits
        self.qpoints = qpoints
        self.g_num = g_num
        Student.totalEnrollment += 1  # Increases totalEnrollment each time a new student is created
    def __str__(self):
        return f'{self.name}, {self.major}, active: {self.enrolled}, credits = {self.credits}, gpa = {self.qpoints / self.credits if self.credits > 0 else 0}'

    def gpa(self):
        if self.credits == 0: #This way, if a student has 0 credits, their GPA will be returned as 0 instead of causing a Zero Division Error.
            return 0
        else:
            gpa = self.qpoints/self.credits
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

    def equals(self, student):
        return self.name == student.name and self.major == student.major and self.enrolled == student.enrolled and self.credits == student.credits and self.qpoints == student.qpoints





#test script
input('\nHit "Enter" to create several objects and print their summaries\n')

s1 = Student('Henry Miller', major = 'Hist',
      enrolled = 'y', credits = 0, qpoints = 0)
s2 = Student('Emma Maria Vicente', major = 'Math',
      enrolled = 'y', credits = 90, qpoints = 315)
s3 = Student('A. Einstein', major = 'Phys',
      enrolled = 'y', credits = 0, qpoints = 0)
s4 = Student('W. A. Mozart', major = 'Mus',
      enrolled = 'n', credits = 29, qpoints = 105)
s5 = Student('Emma Maria Vicente', major = 'CSci',
      enrolled = 'y', credits = 60, qpoints = 130)
s5.g_num = s2.g_num
s6 = Student('Vincent Van Gogh', major = 'Art',
      enrolled = 'y', credits = 120, qpoints = 315)
print('\nThe following Student objects were created: \n')
print('s1 = ', s1)
print('s2 = ', s2)
print('s3 = ', s3)
print('s4 = ', s4)
print('s5 = ', s5)
print('s6 = ', s6)
print('\nTotal number of students: ', Student.totalEnrollment)
input('\n\n\n Hit "Enter" to run several tests of the class methods -----------')
print('The gpa of ', s1.name, ' is ', s1.gpa(), '\n')
print('Class standing of ', s4.name, ' is ', s4.classLevel())
print('Class standing of ', s2.name, ' is ', s2.classLevel(), '\n')
if s1.equals(s2):
    print (s1.name, ' and ', s2.name, ' are the same student')
else:
    print (s1.name, ' and ', s2.name, ' are not the same student')
if s2.equals(s5):
    print (s2.name, ' and ', s5.name, ' are the same student')
else:
    print (s2.name, ' and ', s5.name, ' are not the same student\n')
if s1.isActive():
    print (s1.name, ' is currently active')
else:
    print (s1.name, ' is not currently active')
if s4.isActive():
    print (s4.name, ' is currently active')
else:
    print (s4.name, ' is not currently active\n')
print('Adding grade of "A" for ', s4.name, ', result: ', s4.addGrade('A', 3))
print('GPA of ', s4.name,' is now ', s4.gpa())
print('Class standing of ', s4.name, ' is now ', s4.classLevel())
print('\nTrying to add bogus grade of "X" to ', s1.name, ' result: ', s1.addGrade('X', 3))
print('\nEnd of A2 Student class demo')