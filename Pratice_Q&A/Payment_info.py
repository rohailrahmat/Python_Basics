class payslip:
    def __init__(self, name, amount, payment):
        self.name = name 
        self.amount = amount
        self.payment = payment
    
    def pay(self):
        self.payment == "yes"
    
    def status(self):
        if self.payment == "yes":
            return self.name + " is paid" + str(self.amount)
        else:
            return self.name + " is not paid yet"

rohail = payslip("rohail", "no", 1000)
raheel = payslip("raheel", "no", 2000)

print(rohail.status(), "\n" ,raheel.status())

raheel.pay()

print("After Payment")
print(rohail.status(), "\n", raheel.status())