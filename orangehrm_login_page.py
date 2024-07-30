from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class OrangeHRMLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def load(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, username, password):
        try:
            username_input = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password_input = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

            username_input.send_keys(username)
            password_input.send_keys(password)
            login_button.click()

            return self.wait.until(EC.presence_of_element_located((By.ID, "welcome"))).is_displayed()
        except TimeoutException:
            return False