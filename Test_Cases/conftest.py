from selenium import webdriver
import pytest 

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        # ops=webdriver.ChromeOptions()
        # ops.add_argument("--headless=new")
        driver=webdriver.Chrome()
    elif browser=="edge":
        driver=webdriver.Edge()
    else:
        driver=webdriver.Chrome()

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# def pytest_configure(config):
#     config._metadata["Project Name"]="nop commerce"
#     config._metadata["Module"]="Login"
#     config._metadata["Tester"]="Pruthvi"

def pytest_configure(config):
    config._metadata={
        "Project Name": "My Project",
        "Module": "Login",
        "Tester": "Pruthvi"}
    
def pytest_metadata(metadata):
    metadata.pop("package",None)
    metadata.pop("plugin",None)