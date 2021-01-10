from abc import ABCMeta,abstractmethod

class Payment(metaclass = ABCMeta):
    @abstractmethod
    def pay(self,money):
        pass

class Alipay(Payment):
    def __init__(self,use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self,money):
        if self.use_huabei:
            print('huabei pay %d yuan.' %money)
        else:
            print("zhifubao pay%d yuan" % money)

class WechatPay(Payment):
    def pay(self,money):
        print('wechat pay %d yuan' % money)
class Bankpay(Payment):
    def pay(self,money):
        print('bank pay %d yuan'% money)

class PaymentFactory:
    def create_payment(self,method):
        if method =='alipay':
            return Alipay()
        elif method == 'wechat':
            return WechatPay()
        elif method == 'huabei':
            return Alipay(use_huabei=True)
        else:
            raise TypeError('No such payment named %s' % method)

p = PaymentFactory()
z = p.create_payment('wechat')
p.create_payment('huabei').pay(100)
print(z)

class PaymentFactory_abstract(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass

class AlipayFactory(PaymentFactory_abstract):
    def create_payment(self):
        return Alipay()

class WechatPayFactory(PaymentFactory_abstract):
    def create_payment(self):
        return WechatPay()

class HuaweiFactory(PaymentFactory_abstract):
    def create_payment(self):
        return Alipay(use_huabei=True)

class BankpayFactory(PaymentFactory_abstract):
    def create_payment(self):
        return Bankpay()
pf = HuaweiFactory()
pff = pf.create_payment()
pff.pay(200)

