#Calculator Functions 
#function to add two numbers
def add(a,b):
    return a+b  #return the value with add of a and b
#function to subtract two numbers
def subtract(a,b):
    return a-b  #return the value with substract of a and b
#function to multiply two numbers
def multiply(a,b):
    return a*b  #return the value with multiplication of a and b
#function to divide two numbers (handles division by zero)
def divide(a,b):
    if b == 0:
        return "Error Division of zero is not allowed."
    return a/b  #if b is equal to 0 than its get error ,if it is not 0 than divide both a and b
#function to find modulus
def modulus(a,b):
    return a%b  #return the value by modulus of a and b
#function to find power
def power(a,b):
    return a**b
#main calculator function with menu of 7
def calculator():
    while True:
        print("\n=====Calculator Menu=====")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Modulus")
        print("6.Power")
        print("7.Exit")
        choice = input("Enter your choice from 1 to 7: ")
        if choice == "7":
            print("Exiting Calculator...")
            break
        if choice in ["1","2","3","4","5","6"]:
            a=float(input("Enter first number: "))
            b=float(input("Enter second number: "))
            if choice=="1":
                print("Result",add(a,b))
            elif choice=="2":
                print("Result",subtract(a,b))
            elif choice=="3":
                print("Result",multiply(a,b))
            elif choice=="4":
                print("Result",divide(a,b))
            elif choice=="5":
                print("Result",modulus(a,b))
            elif choice=="6":
                print("Result",power(a,b))
        else:
            print("Invalid choice Please select 1 to 7")
#call the calculator function
calculator()