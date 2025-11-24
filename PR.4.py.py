# data analyzer and transfomer program
print("Welcome to the Data Analyzer and Transfomer Program")
l1=[]
while True:
    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")
    choice=int(input("Please enter your choice: "))
    match choice:
        case 1:
         print("enter data for 1D array ")
         list=int(input("Enter data"))
         l1.append(list)
         print(l1)
         print("Data has been stored successfully!")
        
        case 2:
          print("Data summary:")
          print("Total elements:-",len(l1))
          print("Minimum Value:-",min(l1))
          print("Maximum Value:-",max(l1))
          total=0
          for i in l1:
             total += i
          print(f"Sum of all values: {total}")     
          average=total/len(l1)
          print(f"Average value is {average}")

        case 3:
          print("Calculating factorial")
          def factorial(a):
             pass
        
        
        
        case 4:
          print("Enter a threshold value to filter out  data above this value")
          a = int(input(" "))
          thresold =lambda a,l1:a>=l1
          print("Filtered data ",thresold(int(input("Enter a value to thresold")),l1))

        case 5:
          print("Sortting data option:")  
          print("1. Ascending ")
          print("2. Descending ")
          ch1=int(input("Enter your choice"))
          match ch1:
             case 1:
                l1.sort()
                print(l1.sort())
             case 2:
                pass
             case _:
                print("Invalid option please enter a valid option")
        
        case 6:
          print("Dataset statics:")
