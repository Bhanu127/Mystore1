from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pageobjects.LogIn import LogIn
from Pageobjects.Registration import Registration
from Utilities.BaseClass import BaseClass
from Utilities.CustomLog import CustomLog
from Utilities.Readconfig import Readconfig


class Test004(BaseClass):
    baseURL1 = Readconfig.geturl1()
    baseURL2 = Readconfig.geturl2()
    log = CustomLog.getlogger()
    reg3account = Readconfig.getregaccount3()
    password1 = Readconfig.getpassword1()
    password2 = Readconfig.getpassword2()

    def testlogin1(self, setup):
        self.log.info("*******testlogin1********")
        self.driver = setup
        self.driver.get(self.baseURL1)
        self.lp = LogIn(self.driver)
        self.lp.emaillogin().send_keys(self.reg3account)
        self.lp.passwordlogin().send_keys(self.password1)
        self.lp.buttonlogin()
        self.wait1(15, "//*[@class='logo img-responsive']")
        if  self.driver.current_url == self.baseURL2:
            assert True
            self.driver.close()
            self.log.info("*******login successful********")
        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.log.error("*******login unsuccessful********")
            assert False


    def testlogin2(self, setup):
        self.log.info("*******testlogin2********")
        self.driver = setup
        self.driver.get(self.baseURL1)
        self.lp = LogIn(self.driver)
        #providing blank input as email
        self.lp.passwordlogin().send_keys(self.password1)
        self.lp.buttonlogin()
        self.wait1(15, "//*[@class='logo img-responsive']")
        if  self.driver.current_url == self.baseURL2:
            assert True
            self.driver.close()
            self.log.info("*******login successful********")
        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_login.png")
            # self.driver.close()
            self.log.error("*******login unsuccessful********")
            assert False



    def testlogin3(self, setup):
        self.log.info("*******testlogin2********")
        self.driver = setup
        self.driver.get(self.baseURL1)
        self.lp = LogIn(self.driver)
        self.lp.emaillogin().send_keys(self.reg3account)
        #providing wrong password
        self.lp.passwordlogin().send_keys(self.password2)
        self.lp.buttonlogin()
        self.wait1(15, "//*[@class='logo img-responsive']")
        if  self.driver.current_url == self.baseURL2:
            assert True
            self.driver.close()
            self.log.info("*******login successful********")
        else:
            self.driver.get_screenshot_as_file(".\\C:\\Users\\Bhanu\\PycharmProjects\\Mystore\\Screenshots" + "test_login.png")
            # self.driver.close()
            self.log.error("*******login unsuccessful********")
            assert False


























