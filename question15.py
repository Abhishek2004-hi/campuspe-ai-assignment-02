#Check if a single number is prime
num=int(input("Enter a number: "))
if num<=1:   #if the number is less than 1 than it is not a prime number
    print("not a prime number",num)
elif num==2:  #if the number is equal to 2 the it is a prime number
    print("2 is a prime number")
else:
    prime=True #if it is true
    for i in range(2,num): #the range i is starts from 2 and number
        if num%i==0:
            prime=False    # if it is false than it fails and break the loop
            break
    if prime:
        print("Is a prime number",num)
    else:
        print("Is not a prime number",num)
#find prime numbers in a given range
start=int(input("\nEnter start range: "))
end=int(input("Enter end range: "))
print("Prime numbers:")
for n in range(start,end+1):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n)