# Get data into list
with open("Day1\Data.txt") as file:
    lines = file.readlines()

# Strip crap off, make int
for i in range(len(lines)):
    lines[i] = int(lines[i].strip())

previousNum = -1
numIncreases = int(0)

# count number of increases
for i in range(len(lines)):
    if previousNum != -1 and lines[i] > previousNum:
        numIncreases += 1
        
    previousNum = lines[i]

print(numIncreases)
