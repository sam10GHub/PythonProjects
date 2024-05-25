import json
## Assignment: IT209 – LAB 10 (LA10)
# Purpose:Creating and Processing CSV and JSON Data
# Name: Samuel Essandoh
# Step #1. Read file, create list of dictionaries
input('\n\n\nHit "Enter" to read the csv states file, create the list of dictionaries: \n\n')
SList = []
with open('C:/Users/sessa/PycharmProjects/pythonProject/stateinfo_csv.txt', 'r') as f:
    lines = f.readlines()
    for line in lines[1:]: # Skip the header
        row = line.strip().split(',')
        SList.append({'abbrev': row[0].strip(), 'name': row[1].strip(), 'capital': row[2].strip(), 'population': row[3].strip()})

# Step #2. Create JSON formatted output file from the list of dictionaries
input('\n\n\n"Enter" to create the json formatted output and write it to a file: \n')
with open('us_states.json', 'w') as f:
    json.dump(SList, f)

# Step #3. Inpsect the file just created to verify it was correctly written.
input('\n\n\nInspect the JSON file just created, then hit "Enter" to read it \n')

# Step #4. Read JSON file just created and recreate the list of dictionaries.
input('\n\n\n"Enter" to see read the json file and print the resulting list of dictionaries: \n')
with open('us_states.json', 'r') as f:
    jsonStates = json.load(f)
    for s in jsonStates:
        print(s["abbrev"], s["name"], s["capital"], s["population"])

# Step #5. Test the list of dictionaries created from the json file by printing state names whose population is 5,000,000 or higher.
input('\n\n\n"Enter" to see states whose population is 5,000,000 or higher: \n')
for s in jsonStates:
    if int(s["population"]) > 5000000:
        print(s["name"], s["population"])

input('\n\nHit "Enter" to end program')