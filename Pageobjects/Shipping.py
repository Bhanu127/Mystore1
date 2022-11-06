from selenium.webdriver.common.by import By


class Shipping:

    radiobutton1 = "cgv"
    processdelivery = "//button[@name='processCarrier']"


    def __init__(self , driver):
        self.driver = driver

    def radiobuttonclick(self):
        return self.driver.find_element("id", self.radiobutton1).click()

    def deliveryprocess(self):
         return self.driver.find_element(By.XPATH, self.processdelivery).click()