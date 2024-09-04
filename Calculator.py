def calculator():
     print("----Calculator----")

     while True:
       num1=float(input("Enter first number here: "))
       num2=float(input("Enter second number here: "))
       print("Press 1 for Addition")
       print("Press 2 for subraction")
       print("Press 3 for Multiplication ")
       print("Press 4 for Division")
       n = int(input("Enter your choice: "))
       if n==1:
         print("Sum= ",num1+num2)
       elif n==2:
         print("Difference= ",num1-num2)
       elif n==3:
           print("Multi= ",num1*num2)
       elif n==4:
           if num2!=0:
            print("Div= ",num1/num2)
           else:
               print("Divided by zero is infinite")
       elif n==5:
           print("---***Invalid choice,TATAAA***---")
           break

calculator()