
from HelperScript import HelperFunctions
import pytest


@pytest.mark.usefixtures("CreateDriver")
@pytest.mark.TransferFunds
@pytest.mark.EndToEnd
class TestBalanceTransfer(HelperFunctions):
    account_nums = []
    account_amounts = []
    accounts = {}
    new_account_num = None

    def test_OpenBrowser(self):
        self.GoToURL("https://parabank.parasoft.com/parabank/index.htm", self.driver)

    def test_SignIn(self):
        self.InputCustomText("//*[@id='loginPanel']/form/div[1]/input", self.driver, "john")
        self.InputCustomText("//*[@id='loginPanel']/form/div[2]/input", self.driver, "demo")
        self.ClickElement("//*[@id='loginPanel']/form/div[3]/input", self.driver)
    
    def test_GetAccountValues(self):
        self.WaitForURL("https://parabank.parasoft.com/parabank/overview.htm", self.driver)

        account_rows = self.FindElements("//tbody//tr[@class = 'ng-scope']//td", self.driver)
        for index, row in enumerate(account_rows):
            if index % 3 == 0:
                self.account_nums.append(row.text)
            elif index % 3 == 1:
                self.account_amounts.append(row.text)
            else:
                pass
        
        for i in range(0, len(self.account_nums)):
            self.accounts[self.account_nums[i]] = self.account_amounts[i]

    
    def test_OpenNewAccount(self):
        self.ClickElement("//*[@id='leftPanel']/ul/li[1]/a", self.driver)
        self.WaitForURL("https://parabank.parasoft.com/parabank/openaccount.htm", self.driver)
        dropdown = self.ActivateDropdown("//*[@id='fromAccountId']", self.driver)
        for option in dropdown.options:
            if self.accounts[option.text] >= 100:
                self.ActivateDropdown("//*[@id='fromAccountId']", self.driver).select_by_visible_text(option.text)
            else:
                pass
        
        message = self.ReturnMessage("//*[@id='rightPanel']/div/div/p[1]", self.driver)

        assert message == "Congratulations, your account is now open."

        self.new_account_num = self.FindElement("//*[@id='newAccountId']", self.driver).text

    def test_MakeTransfer(self):
        self.ClickElement("//*[@id='leftPanel']/ul/li[3]/a", self.driver)
        self.WaitForURL("https://parabank.parasoft.com/parabank/transfer.htm", self.driver)

        self.InputCustomText("//*[@id='amount']", self.driver, "50")
        dropdown = self.ActivateDropdown("//*[@id='fromAccountId']", self.driver)
        for option in dropdown.options:
            if self.accounts[option.text] >= 100:
                self.ActivateDropdown("//*[@id='fromAccountId']", self.driver).select_by_visible_text(option.text)
            else:
                pass
        
        self.ActivateDropdown("//*[@id='toAccountId']", self.driver).select_by_visible_text(str(self.new_account_num))
        self.ClickElement("//*[@id='rightPanel']/div/div/form/div[2]/input", self.driver)

        message = self.ReturnMessage("//*[@id='rightPanel']/div/div/h1", self.driver)
        
        assert message == "Transfer Complete!"