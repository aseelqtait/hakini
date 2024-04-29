#all file in tests directory can show this file => because in the same package
# This file acts as a plugin and is automatically discovered by pytest.
from _pytest.fixtures import FixtureRequest
import pytest
from selenium import webdriver
@pytest.fixture(scope="function")
def driver(request: FixtureRequest):
    browser = request.config.getoption("--browser")  # Retrieving the Browser Option: The fixture
     #retrieves the value of the --browser command-line option using
    # request.config.getoption("--browser").
    if browser == "chrome":  #If the --browser option is set to "chrome",
        # it creates an instance of the webdriver.Chrome() class, representing the Chrome browser.
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser should be 'chrome' or 'firefox'")

    yield driver #The yield statement acts as a separator
    # between the setup and teardown phases of the fixture.
    driver.quit()
#  pytest_addoption function adds a custom command-line option --browser,
# which allows you to specify the browser type to be used during test execution.
# By defining the pytest_addoption function, pytest automatically adds
# the --browser option to the available command-line options, (pytest --browser firefox=>>in terminal)
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify the browser to use: chrome or firefox")
# function filters the collected test items based on their parent object names
# and adds the pytest.mark.usefixtures("driver") marker to the matching items
def pytest_collection_modifyitems(config, items):
    for item in items:
        if item.parent.name == "LoginPage" or item.parent.name == "SearchPge" or item.parent.name == "registerPage":
            item.add_marker(pytest.mark.usefixtures("driver"))
# "TestLogin"
@pytest.fixture(scope="function", autouse=True)
def open_url(driver):
    driver.get("https://www.hakini.net/")
# ///////////////////////////////////////////////
# By using hook functions, you can tailor pytest to fit your specific testing needs
# and incorporate custom logic or integrations into the testing process.
# ///////////////////////////////////////////////
 
