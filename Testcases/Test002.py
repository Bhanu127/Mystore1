from selenium.webdriver.common.by import By
from Pageobjects.LogIn import LogIn
from Utilities.CustomLog import CustomLog
from Utilities.Readconfig import Readconfig
from Utilities.BaseClass import BaseClass


class Test002(BaseClass):
    baseURL = Readconfig.geturl()
    log = CustomLog.getlogger()
    reg1account = Readconfig.getregaccount1()
    reg2account = Readconfig.getregaccount2()
    text1 = Readconfig.getregtext1()
    text2 = Readconfig.getregtext2()

    def testsigningpage1(self, setup):
        self.log.info("*******testsigningpage1********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.wait1(7, "//*[(@class = 'login')]")
        self.lp = LogIn(self.driver)
        self.mousehover1(self.lp.driver.find_element(By.XPATH, "//*[(@class = 'login')]"))
        self.lp.signin1(self.reg1account)
        self.lp.regclick1()
        self.wait1(15, "//*[text()[contains(.,'Your personal information')]]")
        if "Login - My Store" == self.driver.title:
            assert True
            self.log.info("******MailID is valid and proceed for registration********")
        else:
            self.log.error("*******Registration page is not available********")
            assert False

    def testsigningpage2(self, setup):
        self.log.info("*******testsigningpage2********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.wait1(7, "//*[(@class = 'login')]")
        self.lp = LogIn(self.driver)
        self.mousehover1(self.lp.driver.find_element(By.XPATH, "//*[(@class = 'login')]"))
        self.lp.signin1(self.reg2account)
        self.lp.regclick1()
        self.wait2(3,"div[id = 'create_account_error'] ol li")
        a = self.lp.regtext1().text
        if  a == self.text1:
            self.log.error("*******registration is unsuccessful********")
        elif "Login - My Store" == self.driver.title:
            self.log.info("*******registration is successful********")
        else:
            self.log.error("*******registration is unsuccessful********")
        self.driver.close()

    def testsigningpage3(self, setup):
        self.log.info("*******testsigningpage3********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.wait1(7, "//*[(@class = 'login')]")
        self.lp = LogIn(self.driver)
        self.mousehover1(self.lp.driver.find_element(By.XPATH, "//*[(@class = 'login')]"))
        self.lp.regclick1()
        self.wait2(3, "div[id = 'create_account_error'] ol li")
        a = self.lp.regtext1().text
        if a == self.text2:
            self.log.error("*******registration is unsuccessful********")
        elif "Login - My Store" == self.driver.title:
            self.log.info("*******registration is successful********")
        else:
            self.log.error("*******registration is unsuccessful********")
        self.driver.close()




