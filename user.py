import csv
class User():

    def __init__(self, user_id=0, username="", password="", email="", balance=0.0):
        self.username = username
        self.password = password
        self.email = email
        self.balance = balance
        self.user_id = user_id

    def save_user(self):
        with open('users.csv', 'r') as f:
            lines_list = f.readlines()
        self.user_id = len(lines_list) + 254301 # That's id creater.
        with open('users.csv', 'a+') as f:
            f.write(f"{self.user_id},{self.username.upper()},{self.password},{self.email},{self.balance},\n")
    
    def check_id_password(self,entered_id, entered_password): #buble sorting'e daha sonra geçilecek.
        with open('users.csv','r') as f:
            line_list = f.readlines()
        
        for a in line_list:
            check_user = a.split(',')
            print(check_user)
            if check_user[0] == entered_id and check_user[2] == entered_password:
                return [True, check_user]
        return [False,""]

    def change_email(self):
        new_email = input("Please enter your new email: ")
        self.email = new_email

    def deposit(self): 
        # to deposit money.
        while True:
            try:
                amount = input("Please enter the amount:\n--------------------------------\nIf you give up, please press enter.\n")
                if amount == "":
                    break
                amount = float(amount)
                print(amount, type(amount))
                if amount > 0:
                    self.balance = float(self.balance)
                    self.balance += amount
                    self.balance = str(self.balance)
                    break 
                elif amount <= 0:
                    print("Please enter a positive number.")
            except:
                print("Please enter a valid amount")
    

    def withdrawal(self): # to wihthdrawal money.
        while True:
            try:
                amount = input("Please enter the amount:\n--------------------------------\nIf you give up, please press enter.\n")
                if amount == "":
                    break
                amount = float(amount)
                if amount >= 0 and self.balance > amount:
                    self.balance = float(self.balance)
                    self.balance -= amount
                    self.balance = str(self.balance)
                    break
                elif amount < 0:
                    print("Please enter a positive number.")
            except:
                print("Please enter a valid amount")

    def final_func(self): # This function saves the users changes and sorts again the users by ID
        with open("users.csv","r") as lines:
            line_list = lines.readlines()
        a = ""
        for i in line_list:
            if i.split(",")[0] == self.user_id:
                i = f"{self.user_id},{self.username.upper()},{self.password},{self.email},{self.balance},\n"
            a += i
        with open("users.csv","w") as file:
            file.write(a)




#  comand + k + c  command line a çeviriyor

if __name__ == "__main__":

    user_1 = User("254301","Berkay","asv123","alcin@hotmail.com","0.0")

    # user_1.deposit()
    # print(user_1.balance)
    # print(type(user_1.balance) )
    
    # user_1.wihthdrawal()
    # print(user_1.balance)
    # print(type(user_1.balance))
    
