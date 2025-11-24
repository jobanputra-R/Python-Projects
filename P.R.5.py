#pr.5 OOP Wrapper 
list1=[]

class Employee:
    name=None
    age=None
    employee_id=None
    salary=None
    
    def  __init__ (self):
        self.name=input("Enter Name: ")
        self.age=int(input("Enter Age: "))
        self.employee_id=input("Enter Employee Id: ")
        self.salary=int(input("Enter Salary: "))
    def getData(self):
        print(f"Employee created with name: {self.name}, age: {self.age}, ID: {self.employee_id}, and salary: {self.salary}💲")


class Manager(Employee):
    department=None  
    
    def __init__(self):
        super().__init__()
        self.department=input("Enter Department: ")
    def getdata(self):
        print(f"Manager created with name: {self.name}, age: {self.age}, ID: {self.employee_id}, and salary: {self.salary}💲, and department: {self.department}")
    
class Devloper(Employee):
    language=None
    def __init__(self):
        super().__init__()
        self.language=input("Enter your language")
    def getlanguage(self):
        print(f"Devloper created with name: {self.name}, age: {self.age}, ID: {self.employee_id}, and salary: {self.salary}💲, and Language known: {self.language}")
    
while True:    
        print("--- Python OOP Project: Employee Management System---")

        print("Choose an operation:")
        print("1. create a person ")
        print("2. create an employee ")
        print("3. create a Manager ")
        print("4. create a Devloper ")
        print("5. Show detail ")
        print("6. Exit ")

        choice=int(input("Enter your choice"))
        match choice:
                
            case 1:
                class person:
                    global list1
                    name=None
                    age=None
                    
                    def setData(self):
                        self.name=input("Enter Name: ")
                        self.age=int(input("Enter Age: "))
                    def getdata(self):
                        print(f"Person created with name: {p1.name} and age: {p1.age}")
            
                p1=person()
                p1.setData()
                p1.getdata()
                person1 = {'name':p1.name,'age':p1.age}
                list1.append(person1)
            case 2:
                e1=Employee()       
                e1.getData()
            case 3:     
             m1=Manager()     
             m1.getdata() 
            case 4 :
             d1=Devloper()
             d1.getlanguage()  
            case 5:
                print("Choose detail to show: ")
                print("1. Person")
                print("2. Employee")
                print("3. Manager")
                print("4. Devloper")
                select=int(input("Enter to view detail"))
                match select:
                    case 1:
                        for i in list1:
                            for j in i:
                                if list1==[]:
                                    print("No Person Created Yet!")
                                    break
                                elif j=='name':
                                    print(f"Person Details: Name: {i['name']} Age: {i['age']}")
                                
                    case 2:
                        e1.getData()
                    case 3:
                        m1.getdata() 
                    case 4:    
                        d1.getlanguage()  
                    case _:
                        print("Invalid Choice Try again!")
            case 6:
                print("You Successfully Exited !")            
                break
            case _:
                print("Invalid Choice Try Again !")