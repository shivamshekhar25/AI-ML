class BankAccount:
    def __init__(self,account_number,owner_number,balance):
        self.account_number=account_number
        self.owner_number=owner_number
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("amount deposit",amount)

    def withraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("withdrwal amount",amount)
        else:
            print("unsufficient balance")
    def check_balance(self):
        print("current balance",self.balance)



account1=BankAccount(204,"shivam",500000)

account1.deposit(5000)
account1.withraw(50000)
account1.check_balance()