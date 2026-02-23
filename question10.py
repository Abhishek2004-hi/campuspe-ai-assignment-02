#simple atm simulator
balance=10000   #example:the initial balance of my account
while True:
    # Displaying ATM menu
    print("\n===ATM SIMULATOR===")
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")
    option=int(input('Enter the options: '))
    #option 1
    if option==1:   #if i choose the option 1 it shows my current balance of my account
        print("Current balance: ",balance)
    #option 2
    elif option==2:  #if i choose the option 2, i can deposit the amount to my account
        deposit=int(input("Enter the amt for Deposit:"))
        balance=balance+deposit   #the deposit amount will add up with my balance amount
        print("Deposit successful")
    #option 3
    elif option==3: #if i choose option 3 i can withdraw the money
        withdraw=float(input("Enter amount to withdraw: "))
        if withdraw<=balance-500:  # the condition is if my account has less than 500 than i can't withdraw the money
            balance=balance-withdraw
            print("Withdrawal successful!")
            print("New Balance:Rs",balance)
        else:
            print("Insufficient balance")
    #option 4
    elif option==4:
        print("Thank you for using ATM")
        break
    else:
        print("Invalid choice")

