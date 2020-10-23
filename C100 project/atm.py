class Atm (object):
    def __init__(self, atmCardNo, pinNo):
        self.atmCardNo = atmCardNo
        self.pinNo = pinNo

    def  CashWithdrawn (self):
        print("Cash withdrawn")

print("Welcome to the atm")
atmCardNo = int(input("Please enter you atm card number: "))
pinNo = int(input("Please enter your pin: "))

atm = Atm(atmCardNo,pinNo)
atm.CashWithdrawn()