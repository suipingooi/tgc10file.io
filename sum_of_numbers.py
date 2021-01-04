fileptr = open("numbers.txt")

total = 0
smallest = None
for line in fileptr:
    number = int(line)
    if smallest == None:
        smallest = number
    elif number < smallest:
        smallest = number

    total = total + number

print("smallest number = ", smallest)
print("sum of all the numbers = ", total)

fileptr.close()
