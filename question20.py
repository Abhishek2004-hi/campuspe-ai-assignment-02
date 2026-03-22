#Number System Functions
#the factorial Function
def factorial(n):
    if n<0:
        return "Not defined for negative numbers"
    result=1
    for i in range(1,n + 1):
        result*=i
    return result
#to check the prime Check Function
def isPrime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
#to check the fibonacci Function
def fibonacci(n):
    if n<=0:
        return "Enter positive number"
    a,b=0,1
    for i in range(n-1):
        a,b=b,a+b
    return b
#to check sum of Digits
def sumOfDigits(n):
    return sum(int(digit) for digit in str(abs(n)))
#reverse the Number
def reverseNumber(n):
    return int(str(n)[::-1])
#armstrong Number Check
def isarmstrong(n):
    digits=str(n)
    power=len(digits)
    total=0
    for digit in digits:
        total+=int(digit) ** power
    return total==n
#GCD Function
def gcd(a, b):
    while b!=0:
        a,b=b,a%b
    return a
#LCM Function
def lcm(a,b):
    return abs(a*b) // gcd(a,b)
#to check perfect Number 
def isPerfectNumber(n):
    if n<=1:
        return False
    total=0
    for i in range(1,n):
        if n%i==0:
            total+=i
    return total==n
#the menu Function
def mathMenu():
    while True:
        print("\n=====MATH MENU=====")
        print("1.Factorial")
        print("2.Prime Check")
        print("3.Fibonacci")
        print("4.Sum of Digits")
        print("5.Reverse Number")
        print("6.Armstrong Check")
        print("7.GCD")
        print("8.LCM")
        print("9.Perfect Number")
        print("10.Exit")
        choice=input("Enter your choice: ")
        if choice=="1":
            n=int(input("Enter number: "))
            print("Factorial:",factorial(n))
        elif choice=="2":
            n=int(input("Enter number: "))
            print("Prime:",isPrime(n))
        elif choice=="3":
            n=int(input("Enter position: "))
            print("Fibonacci:",fibonacci(n))
        elif choice == "4":
            n=int(input("Enter number: "))
            print("Sum of Digits:",sumOfDigits(n))
        elif choice=="5":
            n=int(input("Enter number: "))
            print("Reversed:",reverseNumber(n))
        elif choice=="6":
            n=int(input("Enter number: "))
            print("Armstrong:",isarmstrong(n))
        elif choice=="7":
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print("GCD:", gcd(a, b))
        elif choice=="8":
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print("LCM:",lcm(a,b))
        elif choice=="9":
            n = int(input("Enter number: "))
            print("Perfect Number:",isPerfectNumber(n))
        elif choice=="10":
            print("Exiting")
            break

        else:
            print("Invalid choice")
mathMenu()