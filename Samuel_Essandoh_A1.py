#Assignment: IT209 –  ASSIGNMENT 1 (A1)
# Purpose:Dictionary and Output text file
#Name: Samuel Essandoh
print("Beginning of Program\n")
def loadItems():
    stateList = []
    with open('staeinfo7.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if len(line) > 4:
                data = line.split(';')
                cleaned_data = [item.strip() for item in data]
                stateList.append(cleaned_data)
    return stateList
#removes all the semi-colons to make a list
def displayItems(stateList):
    print("Abbreviation\tName\t\t\t\tCapital\t\t\t\tPopulation")
    print("=============\t===================\t=================\t===============")
    for state in stateList:
        print("{0:<16}{1:22}{2:20}{3:<5}".format(state[0], state[1], state[2], state[3]))

def buildDict(stateList):
    SD = {}
    for state in stateList:
        SD[state[0]] = state[1:]
    return SD
#turns the Abbreviation in each list into a key and remaining attributes into values
def writeFile(SD):
    with open('IT209_A1output.txt', 'w') as file:
        for key, value in SD.items():
            file.write("{},{},{}\n".format(value[0], value[1], value[2]))
#displays only the VALUES in the newly created key-value pairs and separates with commas

stateList = loadItems()
displayItems(stateList)
SD = buildDict(stateList)
writeFile(SD)


print("\n\nDictionary\n", SD)
#Visual of buildDict function
print("\nEnd of Program")
#End of program