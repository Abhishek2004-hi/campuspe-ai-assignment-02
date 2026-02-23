#Factorial Calculator 
num=int(input("Enter a number: "))
#if the number is less than 0 the factorial is not defined 
if num<0:
    print("Factorial is not defined for negative numbers.")
#here the 0 is not equal to 1 
elif num==0:
    print("0!=1")
#calculate factorial for positive numbers
else:
    factorial=1
    steps=""
    for i in range(num,0,-1):
        factorial=factorial * i
        steps=steps+str(i)           #convert the number i to string and add it to steps in which multiplaction sequence like 5*4*3....
        if i!=1:                     #if i is not equal to 1 
            steps=steps+"x"          #if true, add 'x' symbol after the number
        print(f"{num}!={steps}={factorial}")