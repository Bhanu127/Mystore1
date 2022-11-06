import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def wait1(self, duration, webelement):
        wait = WebDriverWait(self.driver, duration)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, webelement)))

    def wait2(self, duration, webelement):
        wait = WebDriverWait(self.driver, duration)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, webelement)))

    def wait3(self, duration, webelement):
        wait = WebDriverWait(self.driver, duration)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, webelement)))

    def mousehover1(self,webelement):
        action = ActionChains(self.driver)
        action.move_to_element(webelement).click().perform()

    def mousehover2(self,webelement):
        action = ActionChains(self.driver)
        action.move_to_element(webelement).perform()

    def idselect1(self,webelement,value):
        dropdown = Select(self.driver.find_element("id", webelement))
        return dropdown.select_by_value(value)

    def idselect2(self,webelement,value):
        dropdown = Select(self.driver.find_element("id", webelement))
        return dropdown.select_by_visible_text(value)

    def compareproducttext1(self, a, b):
        if a == b:
            assert True
        else:
            assert False

    def compareproducttext2(self, a, b, c):
        if a == b == c:
            assert True
            self.log.info("******Both values are equal********")
        else:
            self.log.error("*******Both values are not equal********")
            assert False

    def listvalue(self, a):
        list = []
        for i in a:
            list.append(i.text)
        return list[1:len(a)-1]


