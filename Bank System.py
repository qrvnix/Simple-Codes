# Simple bank made by qrvnix

status = True 
balance = 100

while status:
    print ("____________________________________ WELCOME! ____________________________________\n")                   
    print("SERVICES: \n 1 - Show my balance \n 2 - Deposit \n 3 - Withdraw \n 4 - Transfer money \n 5 - Interest \n 6 - Exit")                 
    try:
        choice = str(input("\nEnter your choice: "))                  
        print(" ")
    except ValueError:
        print("Invalid input. Please try again.")              
    else:                 
        if choice == '1':              
            print("___________________________________ MY BALANCE ___________________________________\n")
            print(f"Your balance is:         $ {balance:.2f}")      

        elif choice == '2':             
            status2 = True             
            while status2:
                print("____________________________________ DEPOSIT ____________________________________\n")
                try:
                    deposit = float(input("Enter an amount to deposit:      $ "))               
                except ValueError:
                    print("Invalid input. Please try again.\n")                 
                else:
                    if deposit <= 0:
                        print("Invalid amount to be deposited. Please try again.\n")                
                        balance += 0                  
                    else:
                        balance += deposit             
                        print(f"${balance:.2f} has been deposited.\n")                 
                        print("Your balance has been updated.\n")
                        status2 = False               

        elif choice == '3':              
            status3 = True             
            while status3:
                print("____________________________________ WITHDRAW ____________________________________\n")
                try:
                    withdraw = float(input("Enter an amount to withdraw:     $ "))           
                    print(" ")
                except ValueError:
                    print("Invalid input. Please try again.\n")        
                else:
                    if balance < withdraw:                
                        print("You have insufficient balance to process withdrawal.\n")
                        balance -= 0
                        status3 = False               
                    elif withdraw < 0:                
                        print("Invalid amount. Please try again.\n")
                    else:
                        balance -= withdraw               
                        print(f"You have withdrawn ${withdraw:.2f}")        
                        print("Your balance has been updated.\n")         
                        status3 = False             
               
        elif choice == '4':              
            print("__________________________________________________________________________________\n")
            recipientBalance = 100             
            status4 = True
            recipient = str(input("Enter the name of the recipient:      "))              
            print(" ")
            while status4:
                print("_________________________________ MONEY TRANSFER _________________________________\n")                
                print("MONEY TRANSFER SERVICES: \n 1 - Recipient's Information \n 2 - Transfer money \n 3 - Return to Main Services \n")            
                try:
                    choice2 = int(input("Enter your choice: "))             
                    print(" ")
                except ValueError:
                    print("Invalid input. Please try again.\n")                
                else:
                    if choice2 == 1:                 
                        print("_____________________________ RECIPIENT'S INFORMATION _____________________________\n")             
                        print(f"Recipient's name:               {recipient}")
                        print(f"Recipient's balance:            $ {recipientBalance:.2f}\n")
                    elif choice2 == 2:               
                        status4v2 = True
                        while status4v2:
                            print("_________________________________ MONEY TRANSFER _________________________________\n")
                            try:
                                transferMoney = float(input("Enter an amount to be transferred:     $ "))            
                                print(" ")
                            except ValueError:
                                print("Invalid input. Please try again.\n")                
                            else:
                                if balance < transferMoney:               
                                    print("You have insufficient balance. Make sure you have enough balance.\n")
                                    balance -= 0
                                    status4v2 = False              
                                elif transferMoney < 0:            
                                    print("Invalid amount to be transferred. Please try again.\n")
                                    balance -= 0
                                else:
                                    balance -= transferMoney                   
                                    recipientBalance += transferMoney           
                                    print(f"You have transffered ${transferMoney:.2f} to Mr./Ms. {recipient}")                 
                                    print("Your balance has been updated.\n")            
                                    status4v2 = False                
                    elif choice2 == 3:
                        status4 = False           

        elif choice == '5':               
            status5 = True
            while status5:
                print("____________________________________ INTEREST ____________________________________\n")
                try:
                    interest = float(input("Enter an amount of interest in percent (1-100):     "))               
                    print(" ")
                except ValueError:
                    print("Invalid input. Please try again (Numbers only).\n")           
                else:
                    if interest <= 0 or interest > 100:     
                        print("Invalid amount of interest. Please try again.\n")
                        balance += 0
                    else:
                        if balance <= 0:              
                            print("You have insufficient balance.\n")
                            status5 = False
                        else:
                            interestPercentage = interest / 100               
                            interestAmount = balance * interestPercentage              
                            balance += interestAmount              
                            print(f"An interest of {interest:.0f}% ($ {interestAmount:.2f}) has been added to your balance.\n")                 
                            status5 = False            
            
        elif choice == '6':              
            print("Thank you for using our services!\n")
            status = False               

        else:
            print("Invalid input. Please try again.\n")               
print("___________________________ THANK YOU! HAVE A NICE DAY! ___________________________\n")           