class Customer:

    def __init__(self, accNo, Balance):
        self.accNo = accNo
        self.Balance = Balance

    def credit(self, credit):
        self.Balance += credit
        print("Amount,",credit,"was credited")
        print(f"Available balance in the account is {self.Balance}")

    def debit(self, debit):
        self.Balance -= debit
        print("Amount,",debit,"was debited")
        print(f"Available balance in the account is {self.Balance}")


Acc1 = Customer(100, 100000)
print(Acc1.accNo)
print(Acc1.Balance)
Acc1.credit(1000)
Acc1.debit(3000)