#Temperature Converter 
while True:
    #displaying menu options
    print("\n===Temperature Converter===")
    print("1.Celsius to fahrenheit")
    print("2.Fahrenheit to celsius")
    print("3.Celsius to kelvin")
    print("4.Kelvin to celsius")
    print("5.Fahrenheit to kelvin")
    print("6.Kelvin to fahrenheit")
    print("7.Exit")
#taking user choice
    selection=int(input("Enter your choice: "))
#option 1 to convert celsius to fahrenheit
    if selection==1:                   #if user select 1
        c=float(input("Enter temperature in celsius: "))
        f=(c*9/5)+32                    #formula to convert celsius to fahrenheit
        print("Temperature in fahrenheit:",f)

#option 2 to convert fahrenheit to celsius
    elif selection==2:               #if user select 2
        f=float(input("Enter temperature in fahrenheit: "))
        c=(f-32)*5/9                    #formula to convert fahrenheit to celsius
        print("Temperature in celsius:",c)
#option 3 to convert celsius to kelvin
    elif selection==3:               #if user select 3
        c=float(input("Enter temperature in celsius: "))
        k=c+273.15                     #formula to celsius to kelvin
        print("Temperature in kelvin:",k)
#option 4 convert kelvin to celsius
    elif selection==4:               #if user select 4
        k=float(input("Enter temperature in kelvin: "))
        c=k-273.15                    #formula to kelvin to celsius
        print("Temperature in celsius:",c)
#option 5 is to convert fahrenheit to kelvin
    elif selection==5:               #if user select 5
        f=float(input("Enter temperature in fahrenheit: "))
        k=(f-32)*5/9+273.15          #formula to convert fahrenheit to kelvin 
        print("Temperature in kelvin:",k)
#option 6 is to convert kelvin to fahrenheit
    elif selection==6:               #if user select 6
        k=float(input("Enter temperature in kelvin:"))
        f=(k-273.15)*9/5+32          #formula to convert kelvin to fahrenheit 
        print("Temperature in fahrenheit:",f)
#option 7 is Exit the program
    elif selection==7:
        print("Exiting program.Thank you!")
        break
#handling invalid choice
    else:
        print("Invalid choice! Please select between 1 and 7.")