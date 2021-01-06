choice = input("Do you want to (r)ead from file or (w)rite to file ")

#three main ways to open a file
# 1. r -> read 
# 2. w -> write
# 3. a -> append

if choice == "r":
    #read from file
    with open("numbers.txt") as fileptr:
        total = 0
        for line in fileptr:
            total += int(line)
            print(line.strip())
        print("total: ", total)
    pass
elif choice =="a":
    #append to file
    with open("numbers.txt", "a") as fileptr:
        while True:
            number = input("Enter a number, type stop to end: ")
            if number == "stop":
                break
            else:
                fileptr.write(number+"\n")
    pass
else:
    print("command not recognized")