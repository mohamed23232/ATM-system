import os 

AccountNumber = 54321
PinNumber = 12345
Balance = 0

def main():
    if login():
        isNotFinished = True
        while isNotFinished:
            if User_Input() == 1:
                ShowBalance()
                isNotFinished = False
                break
            elif User_Input() == 2:
                With_Draw()
                isNotFinished = False
                break
            elif User_Input() == 3:
                Deposit()
                isNotFinished = False
                break
            elif User_Input() == 4:
                isNotFinished = False
                break
            else:
                print("Please: try again")
                isNotFinished = True
            
def login():
    Given_Account_Number = 0
    Given_Pin_Number = 0
    invalid_Account_Number = True
    invalid_Pin_Number = True

    Name = input("Your Name is: ")
    print(f"Welcome, {Name}")

    while invalid_Account_Number:
        Given_Account_Number = int(input("Your Account Number: "))
        if Given_Account_Number == AccountNumber:
            invalid_Account_Number = False
        else:
            invalid_Account_Number = True
            print("Your Account number is not correct, Try again")
    while invalid_Pin_Number:
        Given_Pin_Number = int(input("Your Pin Number: "))
        if Given_Pin_Number == PinNumber:
            invalid_Pin_Number = False
        else:
            print("Your Pin number is not correct, Try again")
            invalid_Pin_Number = True
            
    return True

def User_Input():
    print("**MAIN MENU**")
    print("1:Show Balance")
    print("2:Withdraw")
    print("3:Deposit")
    print("4:Exit")
    
    Selected_Option = input("Enter Your Selected Option: ")
    return Selected_Option

def ShowBalance():
    print(f"Your Balance is: {Balance}$")

def With_Draw():
    option = 0
    amount = 0
    is_valid = True
    
    while is_valid:
        for i in range(10):
            sum = 0
            sum += 10
            print(f"{i + 1}: {sum}$")
        print("11: 200$")
        print("12: 400$")
        print("13: 500$")
        print("14: 1000$")

        option = input("Enter your Option: ")

        if option == 1:
            amount = 10
            is_valid = False
        elif option == 2:
            amount = 20
            is_valid = False
        elif option == 3:
            amount = 30
            is_valid = False
        elif option == 4:
            amount = 40
            is_valid = False
        elif option == 5:
            amount = 50
            is_valid = False
        elif option == 6:
            amount = 60
            is_valid = False
        elif option == 7:
            amount = 70
            is_valid = False
        elif option == 8:
            amount = 80
            is_valid = False
        elif option == 9:
            amount = 90
            is_valid = False
        elif option == 10:
            amount = 100
            is_valid = False
        elif option == 11:
            amount = 200
            is_valid = False
        elif option == 12:
            amount = 400
            is_valid = False
        elif option == 13:
            amount = 500
            is_valid = False
        elif option == 14:
            amount = 1000
            is_valid = False
        else:
            print("Try Again")
            is_valid =True
        if amount != 0:
            if Balance <= amount:
                print("you do not have enough balance")
            else:
                Balance -= amount
                print(f"Your Balance now is: {Balance}")
        amount = 0
       


def Deposit():
    option = 0
    amount = 0
    is_valid = True
    
    while is_valid:
        for i in range(10):
            sum = 0
            sum += 10
            print(f"{i + 1}: {sum}$")
        print("11: 200$")
        print("12: 400$")
        print("13: 500$")
        print("14: 1000$")

        option = input("Enter your Option: ")

        if option == 1:
            amount = 10
            is_valid = False
        elif option == 2:
            amount = 20
            is_valid = False
        elif option == 3:
            amount = 30
            is_valid = False
        elif option == 4:
            amount = 40
            is_valid = False
        elif option == 5:
            amount = 50
            is_valid = False
        elif option == 6:
            amount = 60
            is_valid = False
        elif option == 7:
            amount = 70
            is_valid = False
        elif option == 8:
            amount = 80
            is_valid = False
        elif option == 9:
            amount = 90
            is_valid = False
        elif option == 10:
            amount = 100
            is_valid = False
        elif option == 11:
            amount = 200
            is_valid = False
        elif option == 12:
            amount = 400
            is_valid = False
        elif option == 13:
            amount = 500
            is_valid = False
        elif option == 14:
            amount = 1000
            is_valid = False
        else:
            print("Try Again")
            is_valid =True
        if amount != 0:
            Balance += amount
            print(f"Your Balance now is: {Balance}")
        amount = 0

main()