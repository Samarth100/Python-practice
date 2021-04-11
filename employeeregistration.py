nameList=[]
salaryList=[]
departmentList=[]

while True:
    choice=int(input("Press 1 for for entery and 2 for exiting "))
    if choice == 1:
      name=input("Please enter your name ")    
      nameList.append(name)
      department=input("please enter your department ")
      departmentList.append(department)
      salary=input("please enter your salary ")
      salaryList.append(salary)
    else :
        break
print("Ypur final list is : ")
print(nameList)
print(salaryList)
print(departmentList)      