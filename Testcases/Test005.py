from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from Pageobjects.LogIn import LogIn
from Pageobjects.Orderlist import Orderlist
from Pageobjects.Registration import Registration
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


    def testselectorder1(self, setup):
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
        if  "Casual Dresses" == self.ol.casualdresstitle1():
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
        # self.wait.until(expected_conditions.element_to_be_clickable(By.XPATH("//span[normalize-space()='Add to cart']")))
        self.ol.addtocart()






