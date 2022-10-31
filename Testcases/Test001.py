from selenium.webdriver.common.by import By
from Pageobjects.LogIn import LogIn
from Utilities.CustomLog import CustomLog
from Utilities.Readconfig import Readconfig
from Utilities.BaseClass import BaseClass


class Test001(BaseClass):
    baseURL = Readconfig.geturl()
    log = CustomLog.getlogger()

    def testhomepagetitle(self, setup):
        self.log.info("*******testhomepagetitle********")
        self.driver = setup
        self.driver.get(self.baseURL)
        if "My Store" == self.driver.title:
            assert True
            self.log.info("*******successfully verified the site********")
        else:
            self.log.error("*******Verification was unsuccessful********")
            assert False
        self.wait1(7, "//*[(@class = 'login')]")
        self.lp = LogIn(self.driver)
        self.mousehover1(self.lp.driver.find_element(By.XPATH, "//*[(@class = 'login')]"))
        if "Login - My Store" == self.driver.title:
            self.log.info("*******inside the sign in page********")
        else:
            self.log.error("*******Page is not loaded********")
            assert False

