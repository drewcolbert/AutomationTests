
# ^ this script is intended to be used as a package
# ^ these functions will find all of the elements and do all of this thing sneeded for this test
# ^ I am going to import this into my testing script and use all of these functions

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import random


class HelperFunctions:

    default_wait = 3
    random_text = ''.join(random.sample("abcdefghijklmnopqrstuvwxyz", random.randint(3, 8)))
    username = ''.join(random.sample("abcdefghijklmnopqrstuvwxyz", random.randint(3, 8)))
    password = ''.join(random.sample("abcdefghijklmnopqrstuvwxyz", random.randint(3, 8)))

    def GoToURL(self, url, driver):
        driver.get(url)

    def FindElement(self, XPATH, driver):
        elem = driver.find_element(By.XPATH, XPATH)
        return elem

    def FindElements(self, driver):
        elements = driver.find_elements(By.XPATH, "//td//input[@class='input']")
        return elements

    def WaitForElement(self, XPATH, driver, wait_input = default_wait):
        wait_time = wait_input
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, XPATH)))

    def WaitForElementClickable(self, XPATH, driver, wait_input = default_wait):
        wait_time = wait_input
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, XPATH)))

    def WaitForURL(self, url, driver, wait_input = default_wait):
        wait_time = wait_input
        WebDriverWait(driver, wait_time).until(EC.url_contains(url))

    def InputText(self, XPATH, driver, input_text = "random"):
        if input_text == "username":
            text = self.username
        elif input_text == "password":
            text = self.password
        else:
            text = self.random_text

        elem = self.FindElement(XPATH, driver)
        elem.send_keys(text)
    
    def InputCustomText(self, XPATH, driver, text):
        elem = self.FindElement(XPATH, driver)
        elem.send_keys(text)        

    def ClickElement(self, XPATH, driver):
        self.WaitForElementClickable(XPATH, driver)
        elem = self.FindElement(XPATH, driver)
        elem.click()

    def ReturnMessage(self, XPATH, driver):
        self.WaitForElement(XPATH, driver)
        elem = self.FindElement(XPATH, driver).text
        return elem
    
    def ActivateDropdown(self, XPATH, driver):
        dropdown = self.FindElement(XPATH, driver)
        dropdown_object = Select(dropdown)
        return dropdown_object
    













