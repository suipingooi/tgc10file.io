#with open("file") as fileptr <- auto file closure
fileptr = open("new_numbers.txt", "w")

n = (int(input("please enter a number, enter -99 to stop")))
while n != -99:
    fileptr.write(str(n)+"\n")
    n = int(input("please enter a number, enter -99 to stop"))

print("program ended")
fileptr.close()
