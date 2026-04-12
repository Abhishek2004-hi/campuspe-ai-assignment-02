#Ticket Pricing System 
#taking inputs from user
age=int(input("Enter age: "))
day=input("Enter the day:")
tickets=int(input("Enter number of tickets: "))
#determine base price based on age
if age<3:
    base_price=0
elif age>=3 and age<=12:
    price=150
elif age>=13 and age<=59:
    price=300
else:  # age 60 and above
    price=200
#determine discount based on day
if day in ["friday","saturday","sunday"]:
    discount=0.20   # 20% discount
else:
    discount=0      # No discount (Monday-Thursday)
discount_amount=price*discount                              #calculate discount amount
price_after_discount=price-discount_amount                  #calculate price after discount
total_amount=price_after_discount*tickets                 #calculate total amount for all tickets
#display results
print("\n===BILL DETAILS===")
print("Price per ticket:",price)
print("discount per ticket:",discount_amount)
print("Price after discount per ticket:",price_after_discount)
print("total amount:",total_amount)