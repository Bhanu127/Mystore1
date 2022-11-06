from selenium.webdriver.common.by import By


class Orderlist:

    dress = "//div[@id='block_top_menu']/ul/li[2]"
    casualdress = "//div[@id='block_top_menu']/ul/li[2]/ul/li[1]/a"
    casualdresstitle = "//span[contains(text(),'Casual Dresses ')]"
    selectorder = "//ul[@class ='product_list grid row']/li"
    producttext1 = "//span[text()='There is 1 product.']"
    addcart = "//span[normalize-space()='Add to cart']"
    checkout1 =  "//a[@title='Proceed to checkout']"
    addedproducttext1 = "//h2[normalize-space()='Product successfully added to your shopping cart']"


    def __init__(self , driver):
        self.driver = driver

    def dress1(self):
         return self.driver.find_element(By.XPATH, self.dress)

    def casualdress1(self):
         return self.driver.find_element(By.XPATH, self.casualdress).click()

    def casualdresstitle1(self):
         return self.driver.find_element(By.XPATH, self.casualdresstitle).text

    def orderselect(self):
        return len(self.driver.find_element(By.XPATH, self.selectorder))

    def orderselect2(self):
        return self.driver.find_element(By.XPATH, self.selectorder)

    def textproduct1(self):
        return self.driver.find_element(By.XPATH, self.producttext1).text

    def sizeofproductlist(self):
        a = len(self.driver.find_elements(By.XPATH,self.selectorder))
        if a > 1:
            return "There are "+ str(a) + " products"
        else:
            return "There is 1 product."

    def addtocart(self):
        return self.driver.find_element(By.XPATH, self.addcart).click()

    def productadd1(self):
        return self.driver.find_element(By.XPATH, self.checkout1).click()

    def productaddedtext1(self):
        return self.driver.find_element(By.XPATH,self.addedproducttext1).text


