
# ^ using all of the functions from the 'HelperFunctions.py' script, I want to test every step involved 
# ^ this scripts takes the actual xpath inputs from the site
from HelperScript import HelperFunctions
import pytest


@pytest.mark.usefixtures("CreateDriver")
@pytest.mark.RegisterNewUser
@pytest.mark.EndToEnd
class TestRegisterNewUser(HelperFunctions):

    # go to the home page of the site
    def test_OpenBrowser(self):
        self.GoToURL("https://parabank.parasoft.com/parabank/index.htm", self.driver)
    
    # click on register
    def test_ClickRegisterLink(self):
        self.ClickElement("//*[@id='loginPanel']/p[2]/a", self.driver)
    
    # we need to input a bunch of information in order to create the account
    # however there are a couple of special fields we want to keep track of: username and password
    # the username is one we want to save so we can sign back in if we need to
    # the password needs to be inserted twice so we need to track that as well
    # when we get to these fields, we need to handle them correctly
    def test_InputFields(self):

        # when we register, the url changes so we need to wait for that url to be present
        self.WaitForURL("https://parabank.parasoft.com/parabank/register.htm", self.driver)

        # find each input element and make sure we know which ones are username and password, input the appropriate text
        # ! fortunately there is no requirement that our inputs need a certain structure, so we can input random text
        fields = self.FindElements("//td//input[@class='input']", self.driver)
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
    
    # click the registration button to create our account
    def test_ClickRegisterButton(self):
        self.ClickElement("//*[@id='customerForm']/table/tbody/tr[13]/td[2]/input", self.driver)

    # confirm that we have successfully created the account by asseting we see the expected message
    def test_ConfirmMessage(self):
        message = "Your account was created successfully. You are now logged in."
        assert self.ReturnMessage("//*[@id='rightPanel']/p", self.driver) == message
        print("Proper Message Showed Up. Good to go.")




