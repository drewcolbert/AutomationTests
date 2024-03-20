
# ^ using all of the functions from the 'HelperFunctions.py' script, I want to test every step involved 
# ^ this scripts takes the actual xpath inputs from the site
from HelperScript import HelperFunctions
import pytest


@pytest.mark.usefixtures("CreateDriver")
class TestRegisterNewUser(HelperFunctions):

    def test_OpenBrowser(self):
        self.GoToURL("https://parabank.parasoft.com/parabank/index.htm", self.driver)
    
    def test_ClickRegisterLink(self):
        self.ClickElement("//*[@id='loginPanel']/p[2]/a", self.driver)
    
    def test_InputFields(self):
        self.WaitForURL("https://parabank.parasoft.com/parabank/register.htm", self.driver)

        fields = self.FindElements(self.driver)
        for field in fields:
            field_name = field.get_attribute("id")
            if field_name == "customer.username":
                self.InputText(XPATH = "//*[@id='customer.username']", driver = self.driver, input_text = "username")
            elif field_name == "customer.password":
                self.InputText(XPATH = "//*[@id='customer.password']", driver = self.driver, input_text = "password")
            elif field_name == "repeatedPassword":
                self.InputText(XPATH = "//*[@id='repeatedPassword']", driver = self.driver, input_text = "password")
            else:
                self.InputText(XPATH = f"//*[@id='{field_name}']", driver = self.driver)
    
    def test_ClickRegisterButton(self):
        self.ClickElement("//*[@id='customerForm']/table/tbody/tr[13]/td[2]/input", self.driver)

    def test_ConfirmMessage(self):
        message = "Your account was created successfully. You are now logged in."
        assert self.ReturnMessage("//*[@id='rightPanel']/p", self.driver) == message
        print("Proper Message Showed Up. Good to go.")




