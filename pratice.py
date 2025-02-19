class Create_Account:
    
    bankname="canara Bank"
    branch="Veeravaram Branch"
    def __init__(self,username,password):
        self.username=username
        self.password=password
        print(f"Hi ** {self.username} ** welcome to {Create_Account.bankname}")
        
        
username=input("Enter new user name : ")

while True : 
   
    print("Your password  must be follow Below instraction\n          \n1. Password must be have one Captil latter \n2. Password must be have 8 characters \n3. Password Must ba have a lower letter \n4. Password Must be have a Special character \n     ")     
    password=input("Create Your  new Password : ")
    
    
    if len(password) >= 8 :
        
        upper_count=0
        lower_count=0
        num_count=0
        spl_count=0
        
        for i in password:
            if i.isalpha() :
                if i == i.upper():
                    upper_count+=1
                    
                if i == i.lower():
                    lower_count+=1
                    
            elif i.isnumeric():
                num_count+=1
                
            else:
                spl_count+=1
        
        if upper_count >= 1  and lower_count >=1 and num_count >= 1 and spl_count >= 1: 
                 
            print(f"Your {Create_Account.bankname} Account Created Successfully")
            break  
                
        else:
             print("Your password not satisfy above instraction Please Try again ")
             
c = Create_Account(username,password)

class Bank:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.balance=0.0
        
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
 
   
   
worng_count=0
chance=3
while True:        
    username=input("Enter Username : ")
    password=input("Enter Your password : ")
    if username == c.username and password == c.password:
        print("Your Account loged successfully.")
        break
    else:
        worng_count+=1
        chance-=1
        if chance > 0:
            print("Please enter currect username and Password")
            print(f"You have {chance} chances only ")
        
    if worng_count == 3 :
        print("Sorry You try three time Try After 24 Hours ")
        
        break
    
b=Bank(username,password)     
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
        
