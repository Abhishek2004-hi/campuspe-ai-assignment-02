#Number Pattern Printer
pattern=int(input("Choose pattern: "))
height=int(input("Enter height: "))
#pattern 1:
if pattern==1:                  #here if we choose the pattern 1
    for i in range(1,height+1): #the range i starts from 1 to height provided by the user input
        for j in range(1,i+1):  #the range of j starts from 1 to i 
            print(j,end=" ")    #here display the j by end with space" "
        print()  
#pattern 2                      
elif pattern==2:                #here if we choose the pattern 2
    for i in range(1,height+1): #the range i starts from 1 to height given by user
        for j in range(i):      
            print(i,end=" ")
        print()
#pattern 3
elif pattern==3:
    for i in range(height,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
#pattern 4
elif pattern==4:
    for i in range(1,height+1):
        for j in range(1,i+1):
            print(j,end="") 
        for j in range(i-1,0,-1):
            print(j,end="")
        print()
#invalid choice
else:
    print("Invalid pattern")