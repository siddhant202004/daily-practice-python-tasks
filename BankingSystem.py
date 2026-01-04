#Build a simple banking system with deposit, withdraw, and balance checking.

print(" Welcome to Armor Bank ")


current_balance = 0 
deposit = 0
withdrawl = 0
while True:
    try:
        choice = int(input(f"\nSelect an option: \n 1. Check Balance \n 2. Deposit \n 3. Withdraw \n 4. Exit : \n "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4 ")
        continue
    if choice == 1:
        
        print(f"\nThis is your Balance {current_balance}$ ")
        
    elif choice ==2:
        
        deposit= float(input("\nEnter the deposit amount: "))
        if deposit<=0:
            print("Deposite amount must be greater than 0. ")
        else: 
            current_balance += deposit
        print(f"\nAmount deposited is {deposit}$")
        
    elif choice == 3:
        withdrawl = float(input("\nEnter the amount You want to withdrawl: "))
        if current_balance > withdrawl:
            current_balance-= withdrawl
            print(f"\nAmount {withdrawl}$ is withdrawl from your bank account")
        else:
            print(f"\nInsufficent Balance, Amount of {withdrawl}$ canot be withdrawled ")
            
        
    elif choice == 4: 
        print("\nThank you for using Armor Bank! ")
        break
    