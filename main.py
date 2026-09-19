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
        pass


    def createaccount(self):
        data={
            "name": input("enter your name: "),
            "age": int(input("tell your age: ")),
            "email": input("tell your email: "),
            "pin": int(input("tell your pin: ")),
            "accountNo.": 1234,
            "balance": 0
        }
        if data['age']<18 or len(str(data['pin']))!=4:
            print("sorry you cant create account: ")

        else:
            print("account created successfully")
            for i in data:
                print(f"{i} : {data[i]}")
            print("please note down your account no: ")

            Bank.update(data)








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