# Register For A New Account

## Summary
This framework aims to test the creation of a new account for a banking website. This test supports Edge, Chrome, and Firefox browsers and is able to generate random values for the account creation so no duplicates can occur. 

## File Structure
In this repository you will find the following structure:

-> RegisterNewUser_test <br>
&emsp;&emsp;-> test_module <br>
&emsp;&emsp;&emsp;&emsp;-> Helpers <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-> `__init__`.py <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-> `HelperScript.py` <br>
&emsp;&emsp;&emsp;&emsp;-> `register-new-user_test.py` <br>
&emsp;&emsp;-> venv <br>
&emsp;&emsp;-> `conftest.py` 
<br>
<br>


## File Summary
-- `conftest.py`

This file contains our fixture that is used create our driver. This driver is used by our actual test file and allows us to access the browser that the user chooses. A fixture allows us to have all of our test classes access a browser without have to instatiate it in every class.
<br>
<br>
-- `HelperScript.py`

This files contains all of our useful functions that perform the actual actions of the test. Examples include opening the browser, finding an element, inputting text to an input field, etc. This file does not include any actual element paths or any testing logic. This is simply to make it easier and cleaner to write our test methods. The test class will inherit all of the methods and attributes from this class. 
<br>
<br>
--`register-new-user_test.py`

This file houses the actual testing class with the methods to be testing. Each method corresponds to a step in the testing process and will be tested through pytest. This class holds the actual XPATH variables and URLs and any other inputs to the `HelperScript.py` class that we inherited. 


## Set Up
1. Download the files and add them to a directory. **IMPORTANT:** Make sure the folder that contains `register-new-user_test.py` ends with '_test'. This is how pytest knows where to look. 

#### Windows
2. Open the start menu, type 'cmd' and open the command prompt
3. Change the current directory to the one that holds `register-new-user_test.py` by typing: `cd "\your-file-path\"`
4. Activate the virtual environment: `.\venv\Scripts\Activate`
5. Set the browser you want to use. Supported browsers include: *(edge, chrome, firefox, headlessedge, headlesschrome, headlessfirefox):* `set browser=edge`
6. Run pytest: `pytest`
<br>


#### Mac
2. Open the terminal. Press `cmd + space` and type "Terminal" to open it
3. Change the current directory to the one that holds `register-new-user_test.py` by typing: `cd "\your-file-path\"`
4. Activate the virtual environment: `source "your-project-path"/venv/bin/activate`
5. Set the browser you want to use. Supported browsers include: *(edge, chrome, firefox, headlessedge, headlesschrome, headlessfirefox):* `export browser=edge`
6. Run pytest: `pytest`
<br>
<br>
<br>

## Test Walkthrough

**1. Go to the following URL: https://parabank.parasoft.com/parabank/index.htm**

![Home-Page](/test/RegisterNewUser_test/images/home_screen.jpeg)

**2. Click on the "Register" link**

![Register-Link](/test/RegisterNewUser_test/images/register-link.jpeg)

**3. Change the scope to this new page link**

![New-URL](/test/RegisterNewUser_test/images/new_url.jpeg)

**4. Find all of the input fields and fill out these fields** <br>
&emsp;&emsp;NOTE: Inputs are random everytime so no duplicate accounts are created

![Input-Fields](/test/RegisterNewUser_test/images/input_fields.jpeg)

**5. Click on "Register" button**

![Register-Button](/test/RegisterNewUser_test/images/register-button.jpeg)

<br>
<br>

**6. Confirm the follow message in present:** `Your account was created successfully. You are now logged in.`

![Error-Message](/test/RegisterNewUser_test/images/error-message.jpeg)





