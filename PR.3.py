#creating student data organizer
#1 add student
#2 display all student
#3 update student information
#4 delete student 
#5 display subjects offered
#6 exit
while True:
    student=[]
    students=(tuple)
    print("Press 1 add student")
    print("Press 2 display all student")
    print("Press 3 update student information")
    print("Press 4 delete student ")
    print("Press 5 display subjects offered")
    print("Press 6 exit")
   
    choice=int(input("Enter your choice"))
   
    match choice:
       case 1:
        id=int(input('Enter stud.id.'))
        for i in student:
             if i[id]=="id":
               print("student id is already exist")
               break
        else:
          name=input("Enter student  name")
          age=int(input("Enter student age"))
          grade=input("Enter grade")
          d_o_b=int(input("enter date of birth in (YYYY-MM-DD)"))
          subjects=input("enter subjects")

          i={'name':name,'age':age,'grade':grade,'d_o_b':d_o_b,'subjects':subjects}
          student.append(i)
          i2=(id,d_o_b)
          students.append(i2)
          