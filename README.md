# StringFinder
Module that searches an array of strings for matches with input string. Character order is not relevant.

## Assumptions:
The case of the characters in the strings matter. 'C' != 'c'.
The array should only contain strings.
There is no main function in the file, only the class. The class is to used as a module. The test file imports the module for testing.

## Usage:
string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm']

finder = Finder(string_list)

finder.find("sad") will return and array ["asd"]

## To Run tests:
Ensure Python3, pip and virtualenv are installed
* Run "git clone https://github.com/cathalryan9/StringFinder.git"
* Run "cd StringFinder"
* Run "virtualenv venv" (This creates a virtual environment for your system configuration is not effected by installing/updating new packages  )
* If on Windows run "venv\Scripts\activate.bat". On Mac/Linux run "source venv/bin/activate" 
* Run "pip install -r requirements.txt"
* Run "py.test" (ensure it is run from the base directory i.e same directory as Finder.py)

## Why Pytest?
* Pytest is a commonly used framework in the python community. As a result, there are many resources online that would help when developing tests.
* One downside is that it is not part of the standard Python library and must be downloaded manually. 
* Very little set up is required to write tests and makes them easier to understand. By storing tests in the "test" directory and ensuring test names have "test_" appended at the start it is simple to run the tests. This is done by running "py.test" in the command window.
* It gives good level feedback from failures and also provides colour in the output for better readability.
* If our application was to grow we can add additional suites. When the app become more complex we can mock objects and test these rather than actually creating them through the system.
* Overall, it is a decent framework that provides a high level of functionality. As a result, it is the most popular Python test framework.
