nameList=[]
sectionList=[]
marksList=[]

while True:
    print()
    choice = int(input("Press 1 for adding student record, Press 2 to EXIT "))
    if choice == 1:
        name = input("Whats Your Name ")
        nameList.append(name)
        section = input("In which Class You are ")
        sectionList.append(section)
        marks = input("Whats were your marks ")
        marksList.append(marks)
    else:
        break

print("\n Display records :")
print(nameList)
print(sectionList)
print(marksList)
      