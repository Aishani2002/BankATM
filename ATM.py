class ATM(object):
    def __init__(self,card,pin,balance):
        self.card = card
        self.pin = pin
        self.balance = balance
        
    def Depositing (self,deposit):
        print("Deposited " + deposit)
        
    def Withdrawal(withdraw,withdraw):
        print("Withdrawed " + withdraw)
        
    def BalanceEnquiry (self,balance):
        print(balance)
Aaliya=ATM(5318474827610296,87656,8000)
print(Aaliya.Depositing(500))