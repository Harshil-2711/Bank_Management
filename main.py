import json
import random
import string
from pathlib import Path

class Bank:
    database='data.json'
    data=[]

    try:
       
       if Path(database).exists():
                       
            with open (database) as fs:
                data=json.loads(fs.read())

       else:
            
            print("No such file exists")        

    except Exception as err:
        print(f"an exception occured as {err}")

    @staticmethod
    def update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        splchar=random.choices("!@#$*&^",k=1)
        id=alpha+num+splchar
        random.shuffle(id)
        return "".join(id)



    def createaccount(self):
        info={
            "name": input("enter your name: "),
            "age": int(input("tell your age: ")),
            "email": input("tell your email: "),
            "pin": int(input("tell your pin: ")),
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0
        }
        if info['age']<18 or len(str(info['pin']))!=4:
            print("sorry you cant create account ")

        else:
            print("account created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account no ")


            Bank.data.append(info)
            Bank.update()

    def depositmoney(self):
        acc=input("enter your account no: ")
        p=int(input("enter your pin: "))

        userdata=[i for i in Bank.data if i['accountNo.'] == acc and i['pin'] == p]

        if userdata == False:
            print("sorry no data found")

        else:
            amount=int(input("enter amount to deposit: ")) 
            if amount>10000 or amount<0:
                print("you cant deposit amount above 10000 and below 0")

            else:
                userdata[0]['balance']+=amount
                Bank.update()
                print("amount deposited succesfully") 

                
    def withdrawmoney(self):
            acc=input("enter your account no: ")
            p=int(input("enter your pin: "))
    
            userdata=[i for i in Bank.data if i['accountNo.'] == acc and i['pin'] == p]
    
            if userdata == False:
                print("sorry no data found")
    
            else:
                amount=int(input("enter amount to withdraw: ")) 
                if userdata[0]['balance'] < amount:
                    print("you dont have that much money")
    
                else:
                    userdata[0]['balance']-=amount
                    Bank.update()
                    print("amount withdrawn succesfully")    

    def showdetails(self):
        acc=input("please enter your account no: ")
        pin=int(input("please enter your pin: "))

        userdata=[i for i in Bank.data if i['accountNo.']==acc and i['pin']==pin]
        print("your information are\n\n")
        for i in userdata[0]:
            print(f"{i}:{userdata[0][i]}")

    def detailsupdate(self):
        acc=input("please enter your account no: ")
        pin=int(input("please enter your pin: "))
        
        userdata=[i for i in Bank.data if i['accountNo.']==acc and i['pin']==pin]

        if userdata == False:
            print("sorry no data found")

        else:
            print("you cant change age , account number , balance")

            print("fill the data to be changed or leave empty if no change")

            newdata={
                "name": input("please enter new name or press enter"),
                "email": input("enter your new email or press enter"),
                "pin": input("enter your new pin or press enter")
            }
            if newdata["name"]=="":
                newdata["name"] = userdata[0]['name']

            if newdata["email"]=="":
                newdata["name"] = userdata[0]['email']

            if newdata["pin"]=="":
                newdata["pin"] = userdata[0]['pin']         

            newdata['age'] = userdata[0]['age']

            newdata['accountNo.'] = userdata[0]['accountNo.']

            newdata['balance'] = userdata[0]['balance'] 
        

user=Bank()
print("press 1 for creating an account")
print("press 2 for deposting money")
print("press 3 for withdrawing money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting account")

a=int(input("tell your response: "))
if(a==1):
    user.createaccount()

if(a==2):
    user.depositmoney()    

if(a==3):
    user.withdrawmoney()    

if(a==4):
    user.showdetails() 

if(a==5):
    user.detailsupdate()       