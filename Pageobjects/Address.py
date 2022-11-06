from selenium.webdriver.common.by import By

class Address:


    deladdress = "//ul[@id='address_delivery']/li"
    billaddress = "//ul[@id='address_invoice']/li"
    addresscheckout = "//button[@name='processAddress']"

    def __init__(self, driver):
        self.driver = driver


    def deliaddress(self):
        return self.driver.find_elements(By.XPATH, self.deladdress)

    def billingaddress(self):
        return self.driver.find_elements(By.XPATH, self.billaddress)

    def checkoutaddress(self):
        return self.driver.find_element(By.XPATH, self.addresscheckout).click()




