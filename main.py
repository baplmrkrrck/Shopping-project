def WriteFile(listtowrite):
    filename = None
    while filename == None:
        filename = input("Enter name to call file \n")

    f = open(filename, mode='w')
    for item in listtowrite:
        if item == listtowrite[-1]:
            f.write(item)
        else:
            f.write(item + "\n")
    f.close()
    print("Complete!")

def ReadFile():
    returnlist = []
    filename = None
    while True:
        filename = input("Enter file to read \n")
        try:
            f = open(filename, mode='r')
            lines = f.read().split("\n")
            for line in lines:
                returnlist.append(line)
            return returnlist
        except Exception as e:
            print("Failed: " + e)



menuOption = None

mylist = []

menuText = '''
1.) Add item to drop_lat_dist
2.) Print list
3.) Remove item by number
4.) Save list to file
5.) Load list from file
6.) Exit
'''

while menuOption != '6':
    menuOption = input("Enter selection\n")
    print(menuOption)
    if menuOption == '1':
        print("Add Item")
    elif menuOption == '2':
        print("Print list")
    elif menuOption == '3':
        print("Remove item by number")
    elif menuOption == '4':
        print("Save list to file")
        WriteFile(mylist)
    elif menuOption == '5':
        mylist = ReadFile()
        print(mylist)
        print("Load list from file")
    elif menuOption == '6':
        print("Quit")
    else:
        print("Selection was not recognized")
