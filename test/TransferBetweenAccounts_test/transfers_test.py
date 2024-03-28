
from HelperScript import HelperFunctions
import pytest
import time


@pytest.mark.usefixtures("CreateDriver")
@pytest.mark.TransferFunds
@pytest.mark.EndToEnd
class TestBalanceTransfer(HelperFunctions):
    
    accounts_dict = {}
    new_account_num = None

    # go to the website home page
    def test_OpenBrowser(self):
        self.GoToURL("https://parabank.parasoft.com/parabank/index.htm", self.driver)
        time.sleep(5)
    # sign in using the username = "john" and password = "demo"
    def test_SignIn(self):
        self.InputCustomText("//*[@id='loginPanel']/form/div[1]/input", self.driver, "john")
        self.InputCustomText("//*[@id='loginPanel']/form/div[2]/input", self.driver, "demo")
        self.ClickElement("//*[@id='loginPanel']/form/div[3]/input", self.driver)
    
    '''
    # get all accounts under this user
    def test_GetAccountValues(self):

        # when we sign in, it takes us right to the account overview, before we do anything, we need to wait for this url to load
        self.WaitForURL("https://parabank.parasoft.com/parabank/overview.htm", self.driver)

        # wait for all elements of the account table to be present as well
        self.WaitForAllElements("/html/body/div[1]/div[3]/div[2]/div/div/table/tbody/tr", self.driver)

        # the accounts are displayed in a table with the layout of: account number | account amount | available balance
        # accounts is a list of all rows in the table
        accounts = self.FindElements("/html/body/div[1]/div[3]/div[2]/div/div/table/tbody/tr", self.driver)

        # the last row is just a summary of the total, we dont want that and its ALWAYS the last row
        # if the index in our list is the final one, ignore it and move on
        # for every other row, I want to add it to the dictionary with the account as the key and the available balance as the value
        # * NOTE: i want available balance, not total amount because total amount has pending transactions and the account can be negative or not 100% accurate
        for index, elem in enumerate(accounts):
            if index == len(accounts) - 1:
                pass
            else:
                account = elem.text.split()
                self.accounts_dict[account[0]] = float(account[2].replace("$", ""))
        time.sleep(5)
        import pdb; pdb.set_trace()
    
    '''
    # in order to transfer between accounts, we need more than one account
    # this method creates a new account that we can transfer to
    def test_OpenNewAccount(self):
        # when we sign in, it takes us right to the account overview, before we do anything, we need to wait for this url to load
        self.WaitForURL("https://parabank.parasoft.com/parabank/overview.htm", self.driver)

        # wait for all elements of the account table to be present as well
        self.WaitForAllElements("/html/body/div[1]/div[3]/div[2]/div/div/table/tbody/tr", self.driver)

        # the accounts are displayed in a table with the layout of: account number | account amount | available balance
        # accounts is a list of all rows in the table
        accounts = self.FindElements("/html/body/div[1]/div[3]/div[2]/div/div/table/tbody/tr", self.driver)

        # the last row is just a summary of the total, we dont want that and its ALWAYS the last row
        # if the index in our list is the final one, ignore it and move on
        # for every other row, I want to add it to the dictionary with the account as the key and the available balance as the value
        # * NOTE: i want available balance, not total amount because total amount has pending transactions and the account can be negative or not 100% accurate
        for index, elem in enumerate(accounts):
            if index == len(accounts) - 1:
                pass
            else:
                account = elem.text.split()
                self.accounts_dict[account[0]] = float(account[2].replace("$", ""))

        # click on the 'Open New Account' link
        self.ClickElement("//*[@id='leftPanel']/ul/li[1]/a", self.driver)

        # wait for the URL
        self.WaitForURL("https://parabank.parasoft.com/parabank/openaccount.htm", self.driver)

        # wait for the dropdown element to be present
        self.WaitForElement("//*[@id='fromAccountId']", self.driver)

        # activate the dropdown element
        dropdown = self.ActivateDropdown("//*[@id='fromAccountId']", self.driver)

        # in order to open an account, we need an active account with at least $100 in it, thats why we got those account values   
        # for every option available, if that option has more than $100 in it, select it and then stop the loop
        # * in our case, the first valid account is fine
        import pdb; pdb.set_trace()
        for option in dropdown.options:
            if self.accounts_dict[str(option.text)] >= 100:
                dropdown.select_by_value(option.text)
                # subtract 100 from the current account
                self.accounts_dict[str(option.text)] -= 100
                break
            else:
                pass
            
        # there will be a confirmation message, if we get this message than all is well
        message = self.ReturnMessage("//*[@id='rightPanel']/div/div/p[1]", self.driver)

        assert message == "Congratulations, your account is now open."

        # we will need to new account number for later, we save it to this variable
        self.new_account_num = self.FindElement("//*[@id='newAccountId']", self.driver).text
            
    # make the transfer from one account to the new one
    def test_MakeTransfer(self):

        # click the "Make a Transfer" button
        self.ClickElement("//*[@id='leftPanel']/ul/li[3]/a", self.driver)

        # wait for the correct URL
        self.WaitForURL("https://parabank.parasoft.com/parabank/transfer.htm", self.driver)

        # in our amount to be transferred, we only want to transfer 50
        self.InputCustomText("//*[@id='amount']", self.driver, "50")

        # this is a similar process to above
        # for each available account, the first one that has enough money will be select
        # this drop down is the one that we want to take money from
        dropdown = self.ActivateDropdown("//*[@id='fromAccountId']", self.driver)
        for option in dropdown.options:
            if self.accounts_dict[str(option.text)] >50:
                dropdown.select_by_value(option.text)
                self.accounts_dict[str(option.text)] -= 50
                break
            else:
                pass
        
        # this dropdown is the one we want to put into
        self.ActivateDropdown("//*[@id='toAccountId']", self.driver).select_by_value(str(self.new_account_num))

        # click transfer and confirm that we see the confirmation message
        self.ClickElement("//*[@id='rightPanel']/div/div/form/div[2]/input", self.driver)

        message = self.ReturnMessage("//*[@id='rightPanel']/div/div/h1", self.driver)
        
        assert message == "Transfer Complete!"


