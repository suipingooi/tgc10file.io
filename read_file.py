#filepointer - files must be in the same directory
fileptr = open("holiday.txt")
for line in fileptr:
    print(line.strip())