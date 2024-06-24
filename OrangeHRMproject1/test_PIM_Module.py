import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import sys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
import sys
import os
import time
import random

# Add the parent directory to the path if amazon_login_page.py is in the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from HRM_login_page import LoginPage
from HRM_login_page import PIM

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

def test_PIM_01(browser):

    login_page = LoginPage(browser)
    login_page1 = PIM(browser)
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # Click the "Sign in" button
    # HRM_login_page.click_sign_in_button()
    login_page.setUserName("Admin")
    login_page.setPassword("admin123")
    login_page.clickLogin()
    # Click the "PIM" button to add Employee
    login_page1.select_PIM()
    login_page1.select_Add_Employee()
    login_page1.set_first_name("Vignesh")
    login_page1.set_mid_name("B")
    login_page1.set_last_name("Bala")
    emp_id1 = (random.randint(3000, 9000))
    emp_id = emp_id1
    login_page1.set_emp_id(emp_id)
    login_page1.select_save_employee()
    try:
        login_page1.emp_added_success()
        print("test_PIM_01 is passed")
    # Add assertions or further actions based on the login result
        if login_page1.emp_added_success() == "Success Successfully Saved ×":
            assert True
            print("test_PIM_01  is passed")

    except:
        assert False

def test_PIM_02(browser):

    login_page = LoginPage(browser)
    login_page1 = PIM(browser)
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # Click the "Sign in" button
    # HRM_login_page.click_sign_in_button()
    login_page.setUserName("Admin")
    login_page.setPassword("admin123")
    login_page.clickLogin()
    # Click the "PIM" button to add Employee
    login_page1.select_PIM()
    login_page1.select_Add_Employee()
    login_page1.set_first_name("Vignesh")
    login_page1.set_mid_name("B")
    login_page1.set_last_name("Bala")
    emp_id1 = (random.randint(3000, 9000))
    emp_id = emp_id1
    login_page1.set_emp_id(emp_id)
    login_page1.select_save_employee()
    time.sleep(10)
    # perform edit operation of Employee_List
    login_page1.select_Employee_List()
    time.sleep(10)
    login_page1.set_Employee_Id(emp_id)
    time.sleep(10)
    login_page1.select_search()
    login_page1.select_edit()
    login_page1.set_Driving_license("987654321")
    login_page1.set_license_Expiry("2029-09-10")
    login_page1.select_save()
    try:
        login_page1.emp_edited_success()
        print("test_PIM_02 is passed")
    # Add assertions or further actions based on the login result
        if login_page1.emp_edited_success() == "Success Successfully Saved ×":
            assert True
            print("test_PIM_02  is passed")

    except:
        assert False

def test_PIM_03(browser):

    login_page = LoginPage(browser)
    login_page1 = PIM(browser)
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page.setUserName("Admin")
    login_page.setPassword("admin123")
    login_page.clickLogin()
    # Click the "PIM" button to add Employee
    login_page1.select_PIM()
    login_page1.select_Add_Employee()
    login_page1.set_first_name("Vignesh")
    login_page1.set_mid_name("B")
    login_page1.set_last_name("Bala")
    emp_id1 = (random.randint(3000, 9000))
    emp_id = emp_id1
    login_page1.set_emp_id(emp_id)
    login_page1.select_save_employee()
    time.sleep(10)
    login_page1.select_Employee_List()
    time.sleep(10)
    login_page1.set_Employee_Id(emp_id)
    time.sleep(10)
    login_page1.select_search()
    # perform delete operation of Employee_List
    login_page1.select_delete()
    time.sleep(10)
    whandle = browser.window_handles[0]
    browser.switch_to.window(whandle)
    time.sleep(10)
    login_page1.select_wndow_delete()

    try:
        login_page1.emp_deleted_success()
        print("test_PIM_03 is passed")
    # Add assertions or further actions based on the login result
        if login_page1.emp_deleted_success() == "Success Successfully Deleted ×":
            assert True
            print("test_PIM_03  is passed")

    except:
        assert False


