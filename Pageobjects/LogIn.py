from selenium.webdriver.common.by import By


class LogIn:

    signininput = "//*[(@class = 'login')]"
    reginput = "//input[@id = 'email_create']"
    regclick = "//button[@id = 'SubmitCreate']"
    button_xpath = "//button[@value='1']"
    regtext = "div[id = 'create_account_error'] ol li"
    loginemail = "email"
    loginpassword = "passwd"
    loginbutton = "SubmitLogin"

    def __init__(self , driver):
        self.driver = driver

    def signinelement(self):
        self.driver.find_element(By.XPATH, self.signininput)

    def signin1(self,reg1account):
        self.driver.find_element(By.XPATH, self.reginput).clear()
        self.driver.find_element(By.XPATH, self.reginput).send_keys(reg1account)

    def regclick1(self):
        self.driver.find_element(By.XPATH, self.regclick).click()

    def regtext1(self):
         return self.driver.find_element(By.CSS_SELECTOR, self.regtext)

    def emaillogin(self):
         return self.driver.find_element("id", self.loginemail)

    def passwordlogin(self):
         return self.driver.find_element("id", self.loginpassword)

    def buttonlogin(self):
         self.driver.find_element("id", self.loginbutton).click()




    # def setPassword (self,password):
    #     self.driver.find_element("id", self.password_id).clear()
    #     self.driver.find_element("id", self.password_id).send_keys(password)

    def clickLogin (self):
        self.driver.find_element(By.XPATH, self.button_xpath).click()


    # def clickLogout (self):
    #     self.driver.find_element_by_id("id", self.linktext_logout).click()
    #



