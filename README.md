# Parabank Testing Repository
Automated testing framework contain various front end, end-to-end tests using Selenium and Python. 
These tests are in place to ensure that each element of the webiste is working as expected from a user perspective. 
This repository contains both smoke and end-to-end tests, you can decide which one to run my declaring a mark *(more imformation below).*
<br>

**NOTE: This repository is being consistantly updated as more tests are completed. This is a work in progess!**
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

## How to Use
1. Download the repository zip file or clone this repository

#### Windows
2. Open the start menu, type 'cmd' and open the command prompt
3. Change the current directory to the one that holds the repository folder by typing: `cd "\your-file-path\"`
4. Activate the virtual environment: `.\venv\Scripts\Activate`
5. Set the browser you want to use. Supported browsers include: *(edge, chrome, firefox, headlessedge, headlesschrome, headlessfirefox):* `set browser=edge`
6. Run pytest: `pytest`
<br>


#### Mac
2. Open the terminal. Press `cmd + space` and type "Terminal" to open it
3. Change the current directory to the one that holds the repository folder by typing: `cd "\your-file-path\"`
4. Activate the virtual environment: `source "your-project-path"/venv/bin/activate`
5. Set the browser you want to use. Supported browsers include: *(edge, chrome, firefox, headlessedge, headlesschrome, headlessfirefox):* `export browser=edge`
6. Run pytest: `pytest`
<br>
<br>

**NOTE: This method will run every single test in the repository, use marks to narrow down which tests to run**


## Marks guide

### Using marks
In the command line, when you run `pytest` you can add the mark name as an argument --- `pytest -m mark-name`. <br>
Simply replace the 'mark-name' with a mark listed below.
<br>
<br>

## Tests

Date Added - 2024-03-19 <br>
Marks - RegisterNewUser | EndToEnd <br>
To run - `pytest -m RegisterNewUser` <br>
[Register a New User](https://github.com/drewcolbert/Python-Automation-Tests/tree/main/test/RegisterNewUser_test)
