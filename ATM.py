class Atm(object):
    def __init__(self,cardNo,pinNo):
        self.cardNo = cardNo
        self.pinNo = pinNo

    def CashWithdrawl(self):
        print("Cash Withdrayed successfully")

    def BalanceEnquiry(self):
        print("Ur Balance") 

Mia = Atm(102360493,1234)

print(Mia.pinNo)        