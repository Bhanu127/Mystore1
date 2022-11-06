from selenium.webdriver.common.by import By


class Cart:

    deletebutton  = "3_13_0_763648"
    deletetext1 = "//p[@class='alert alert-warning']"
    emptytext1 = "//span[@class='ajax_cart_no_product']"
    textcheck1 = "//span[@id='summary_products_quantity']"
    textcheck2 = "//a[@title='View my shopping cart']//span[@class='ajax_cart_quantity']"
    productup = "cart_quantity_up_3_13_0_763648"
    productdown = "cart_quantity_down_3_13_0_763648"
    productaddedattribute = "//input[@name='quantity_3_13_0_763648']"
    productvalue1 = "//span[@id='product_price_3_13_763648']/span"
    producttotalvalue1 = "//td[@class='cart_total']/span"
    lastcheckout = "//a[@class='button btn btn-default standard-checkout button-medium']"
    pricefinal = "//span[@id='total_price']"
    totalvalue = "//span[@id='total_price']"

    def __init__(self , driver):
        self.driver = driver

    def deleteproduct1(self):
         return self.driver.find_element("id", self.deletebutton).click()

    def cartnoitem1(self):
         return self.driver.find_element(By.XPATH, self.deletetext1).text

    def orderempty1(self):
         return self.driver.find_element(By.XPATH, self.emptytext1).text

    def checktext1(self):
        a = self.driver.find_element(By.XPATH, self.textcheck1).text
        return int(a[0:1])

    def checktext2(self):
        return int(self.driver.find_element(By.XPATH, self.textcheck2).text)

    def addingproduct(self):
     return self.driver.find_element("id", self.productup).click()

    def substractingproduct(self):
     return self.driver.find_element("id", self.productdown).click()

    def addedproductattribute(self):
     return int(self.driver.find_element(By.XPATH, self.productaddedattribute).get_attribute("size"))

    def valueproduct1(self):
        a = self.driver.find_element(By.XPATH, self.productvalue1).text
        return float(a[1::])

    def totalvalueproduct1(self):
        a = self.driver.find_element(By.XPATH, self.producttotalvalue1).text
        return float(a[1::])

    def checkoutlast(self):
        return self.driver.find_element(By.XPATH, self.lastcheckout).click()

    def finalprice(self):
        return self.driver.find_element(By.XPATH,self.pricefinal).text





    def totalvalueatpay(self):
          return self.driver.find_element(By.XPATH, self.totalvalue).text

