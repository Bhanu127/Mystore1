import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pageobjects.Address import Address
from Pageobjects.LogIn import LogIn
from Pageobjects.Orderlist import Orderlist
from Pageobjects.Payment import Payment
from Pageobjects.Cart import Cart
from Pageobjects.Shipping import Shipping
from Utilities.BaseClass import BaseClass
from Utilities.CustomLog import CustomLog
from Utilities.Readconfig import Readconfig


class Test005(BaseClass):
    baseURL1 = Readconfig.geturl1()
    baseURL2 = Readconfig.geturl2()
    log = CustomLog.getlogger()
    reg3account = Readconfig.getregaccount3()
    password1 = Readconfig.getpassword1()   
    addedproducttext1 = Readconfig.addedproducttext1()
    baseurl3 = Readconfig.geturl3
    ordercartdeletetext1 = Readconfig.ordercartdeletetext1()
    dresstitle1 = Readconfig.dresstitle1()
    ordercarttitle1 = Readconfig.ordercarttitle1()
    ordercartemptytext1 = Readconfig.ordercartemptytext1()
    confirmordertext1 = Readconfig.confirmordertext1()


    def testselectorder1(self, setup):
        self.log.info("*******testselectorder1********")
        self.driver = setup
        self.driver.get(self.baseURL1)
        if self.baseurl3 != self.driver.title:
            assert True
        else:
            assert False
        self.lp = LogIn(self.driver)
        self.lp.emaillogin().send_keys(self.reg3account)
        self.lp.passwordlogin().send_keys(self.password1)
        self.lp.buttonlogin()
        self.wait1(5, "//*[@class='logo img-responsive']")
        self.ol = Orderlist(self.driver)
        self.mousehover2(self.ol.dress1())
        self.ol.casualdress1()
        if  self.dresstitle1 == self.ol.casualdresstitle1():
            assert True
            self.log.info("*******in casualdresses section********")
        else:
            self.log.error("***************")
            assert False
        self.idselect2("selectProductSort", "In stock")
        self.driver.implicitly_wait(5)
        if self.ol.textproduct1() == self.ol.sizeofproductlist():
            assert True
            self.log.info("*******product count is same as per shown.********")
        else:
            self.log.error("*******Product count is different.********")
            assert False
        self.mousehover2(self.ol.orderselect2())
        self.ol.addtocart()
        time.sleep(10)
        if self.addedproducttext1 == self.ol.productaddedtext1():
            assert True
            self.log.info("*******product added successfully text has not come.********")
        else:
            self.log.error("*******product added successfully text has not come.********")
            assert False
        self.ol.productadd1()
        if self.ordercarttitle1 == self.driver.title:
            assert True
            self.log.info("*******at orderpage*******")
        else:
            self.log.error("*******not at orderpage*******")
            assert False
        self.cart = Cart(self.driver)
        self.cart.deleteproduct1() 
        time.sleep(5)
        if self.cart.cartnoitem1() == self.ordercartdeletetext1:
            assert True
            self.log.info("*******order deleted*******")
        else:
            self.log.error("*******Order has not been deleted*******")
            assert False
        if self.ordercartemptytext1 == self.cart.orderempty1():
            assert True
            self.log.info("*******cart is empty*******")
        else:
            self.log.error("*******cart is not empty*******")
            assert False
        self.driver.close()

    def testselectorder2(self, setup):
        self.log.info("*******testselectorder1********")
        self.driver = setup
        self.driver.get(self.baseURL1)
        self.lp = LogIn(self.driver)
        self.lp.emaillogin().send_keys(self.reg3account)
        self.lp.passwordlogin().send_keys(self.password1)
        self.lp.buttonlogin()
        self.wait1(5, "//*[@class='logo img-responsive']")
        self.ol = Orderlist(self.driver)
        self.mousehover2(self.ol.dress1())
        self.ol.casualdress1()
        self.idselect2("selectProductSort", "In stock")
        self.driver.implicitly_wait(5)
        self.mousehover2(self.ol.orderselect2())
        self.ol.addtocart()
        time.sleep(5)
        self.ol.productadd1()
        self.cart = Cart(self.driver)
        a, b = self.cart.checktext1(), self.cart.checktext2()
        self.compareproducttext1(a, b)
        self.cart.addingproduct()
        time.sleep(3)
        a, b = self.cart.checktext1(), self.cart.checktext2()
        self.compareproducttext1(a, b)
        self.cart.substractingproduct()
        time.sleep(4)
        finalquantity, b = self.cart.checktext1(), self.cart.checktext2()
        self.compareproducttext1(finalquantity, b)
        finalprice = self.cart.finalprice()
        self.cart.checkoutlast()
        self.adr = Address(self.driver)
        if self.listvalue(self.adr.deliaddress()) == self.listvalue(self.adr.billingaddress()):
            assert True
            self.log.info("******Both addresses are equal********")
        else:
            self.log.CRITICAL("******Both addresses are not equal********")
            assert False
        time.sleep(3)
        self.adr.checkoutaddress()
        self.ship = Shipping(self.driver)
        self.ship.radiobuttonclick()
        self.ship.deliveryprocess()
        if finalprice == self.cart.totalvalueatpay():
            assert True
        else:
            assert False
        self.pay = Payment(self.driver)
        if finalquantity == self.pay.quantitytotal():
            assert True
        else:
            assert False
        self.pay.payatbank()
        paymentprice = self.pay.finalpayment()
        assert finalprice == paymentprice
        self.pay.finalorderconfirmation()
        confirmationtext = self.pay.confirmedtext()
        assert self.confirmordertext1 == confirmationtext
        confirmedprice = self.pay.confirmedprice()
        assert finalprice == paymentprice == confirmedprice
        self.driver.close()






















