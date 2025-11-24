# Project logic box 
print("*=======Logical Box=======*")
while True:
    print("1.Generate a pattern")
    print("2.Analyze a ramge of numbers")
    print("3.Exit")
    print("*"*30)
    Choice=int(input("Enter your choice:"))
    print("*="*15)
    #rows=int(input("Enter the number of rows for the pattern"))
    if Choice==1:
        rows=int(input("Enter the number of rows for the pattern:-"))
        for i in range(1,rows+1):
            for j in range(1,i+1):
                print(j,end=" ")
            print()
    elif Choice==2:
        Start=int(input("Enter the Start of the range:"))
        end=int(input("Enter the End of the range:"))
        sum =0
        for i in range(Start,end+1):
            if i%2==0:
                print(f"Number is {i} even ")
                sum+=i
            else:
                print(f"Number is {i} odd ")
                sum+=i
        print("*"*30)
        print(f"The Sum of all the number is",sum)   
        print("*="*15)
    elif Choice==3:
        break
    else: 
        print("Invalid Choice enter a correct choice")
