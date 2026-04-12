#Grade Calculator
#from m1 to m5 it is the user input
marks1=float(input("Enter marks for Subject 1: "))
marks2=float(input("Enter marks for Subject 2: "))
marks3=float(input("Enter marks for Subject 3: "))
marks4=float(input("Enter marks for Subject 4: "))
marks5=float(input("Enter marks for Subject 5: "))
#the variable marks is the total marks of the 5 subjects and calculating the percentage
marks=marks1+marks2+marks3+marks4+marks5                     
percentage=(marks/500)*100      
#determining grade based on percentage
if percentage>=90:
    result="A+(outstanding)"
elif percentage>=80:
    result="A(excellent)"
elif percentage>=70:
    result="B(good)"
elif percentage>=60:
    result="C(average)"
elif percentage>=50:
    result="D(pass)"
else:
    result="F(fail)"
#checking pass or fail .if the marks is less than 40 the result is fail 
# if the marks is greater than 40 then result is pass
if marks1>=40 and marks2>=40 and marks3>=40 and marks4>=40 and marks5>=40:
    result="Pass"
else:
    result="Fail"
#the displaying the variables
print("\n===RESULT SUMMARY===")
print("Marks in each subject:")
print("Subject 1:",marks1)
print("Subject 2:",marks2)
print("Subject 3:",marks3)
print("Subject 4:",marks4)
print("Subject 5:",marks5)
print("Total Marks:",marks,"/500")
print("Percentage:",percentage,"%")
print("Grade:",result)
print("Result:",result)