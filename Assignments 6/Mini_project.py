from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print("Rs.", amount, "Paid via credit cart.")

class Bank(PaymentMethod):
    def pay(self, amount):
        print("Rs.", amount, "paid via bank transfer.")

class EasyPaisa(PaymentMethod):
    def pay(self, amount):
        print("Rs.", amount, "paid via easypaisa.")

def payment_karwao(method, amount):
    method.pay(amount)

cc = CreditCard()
b = Bank()
e = EasyPaisa()

payment_karwao(cc, 1500)
payment_karwao(b, 2500)
payment_karwao(e, 700)
