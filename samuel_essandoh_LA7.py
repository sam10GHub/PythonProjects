# IT209_LA7 Extending the ‘List’ Built-in Class - Lab #7
# Name: Samuel Essandoh
#Purpose:In this assignment you are asked to write a Python program to extend the built-in ‘List’ class by
#creating a derived class called ‘USPresidents’ that inherits from the built-in Python List class.


presidents = [[1789, 'Washington', 'None', 'Virginia'],
              [1797, 'Adams', 'Federalist', 'Massachusetts'],
              [1801, 'Jefferson', 'Democratic-Republican', 'Virginia'],
              [1809, 'Madison', 'Democratic-Republican', 'Virginia'],
              [1817, 'Monroe', 'Democratic-Republican', 'Virginia'],
              [1825, 'Quincy Adams', 'Democratic-Republican', 'Massachusetts'],
              [1829, 'Jackson', 'Democrat', 'Tennessee'],
              [1837, 'Van Buren', 'Democrat', 'New York'],
              [1841, 'Harrison', 'Whig', 'Virginia'],  # died after 1 month in office
              [1841, 'Tyler', 'Whig', 'Virginia'],  # finished Harrison's term
              [1845, 'Polk', 'Democrat', 'Tennessee'],
              [1849, 'Taylor', 'Whig', 'Kentucky'],
              [1853, 'Pierce', 'Democrat', 'New Hampshire'],
              [1857, 'Buchanan', 'Democrat', 'Pennsylvania'],
              [1861, 'Lincoln', 'Republican', 'Illinois'],
              [1865, 'Lincoln', 'Republican', 'Illinois'],  # assasinated 4/1865
              [1865, 'Johnson', 'National Union', 'Tennessee'],  # finished Lincoln's term
              [1869, 'Grant', 'Republican', 'Ohio'],
              [1877, 'Hayes', 'Republican', 'Ohio'],
              [1881, 'Garfield', 'Republican', 'Ohio'],  # assasinated 1881
              [1881, 'Arthur', 'Republican', 'Vermont'],  # finished Garfield's term
              [1885, 'Cleveland', 'Democrat', 'New Jersey'],
              [1889, 'Harrison', 'Republican', 'Ohio'],
              [1893, 'Cleveland', 'Republican', 'Ohio'],
              [1897, 'McKinley', 'Republican', 'Ohio'],
              [1901, 'McKinley', 'Republican', 'Ohio'],  # assasinated 1901
              [1901, 'Roosevelt', 'Republican', 'New York'],  # finished McKinley's term
              [1909, 'Taft', 'Republican', 'Ohio'],
              [1913, 'Wilson', 'Democrat', 'Virginia'],
              [1921, 'Harding', 'Republican', 'Ohio'],
              [1925, 'Coolidge', 'Republican', 'Massachusetts'],
              [1929, 'Hoover', 'Republican', 'Iowa'],
              [1933, 'Roosevelt', 'Democrat', 'New York'],  # died in office 4/1945
              [1945, 'Roosevelt', 'Democrat', 'New York'],  # died in office 4/1945
              [1945, 'Truman', 'Democrat', 'Missouri'],  # finished FDR's term
              [1953, 'Eisenhower', 'Republican', 'Kansas'],
              [1961, 'Kennedy', 'Democrat', 'Massachusetts'],
              [1963, 'Kennedy', 'Democrat', 'Massachusetts'],  # assasinated 11/22/1963
              [1963, 'Johnson', 'Democrat', 'Texas'],  # finished Kennedy's term
              [1969, 'Nixon', 'Republican', 'California'],
              [1974, 'Nixon', 'Republican', 'California'],  # resigned 8/1974
              [1974, 'Ford', 'Republican', 'Michigan'],  # finished Nixon's term 8/1974
              [1977, 'Carter', 'Democrat', 'Georgia'],
              [1981, 'Reagan', 'Republican', 'California'],
              [1989, 'Bush', 'Republican', 'Texas'],
              [1993, 'Clinton', 'Democrat', 'Arkansas'],
              [2001, 'Bush', 'Republican', 'Texas'],
              [2009, 'Obama', 'Democrat', 'Illinois'],
              [2017, 'Trump', 'Republican', 'New York'],
              [2021, 'Biden', 'Democrat', 'Delaware']]


# creating class for list
class USPresidents(list):
    def __init__(self, inlist):
        super().__init__(inlist)
        self.currentYear = 2024

    def whoWasPrez(self, year):
        if not 1789 <= year <= self.currentYear:
            return 'Error: Year out of range'
        return ', '.join(prez[1] for prez in self if prez[0] == year)

    def partyCount(self):
        party_counts = [0, 0, 0]
        for prez in self:
            if prez[2] == 'Democrat':
                party_counts[0] += 1
            elif prez[2] == 'Republican':
                party_counts[1] += 1
            else:
                party_counts[2] += 1
        return tuple(party_counts)

    def stateList(self, state):
        return list(set(prez[1] for prez in self if prez[3] == state))




PL = USPresidents(presidents)

# Should return 63:
print('T1. Size of list (should be 50): ', len(PL), '\n')

# Should return 'Biden':
input('\nHit "Enter" to run T2. Most recent president: ')
print(PL[-1][1])

# Should return 'Lincoln':
prez = PL.whoWasPrez(1861)
input('\nHit "Enter" to run T3. President who took office in 1861: ')
print(prez)

# Should return 'Harrison, Tyler'
prez = PL.whoWasPrez(1841)
input('\nHit "Enter" to run T4. Presidents in 1841, should be Harrison and Tyler: ')
print(prez)

# Should return 'Roosevelt and McKinley'
prez = PL.whoWasPrez(1901)
input('\nHit "Enter" to run T5. Presidents in 1901, should be McKinley and Roosevelt: ')
print(prez)

# Should return 'Roosevelt, Truman'
prez = PL.whoWasPrez(1945)
input('\nHit "Enter" to run T6. Presidents in 1945, should be Roosevelt and Truman: ')
print(prez)

# Should return 'Biden':
prez = PL.whoWasPrez(2023)
input('\nT7. President who was in office in 2023: ')
print(prez)

# Should display an 'out of range' error:
input('\nHit ""Enter" to run T8. President who was in office in 1788: ')
print(PL.whoWasPrez(1788))

# Should display three counts, Dems, Repubs, Other:
input('\nHit "Enter" to run T9. Number of presidents in the various parties (17, 23, 10)')
result = PL.partyCount()
print('\tT9. Democrats:   ', result[0])
print('\tT9. Republicans: ', result[1])
print('\tT9. Other:       ', result[2])

# Should display seven presidents from Virginia in a list:
print('\nHit "Enter" to run T10. List of presidents from Virginia (should be 7): \n')
pList = PL.stateList('Virginia')
print(pList)

print('\nEnd of Lab #7 Test')
