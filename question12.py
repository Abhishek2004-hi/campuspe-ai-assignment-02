#Multiplication Table Generator 
#here user is giving the input
number=int(input("Enter number: "))
end=int(input("Enter range : "))   #here end is the range in which we have to stop the iteration
print("\n multiplication Table of",number)
for i in range(1,end+1):    #the range starts from 1 to end 
    result=number*i   #multiplying number with i
    print(number,"x",i,"=",result)