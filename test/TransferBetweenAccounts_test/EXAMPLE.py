

'''

This script is here to test out all of these elements and how we access them. This is not a test, 
but rather a way to confirm our tests are doing what I expect them to be doing without have to run pytest each time

'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium import webdriver


driver = webdriver.Edge()
driver.get("https://parabank.parasoft.com/parabank/index.htm")

driver.find_element(By.XPATH, "//*[@id='loginPanel']/form/div[1]/input").send_keys("john")
driver.find_element(By.XPATH, "//*[@id='loginPanel']/form/div[2]/input").send_keys("demo")
driver.find_element(By.XPATH, "//*[@id='loginPanel']/form/div[3]/input").click()

WebDriverWait(driver, 10).until(EC.url_contains("https://parabank.parasoft.com/parabank/overview.htm"))
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/table/tbody/tr")))
x = driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/table/tbody/tr")
p = {}
for index, elem in enumerate(x):
    if index == len(x) - 1:
        pass
    else:
        account = elem.text.split()
        p[account[0]] = float(account[2].replace("$", ""))


driver.find_element(By.XPATH, "//*[@id='leftPanel']/ul/li[1]/a").click()
WebDriverWait(driver, 10).until(EC.url_contains("https://parabank.parasoft.com/parabank/openaccount.htm"))

dropdown = driver.find_elements(By.XPATH, "//*[@id='fromAccountId']")
print(dropdown)
for option in dropdown:
    print(option.text)

dropdown_obj = Select(driver.find_element(By.XPATH, "//*[@id='fromAccountId']"))
for x in dropdown_obj.options:
    print(x.text)
    print(p[str(x.text)])

driver.close()