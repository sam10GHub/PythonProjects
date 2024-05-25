# Program: Assignment 7 Police Call Report Analytics
# Purpose: This program analyzes police call report data to provide insights on crime incidents.
# Author: Samuel Essandoh

print("Start of Program\n\n\n")
csv_file = r"C:\\Users\\sessa\\Downloads\\CrimeReports.csv"

# Initialize an empty list to store the data
data = []

# Read the CSV file
with open(csv_file, "r") as file:
    for line in file:
        # Split the line by comma
        row = line.strip().split(",")
        data.append(row)

# Print the data
for row in data:
    print(row)

# Define the FCPDCrime class
class FCPDCrime(list):
    def __init__(self, name):
        self.name = name

    def load(self, csv_file):
        data = []
        with open(csv_file, "r") as file:
            for line in file:
                row = line.strip().split(",")
                data.append(row)
        self.extend(data)  # Load data into the FCPDCrime object

    def printCrimes(self, start=0, end=None, zips=None):
        """
        This method prints the crimes in the data from the start to end indices.
        If zips is specified, only crimes in those zip codes will be printed.
        """
        end = end if end else len(self)
        if zips is None:
            for i in range(start, end):
                if zips and self[i][7] not in zips:
                    continue

                print(self[i])
        else:
            zipList = self.zipCodeList(zip)
            for i in range(start, end):
                if zips and zipList[i][7] not in zips:
                    continue

                print(zipList[i])

    def zipCodeList(self, zip=None):
        """
        This method returns a list of unique zip codes present in the data.
        If a specific zip code is provided, it only includes that zip code.
        """
        zip_codes = []
        for row in self:
            if zip is not None and zip not in row:
                continue
            zip_codes.append(row)
        return zip_codes

    def countByZip(self):
        zip_counts = {}
        for row in self:
            zip_code = row[8]
            if zip_code not in zip_counts:
                zip_counts[zip_code] = 1
            else:
                zip_counts[zip_code] += 1

        # Calculate total crimes
        total_crimes = sum(zip_counts.values())

        # Calculate percentage and create tuples (zip code, count, percentage)
        count_tuples = []
        for zip_code, count in zip_counts.items():
           percentage = str(round((count / total_crimes) * 100 , 2)) + ' %'
           count_tuples.append((zip_code, count, percentage))

        # Sort tuples by count in descending order
        count_tuples.sort(key=lambda x: x[1], reverse=True)

        return count_tuples

    def countByCrime(self):
        """
        This method provides a list of crimes by crime code for the entire data or a selected zip code.
        The list includes the description of the crime and is sorted by frequency from highest to lowest.
        """
        crime_counts = {}
        for row in self:
            crime_code = row[2]
            crime_description = row[3]
            if crime_code not in crime_counts:
                crime_counts[crime_code] = [1, crime_description]
            else:
                crime_counts[crime_code][0] += 1

        # Calculate total crimes
        total_crimes = sum([count[0] for count in crime_counts.values()])

        # Calculate percentage and create tuples (crime code, count, percentage, description)
        count_tuples = []
        for crime_code, count_description in crime_counts.items():
            count = count_description[0]
            description = count_description[1]
            percentage = str(round((count / total_crimes) * 100, 2)) + ' %'
            count_tuples.append((crime_code, count, percentage, description))

        # Sort tuples by count in descending order
        count_tuples.sort(key=lambda x: x[1], reverse=True)

        # Print the tuples vertically
        for count_tuple in count_tuples:
            print('\n'.join(map(str, count_tuple)) + '\n')

        return count_tuples

# Instantiate an object of the FCPDCrime class
FC = FCPDCrime(name='IT209 A7 – FCPD Crime Reporting Analytics Class')

# Load the data from the csv file into the FCPDCrime object
FC.load("C:\\Users\\sessa\\Downloads\\CrimeReports.csv")

# Run the necessary methods
# Prompt user before running each method
runPrintCrimes = input("\n\n\nPress Enter to run printCrimes method or type 'no' to skip: ")
if runPrintCrimes.lower() != "no":
    print("""
    IT209 - Assignment #7 :


    FCPD Police crime calls for the week 2024-03-24 through 2024-03-30:\n\n
    """)
    FC.printCrimes()

runZipCodeList = input("\n\nPress Enter to run zipCodeList method or type 'no' to skip: ")
if runZipCodeList.lower() != "no":
    print("""
\n\nIT209 - Assignment #7 :


FCPD Police crime calls for the week 2024-03-24 through 2024-03-30:
""")
    ZL = FC.zipCodeList(zip = '22030')
    for c in ZL:
        print(c)

runCountByZip = input("\n\nPress Enter to run countByZip method or type 'no' to skip: \n\n")
if runCountByZip.lower() != "no":
    CL = FC.countByZip()
    for c in CL:
        print(c)

runCountByCrime = input("Press Enter to run countByCrime method or type 'no' to skip: ")
if runCountByCrime.lower() != "no":
    print(FC.countByCrime())

print("End of Program")