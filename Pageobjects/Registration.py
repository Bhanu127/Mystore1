from selenium.webdriver.common.by import By


class Registration:

    radio1 = "id_gender1"
    # radio2 = "//input[@id='id_gender1']"
    firstname = "customer_firstname"
    lastname  = "customer_lastname"
    # email = "email"
    password = "passwd"
    address1 = "address1"
    city = "city"
    mobile = "phone_mobile"
    refer1 = "alias"
    registerbutton = "submitAccount"
    pcode = "postcode"
    firstnameerror = "//div[@class='columns-container']//li[1]"
    errortext1 = "//p[normalize-space()='There is 1 error']"
    errortext2 = "//p[normalize-space()='There are 3 errors']"
    errorlist = "//div[@class='alert alert-danger']//ol//li"


    def __init__(self , driver):
        self.driver = driver

    def radiobutton1(self):
         self.driver.find_element("id", self.radio1).click()

    def firstname1(self):
        self.driver.find_element("id", self.firstname).clear()
        return self.driver.find_element("id", self.firstname)

    def lastname1(self):
        self.driver.find_element("id", self.lastname).clear()
        return self.driver.find_element("id", self.lastname)

    def password1(self):
        self.driver.find_element("id", self.password).clear()
        return self.driver.find_element("id", self.password)

    def address01(self):
        self.driver.find_element("id", self.address1).clear()
        return self.driver.find_element("id", self.address1)

    def city01(self):
        self.driver.find_element("id", self.city).clear()
        return self.driver.find_element("id", self.city)

    def postalcode01(self):
        self.driver.find_element("id", self.pcode).clear()
        return self.driver.find_element("id", self.pcode)

    def mobile1(self):
        self.driver.find_element("id", self.mobile).clear()
        return self.driver.find_element("id", self.mobile)

    def refer01(self):
        self.driver.find_element("id", self.refer1).clear()
        return self.driver.find_element("id", self.refer1)

    def registersubmit(self):
        return self.driver.find_element("id", self.registerbutton).click()

    def fnameerror(self):
        return self.driver.find_element(By.XPATH, self.firstnameerror).text

    def texterror1(self):
        return self.driver.find_element(By.XPATH, self.errortext1).text

    def texterror2(self):
        return self.driver.find_element(By.XPATH, self.errortext2)

    def sizeoferrorlist(self):
        a = len(self.driver.find_elements(By.XPATH, self.errorlist))
        if a > 1:
            return "There are "+ str(a)+ " errors"
        else:
            return "There is 1 error"












