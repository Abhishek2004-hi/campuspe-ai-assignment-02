#Simple Calculator
  
num1=eval(input("Enter the num1: "))             #Input 1 for user
num2=eval(input("Enter the num2: "))             #Input 2 for user
print("\nResult: ")
print(num1,"+",num2,"=",num1+num2)               # Addition
print(num1,"-",num2,"=",num1-num2)               # Subtraction
print(num1,"*",num2,"=",num1*num2)               # Multiplication
if num2!=0:                                      # Division
    print(num1,"/",num2,"=",round(num1/num2,2))  
else:
    print("Division by zero is not allowed")
print(num1,"%",num2,"=",num1%num2)               # Modulus
print(num1,"^",num2,"=",num1**num2)              # Exponentiation    