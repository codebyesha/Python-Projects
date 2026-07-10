print("========Simple Calculator========")
while True:
    print("\n1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Power")
    print("5.Division")
    print("6.Floor Division")
    print("7.Modulus")
    print("8.Exit")
    choice=input("Choose an option(1-8): ")
    if choice == "8":
        print("Goodbye!")
        break
    if choice in ["1","2","3","4","5","6","7"]:
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        if choice == "1":
            print("Result: ",num1+num2)
        elif choice == "2":
            print("Result: ",num1-num2)
        elif choice == "3":
            print("Result: ",num1*num2)
        elif choice == "4":
            print("Result: ",num1**num2)
        elif choice == "5":
            if num2!=0:
                print("Result: ",num1/num2)
            else:
                print("Can't divided by zero")
        elif choice == "6":
            if num2!=0:
                print("Result: ",num1//num2)
            else:
                print("Can't divided by zero")
        elif choice == "7":
            if num2!=0:
                print("Result: ",num1%num2)
            else:
                print("Can't divided by zero")
        else:
            print("Invalid choice")

