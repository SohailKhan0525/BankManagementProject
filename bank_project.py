import random
import string
import json
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            with open(database, 'w') as fs:
                fs.write("[]")
    except Exception as err:
        print(f"An error occured as {err}")
    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __generateaccountno(cls):
        alpha = random.choices(string.ascii_letters, k = 6)
        num = random.choices(string.digits, k= 3)
        spchr = random.choices("$@!$#%&", k =2)
        id = alpha + num + spchr
        random.shuffle(id)
        return "".join(id)


    def createaccount(self):
        info = {
            'name' : input("Enter the full name: "),
            'age' : int(input("Enter your age: ")),
            'email' : input("Enter your email address: "),
            'pin' : input("Enter your pin(must be 4 digits): "),
            'accountno' : Bank.__generateaccountno(),
            'balance' : 0
        }
        if info['age'] < 18:
            print("Sorry you can't create the account, age must be 18 or above.")
        elif len(str(info['pin'])) != 4:
            print("Pin must be 4 digits.")
        else:
            print("Your account has been created.")
            for i in info:
                print(f"{i}: {info[i]}")
            print("Please Note down your account no.")
            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnum = input("Enter your account no: ")
        pin = input("Enter your pin: ")

        userdata = [i for i in Bank.data if i['accountno'] == accnum and i['pin'] == pin]
        if userdata == False:
            print("Sorry no data found.")
        else:
            amount = int(input("Enter the amount to be deposited: "))
            if amount > 15000 or amount < 0:
                print("The amount must be less than '15000'/ must be greater than '100")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("**************************************************")
                print(f"Amount ${amount} has been deposited successfully.")

    def withdrawmoney(self):
        accnum = input("Enter your account no: ")
        pin = input("Enter your pin: ")

        userdata = [i for i in Bank.data if i['accountno'] == accnum and i['pin'] == pin]
        if userdata == False:
            print("Sorry no data found.")
        else:
            amount = int(input("Enter the amount to withdraw: "))
            if userdata[0]['balance'] < amount:
                print("Infsufficient money.")
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("**************************************************")
                print(f"Amount ${amount} has been withdrawn successfully.")

    def showdetails(self):
        accnum = input("Enter your account no: ")
        pin = input("Enter your pin: ")

        userdata = [i for i in Bank.data if i['accountno'] == accnum and i['pin'] == pin]
        if userdata == False:
            print("Sorry no data found.")
        else:
            print("*************************")
            print("Your Bank Information\n\n")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")
            print("\n\n")

    def updatedetails(self):
        accnum = input("Enter your account no: ")
        pin = input("Enter your pin: ")

        userdata = [i for i in Bank.data if i['accountno'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found")
        
        else:
            print("\n")
            print("Fill the new details to update your bank information.")
            print("\n")

            newdata = {
                "name": input("Enter your new name or press enter to skip: "),
                "email":input("Enter your new email or press enter to skip: "),
                "pin": input("Enter your new pin or press enter to skip: ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']
            
            newdata['age'] = userdata[0]['age']

            newdata['accountno'] = userdata[0]['accountno']
            newdata['balance'] = userdata[0]['balance']
            
            # if type(newdata['pin']) == str:
            #     newdata['pin'] = int(newdata['pin'])
            

            for i in newdata:
                 if newdata[i] == userdata[0][i]:
                     continue
                 else:
                     userdata[0][i] = newdata[i]

            Bank.__update()
            print("\n")
            print("Account details has been successfully updated.")
            for i in userdata[0]:
                print(f"{i}: {userdata[0][i]}")
            print("\n")

    def deletebankacc(self):
        accnum = input("Enter your account no: ")
        pin = input("Enter your pin: ")

        userdata = [i for i in Bank.data if i['accountno'] == accnum and i['pin'] == pin]
        if userdata == False:
            print("Sorry no data found.")
        else:
            delete = input("Press 'y' to delete bank account or press 'n': ")
            if delete == 'n' or delete == 'N':
                print("Exits..")
            else:
                print("Please reconfirm.")
                redelete = input("Press 'y' to delete: ")
                if redelete == 'y' or redelete == 'Y':
                    index = Bank.data.index(userdata[0])
                    Bank.data.pop(index)
                    print("************************************************")
                    print("Your bank account has been deleted successfully.")
                    Bank.__update()


user = Bank()
while True:
    print("**************************")
    print("Press '1' to create an account")
    print("Press '2' to deposit money")
    print("Press '3' to withdraw money")
    print("Press '4' to see the details")
    print("Press '5' to update the details")
    print("Press '6' to delete an account")
    print("Press '7' to quit")
    print("**************************")

    try:
        resp = int(input("Enter your response: "))
    except Exception as err:
        print(f"Please enter a valid number [{err}]")
    if resp == 1:
        user.createaccount()
    elif resp == 2:
        user.depositmoney()
    elif resp == 3:
        user.withdrawmoney()
    elif resp == 4:
        user.showdetails()
    elif resp == 5:
        user.updatedetails()
    elif resp == 6:
        user.deletebankacc()
    elif resp == 7:
        print("----------------------")
        print("Quitting.... Good Bye!")
        print("----------------------")
        break
    else:
        print(f"{resp} is an invalid.")