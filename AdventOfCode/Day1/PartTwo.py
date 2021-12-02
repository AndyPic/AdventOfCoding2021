# Get data into list
with open("Day1\Data.txt") as file:
    lines = file.readlines()

# Strip crap off, make int
for i in range(len(lines)):
    lines[i] = int(lines[i].strip())

previousSum = -1
numIncreases = int(0)

# count number of increases
for i in range(len(lines)):

    if i+2 >= len(lines):
        break

    thisSum = lines[i] + lines[i+1] + lines[i+2]

    if previousSum != -1 and thisSum > previousSum:
        numIncreases += 1
        
    previousSum = thisSum

print(numIncreases)