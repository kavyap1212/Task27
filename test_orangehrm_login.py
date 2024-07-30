import pytest
from selenium import webdriver
import pandas as pd
from datetime import datetime
from orangehrm_login_page import OrangeHRMLoginPage
import os

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_orangehrm_login(driver):
    file_path = os.path.abspath('login_data.xlsx')
    
    try:
        df = pd.read_excel(file_path)
    except PermissionError:
        pytest.fail("Permission denied: Ensure the file is not open in another application and the script has necessary permissions.")

    for index, row in df.iterrows():
        test_id = row['Test ID']
        username = row['Username']
        password = row['Password']
        date = datetime.now().strftime("%Y-%m-%d")
        time_of_test = datetime.now().strftime("%H:%M:%S")
        tester_name = row['Name of Tester']

        page = OrangeHRMLoginPage(driver)
        page.load()
        
        is_logged_in = page.login(username, password)
        result = "Passed" if is_logged_in else "Failed"
        
        df.at[index, 'Date'] = date
        df.at[index, 'Time of Test'] = time_of_test
        df.at[index, 'Test Result'] = result

    try:
        df.to_excel(file_path, index=False)
    except PermissionError:
        pytest.fail("Permission denied: Ensure the file is not open in another application and the script has necessary permissions.")