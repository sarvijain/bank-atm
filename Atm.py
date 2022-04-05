class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceinquiry(self):
        print("your balance is: $100")

    def cashwidthdrawal(self,amount):
        new_amount = 100-amount
        print("you withdrawed :" + str(amount)+ "your remaining balance is: " + str(new_amount))


def main():
    name = input("hello what is your name?")
    print("hello, "+ name)
    cardnumber = input("insert your card number: ")
    pin = input("enter your pin: ")
    new_user = Atm(cardnumber, pin)


    print("choose your activity")
    print("1. balance Inquiry")
    print("2. Cash withdrawal")
    activity = int(input("enter activity choice: "))


    if(activity == 1):
        new_user.balanceinquiry()
    elif (activity == 2):
        amount = int(input("enter the amount: "))
        new_user.cashwidthdrawal(amount)
    else:
        print("enter a valid number")

if __name__ == "__main__":
    main()