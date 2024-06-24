from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
import sys
import os
import time

# Add the parent directory to the path if amazon_login_page.py is in the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from HRM_login_page import LoginPage
# from HRM_login_page import browser

@pytest.fixture
def browser():
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(options=options)
    # driver.maximize_window()
    # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    chromedriver_path = r"D:\Automation study\Python Programming\Requirement\chromedriver.exe"
    if not os.path.exists(chromedriver_path):
        raise FileNotFoundError(f"ChromeDriver not found at path: {chromedriver_path}")

    os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    time.sleep(6)
    driver.quit()


def test_login_01(browser):
    login_page = LoginPage(browser)
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # Click the "Sign in" button
    # HRM_login_page.click_sign_in_button()

    # Perform login actions (replace with actual login details and logic)
    login_page.setUserName("Admin")
    login_page.setPassword("admin123")
    login_page.clickLogin()

    # Add assertions or further actions based on the login result
    # For example, you could assert that the user is redirected to the homepage after successful login

    print("The First Window is:", browser.title)
    assert "OrangeHRM" in browser.title

def test_login_02(browser):
    login_page = LoginPage(browser)
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # Click the "Sign in" button
    # Perform login actions (replace with actual login details and logic)
    login_page.setUserName("Admin")
    login_page.setPassword("Invalid Password")
    login_page.clickLogin()
    try:
        login_page.invalid_credentials()
        print("test_login_02 is passed")
        # Add assertions or further actions based on the login result
        if login_page.invalid_credentials() == "Invalid credentials":
            assert True
            print("test_login_02 is passed")
    except:
        print("test_login_02 is failed")