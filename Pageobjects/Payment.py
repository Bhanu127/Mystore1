from selenium.webdriver.common.by import By


class Payment:
    toalquantity = "//td[@class='cart_quantity text-center']/span"
    bankpay = "//a[@title='Pay by bank wire']"
    finalpaymentvalue = "//span[@id='amount']"
    finalconfirmationorder = "//button[@class='button btn btn-default button-medium']"
    orderconfirmedtext = "//strong[normalize-space()='Your order on My Store is complete.']"
    priceconfirmed = "//strong[normalize-space()='$29.12']"

    def __init__(self , driver):
        self.driver = driver

    def quantitytotal(self):
         a = self.driver.find_element(By.XPATH, self.toalquantity).text
         return int(a)

    def payatbank(self):
        return self.driver.find_element(By.XPATH, self.bankpay).click()

    def finalpayment(self):
        return self.driver.find_element(By.XPATH,self.finalpaymentvalue).text

    def finalorderconfirmation(self):
        return self.driver.find_element(By.XPATH,self.finalconfirmationorder).click()

    def confirmedtext(self):
        return self.driver.find_element(By.XPATH, self.orderconfirmedtext).text

    def confirmedprice(self):
        return self.driver.find_element(By.XPATH, self.priceconfirmed).text

