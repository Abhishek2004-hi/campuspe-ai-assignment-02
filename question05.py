#Bill Splitter
#the user input for bill,number of people,tax,tip
bill=float(input('Enter the total bill amount: '))
persons=int(input('Enter the number of people: '))
tax=float(input('Enter the tax percentage: '))
tip=float(input("Enter the tip percentage: "))
tax_amount=(bill*tax)/100                 #here we are calculating the tax amount by multiplying with biil and tax and dividing it               
after_tax=bill+tax_amount                 #after tax is calculated by adding the bill and tax amount   
tip_amount=(bill*tip)/100                 
final=after_tax+tip_amount                #the final total amount is calculated by after tax and tip amount   
per_person=final/persons                  #the per person is calculated by dividing the the both final amount and number of persons             
#here we displaying the result
print("\n==BILL BREAKDOWN==")                            
print("Subtotal:Rs",bill,)
print("Tax(",tax,"%):",tax_amount)
print("After tax:Rs",after_tax)
print("Tip(",tip,"%):Rs",tip_amount)
print("Total:Rs",final)
print("Per person:Rs",per_person)