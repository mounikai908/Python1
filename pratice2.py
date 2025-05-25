class Bank:
    def __init__(self):
        self.balanace=0
    
    #Deposit
    
    def deposit(self,amount):
        self.balanace=self.balanace + amount
        print(f"{amount} is deposited successfully.")
    
    #Withdraw 
    
    def withdraw(self,amount):
        if self. balanace > amount :
            self.balanace=self.balanace - amount
            print(f"{amount} is successfully withdraw ")
            
        else :
            print("Insuffent balance...")
            
    # Check_Balance 
    def chack_balance(self):
        print(f"Your bank balance is {self.balanace}")




b=Bank()

while True:
    print("Please select Below any one option.....")
    print("1. Deposit \n2. Withdraw \n3. Check_Balance \n4. Exit")

    option = input("Select any one '1 / 2 / 3 / 4' : ")
   

    if option in ("1","2","3","4"):
        if option == "1" :
            try:
                amount=int(input("Enter you want to deposit amount : "))
                b.deposit(amount)
            except ValueError:
                print("Invalid input please try again ....")
                continue
            
        elif option == "2":
            try:
                amount=int(input("Entere You want to withdraw amount : "))
            except ValueError:
                print("Invalid input please try again ....")
                continue
            
        elif option == "3" :
            b.chack_balance()
        
        elif option == "4" :
            break
    else :
        print("inviled input....\n    ")



# hello this is 