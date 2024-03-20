import pytest
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options as CHOptions
from selenium.webdriver.edge.options import Options as EDGEOptions
from selenium.webdriver.firefox.options import Options as FFOptions

@pytest.fixture(scope = "class")
def CreateDriver(request):

    supported_browsers = ["chrome", "edge", "firefox", "headlessedge", "headlesschrome", "headlessfirefox"]
    
    # this gets the browser that the user is currently using
    # this is a dictionary, when we use .get on a dictionary it will find that key and return it, if it does not exist, returns NONE
    # if the browser does not exist, we raise an exception saying to set the browser
    browser = os.environ.get("BROWSER")
    if not browser:
        raise Exception("To set broswer. Type 'set browser=edge' in the command prompt.")
    
    # make the broswer lowercase, if it is not found in our supported browsers list, raise an exception
    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Current browser {browser} not supported. Supported browsers: {supported_browsers}.")
    
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    
    # we can add options for headless browsers
    # a headless browser just means that the window will not actually open when the test is running
    elif browser == "headlesschrome":
        chrome_options = CHOptions()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options = chrome_options)
    
    elif browser == "headlessedge":
        edge_options = EDGEOptions()
        edge_options.add_argument("--disable-gpu")
        edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--headless")
        driver = webdriver.Edge(options = edge_options)
    
    elif browser == "headlessfirefox":
        firefox_options = FFOptions()
        firefox_options.add_argument("--disable-gpu")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options = firefox_options)

    request.cls.driver = driver

    yield

    driver.quit()