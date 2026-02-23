#Leap Year Checker
#taking year input from user
year=int(input("Enter a year: "))
#checking leap year conditions
if year%4==0:                                       #if not divisible by 4,it is not a leap year
    if year%100==0:                                 #if divisible by 4,check if divisible by 100,Years divisible by 100 are Not leap years,unless they are also divisible by 400
        if year%400==0:                             #if yes,then it iS a leap year
            print(year,"is a leap year")
            print("It is divisible by 400")
        else:
            print(year,"is NOT a leap year")
            print("It is divisible by 100 but NOT divisible by 400")
    else:
        print(year,"is a leap year.")               #if divisible by 4 but not divisible by 100 then it iS a leap year
        print("It is divisible by 4 but NOT divisible by 100.")    
else:                                               #if not divisible by 4 at all then it is not a leap year
    print(year,"is NOT a leap year")
    print("It is NOT divisible by 4")