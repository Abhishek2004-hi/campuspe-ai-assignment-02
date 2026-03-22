#Sum and Average Calculator
count=int(input("How many numbers"))
sum=0                               #to store sum
max=None                            #to store maximum value
mini=None                           #to store minimum value
for i in range(1,count+1):
    num=float(input("Enter number "+str(i)+":"))
    #add number to total sum
    sum=sum+num
    #set first number as initial max and min
    if max is None or num>max:
        maxi=num
    if mini is None or num<mini:
        mini=num
average=sum/count
print("\n===Results===")
print("Sum:",sum)
print("Average:",average)
print("Maximum:",max)
print("Minimum:",mini)