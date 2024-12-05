user_name = "Veerendra"
Password = "2408"

user = input("Enter Your USer_name: ")
pass_word = input("Enter your password: ")

if user == user_name  and pass_word == Password :
    print ('''
    1.Withdrawl
    2.Deposit
    3.Mini_statement
    4.Exit                  
    ''')
    amount = 50000
    option =  int(input("Enter Your input: "))
    if option == 1:
        withdrawl = int(input("Enter the amount: "))
        amount -= withdrawl
        print("Account Balance: ",amount)
    if option == 2:
        Deposit = int(input("Enter the amount: "))
        amount += Deposit
        print("Account Balance: ",amount)
    if option == 3:
        print("========ATM========") 
        print("                   ")  
        print("Name   : ",user_name)
        print("Balance: ",amount)
        print("                   ") 
        print("=Thanks for visiting=")
    if option == 4:
        exit()
else:
    print("Please enter correct Details")            


       





