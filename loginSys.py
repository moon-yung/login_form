from database_handler import delete, register,login, get_acc_info, update_first_name,update_last_name,update_password,update_username,create_table
import datetime 
import pwinput # import password input ******
import os # for clear display
import hashlib # hide password



def loginRights(username, password):
    while True:
        accInfo = get_acc_info(username, password)
        print("\nChoose Option")
        print("[1] Change First Name")
        print("[2] Change Last Name")
        print("[3] Change Username")
        print("[4] Change Password")
        print("[5] Delete Account")
        print("[6] Log Out\n")
        
        choice = input(">>> ")

        if choice < "7":
            if choice == "1":
                new_first = input("Enter new First Name: ").title()
                update_first_name(username, password, new_first)
                print(f"First Name changed to {new_first}!")

            elif choice == "2":
                new_last = input("Enter new Last Name: ").title()
                update_last_name(username, password, new_last)
                print(f"Last Name changed to {new_last}!")

            elif choice =="3":
                new_user = input("Enter new Username: ")
                update_username(username, password, new_user)
                print(f"User Name changed to {new_user}!")

            elif choice == "4":
                while True:
                    new_password = input("Enter new password: ")
                    if len(new_password) <=8 :
                        print("Password must be 8 characters up")
                        print()
                        continue            
                    else:
                        new_pass = hashlib.sha256(new_password.encode('utf-8')).hexdigest()# encryption
                        update_password(username, password, new_pass)
                        print("Password changed!")
                        break

            elif choice == "5":
                sure = input("\nAre you sure to delete your account (Y/N)?: ")
                if sure.lower() == 'y':
                    delete(username,password)
                    print(f"{username} Account is Deleted") 
                    main()
                    continue

                elif sure.lower() == 'n' :
                    continue    

                else:
                    print("Input only Y or N")
                    continue    
                         
            elif choice == "6":
                print("Exiting.....")  
                break  
        
        else:
            print("\nEnter only numbers 1 to 5")


def main():
    while True:
        print("\nWelcome to Login System!\n")
        print("[1] Register")
        print("[2] Log in")
        print("[3] Exit\n")
        print()

        user_input = input(">>> ")
        if user_input < "4":
            if user_input == "1":
                print("-" *30)
                print("R E G I S T E R")
                print("-" *30)
                first = input("\nFirst Name: ").title()
                os.system('cls') # to clear display of last input
                last = input("\nLast Name: ").title()
                os.system('cls')
                un = input("\nUsername: ")
                os.system('cls')
                current_date = datetime.date.today()                                    
                
                while True:
                    pword = input("\nPassword: ")
                    if len(pword) <= 8 :
                        print("Password must be 8 characters up")
                        print()
                        continue                     
                    else:
                        pw = hashlib.sha256(pword.encode('utf-8')).hexdigest() #encryption
                        os.system('cls')
                        print("\nRegistration Details\n")
                        print(f"First Name: {first}")
                        print(f"Last Name : {last}")
                        print(f"Username  : {un}")
                        print(f"Password  : {pword}")
                        print(f"Date Registered: {current_date}")
                        break

                ask = input("\nAre you sure to register (Y/N)?: ")
                if ask.lower() == 'y':
                    print(f"{first} now registered!")
                    # get current date
                    register(first,last,un,pw,current_date)
                    continue 

                elif ask.lower() == 'n' :
                    continue   

                else:
                    print("Input only Y or N")
                    continue
    

            elif user_input == "2":
                print("-" *30)
                print("L O G  I N")
                print("-" *30)
                username = input("Username: ")
                # python convert user input to asterisk
                passwordlogin = pwinput.pwinput(prompt ="Password: ", mask="*")
                password = hashlib.sha256(passwordlogin.encode('utf-8')).hexdigest() #encryption
                print()
                if login(username,password):
                    print(f"{username}, You are now logged in!")
                    loginRights(username, password)
                else:
                    print("Sorry! Account not found in the Database\n")
                    continue
                
            else:
                print("Exiting......\n") 
                break 

        else: 
            print("\nEnter only numbers 1 to 3")      


main()