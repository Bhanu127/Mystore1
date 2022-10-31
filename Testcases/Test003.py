from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pageobjects.LogIn import LogIn
from Pageobjects.Registration import Registration
from Utilities.BaseClass import BaseClass
from Utilities.CustomLog import CustomLog
from Utilities.Readconfig import Readconfig


class Test003(BaseClass):
    baseURL1 = Readconfig.geturl1()
    log = CustomLog.getlogger()
    reg3account = Readconfig.getregaccount3()
    reg4account = Readconfig.getregaccount4()
    first_name = Readconfig.firstname1()
    last_name = Readconfig.lastname1()
    password1 = Readconfig.getpassword1()
    address1 = Readconfig.getaddress1()
    city1 = Readconfig.getcity1()
    postalcode1 = Readconfig.getpcode1()
    mobile1 = Readconfig.getmobile1()
    refer1 = Readconfig.getrefer1()
    ftext1 = Readconfig.getftext1()
    signintitle = Readconfig.geturl2()

    def testcheckinput1(self, setup):
        self.log.info("*******testcheckinput1********")
        self.driver = setup
        self.driver.get(self.baseURL1)
        self.lp = LogIn(self.driver)
        self.lp.signin1(self.reg4account)
        self.lp.regclick1()
        self.rg = Registration(self.driver)
        self.wait1(10, "//input[@id='id_gender1']")
        self.rg.radiobutton1()
        self.rg.firstname1().send_keys(self.first_name)
        self.rg.lastname1().send_keys(self.last_name)
        self.rg.password1().send_keys(self.password1)
        self.idselect1("days","15")
        self.idselect1("months", "7")
        self.idselect1("years", "1996")
        self.rg.address01().send_keys(self.address1)
        self.rg.city01().send_keys(self.city1)
        self.idselect1("id_state", "1")
        self.idselect2("id_country", "United States")
        self.rg.postalcode01().send_keys(self.postalcode1)
        self.rg.mobile1().send_keys(self.mobile1)
        self.rg.refer01().send_keys(self.refer1)
        self.rg.registersubmit()
        assert self.driver.current_url == self.signintitle
        self.driver.close()

    def testcheckinput2(self, setup):
        self.log.info("*******testcheckinput2********")
        self.driver = setup
        self.driver.get(self.baseURL1)
        self.lp = LogIn(self.driver)
        self.lp.signin1(self.reg4account)
        self.lp.regclick1()
        self.rg = Registration(self.driver)
        self.wait1(5, "//input[@id='id_gender1']")
        self.rg.radiobutton1()
        #skipped the firstname
        self.rg.lastname1().send_keys(self.last_name)
        self.rg.password1().send_keys(self.password1)
        self.idselect1("days","15")
        self.idselect1("months", "7")
        self.idselect1("years", "1996")
        self.rg.address01().send_keys(self.address1)
        self.rg.city01().send_keys(self.city1)
        self.idselect1("id_state", "1")
        self.idselect2("id_country", "United States")
        self.rg.postalcode01().send_keys(self.postalcode1)
        self.rg.mobile1().send_keys(self.mobile1)
        self.rg.refer01().send_keys(self.refer1)
        self.rg.registersubmit()
        self.wait1(5,"//div[@class='columns-container']//li[1]")
        assert self.rg.fnameerror() == self.ftext1
        self.driver.close()

    def testcheckinput3(self, setup):
        self.log.info("*******testcheckinput3********")
        self.driver = setup
        self.driver.get(self.baseURL1)
        self.lp = LogIn(self.driver)
        self.lp.signin1(self.reg4account)
        self.lp.regclick1()
        self.rg = Registration(self.driver)
        self.wait1(5, "//input[@id='id_gender1']")
        self.rg.radiobutton1()
        self.rg.firstname1().send_keys(self.first_name)
        self.rg.lastname1().send_keys(self.last_name)
        self.rg.password1().send_keys(self.password1)
        #skipped the date
        self.idselect1("months", "7")
        self.idselect1("years", "1996")
        self.rg.address01().send_keys(self.address1)
        self.rg.city01().send_keys(self.city1)
        self.idselect1("id_state", "1")
        self.idselect2("id_country", "United States")
        self.rg.postalcode01().send_keys(self.postalcode1)
        self.rg.mobile1().send_keys(self.mobile1)
        self.rg.refer01().send_keys(self.refer1)
        self.rg.registersubmit()
        self.wait1(5, "//p[normalize-space()='There is 1 error']")
        print(self.rg.sizeoferrorlist())
        a = self.rg.texterror1()
        print(a)
        if self.rg.sizeoferrorlist() == self.rg.texterror1():
            assert True
        else:
            assert False
        self.driver.close()

    def testcheckinput4(self, setup):
        self.log.info("*******testcheckinput4********")
        self.driver = setup
        self.driver.get(self.baseURL1)
        self.lp = LogIn(self.driver)
        self.lp.signin1(self.reg4account)
        self.lp.regclick1()
        self.rg = Registration(self.driver)
        self.wait1(5, "//input[@id='id_gender1']")
        self.rg.radiobutton1()
        self.rg.firstname1().send_keys(self.first_name)
        self.rg.lastname1().send_keys(self.last_name)
        #skipped the password
        #skipped the date
        self.idselect1("months", "7")
        self.idselect1("years", "1996")
        self.rg.address01().send_keys(self.address1)
        self.rg.city01().send_keys(self.city1)
        self.idselect1("id_state", "1")
        self.idselect2("id_country", "United States")
        self.rg.postalcode01().send_keys(self.postalcode1)
        self.rg.mobile1().send_keys(self.mobile1)
        self.rg.refer01().send_keys(self.refer1)
        self.rg.registersubmit()
        self.wait1(5, "//p[normalize-space()='There are 2 errors']")
        if self.rg.sizeoferrorlist() == self.rg.texterror2().text:
            assert True
        else:
            assert False
        self.driver.close()





























