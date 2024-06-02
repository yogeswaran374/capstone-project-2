from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_data.testdata import Inputs,Selectors


class Login:


    def __init__(self,driver):
        self.driver = driver

    def click_forget_pswd(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.forget_password_element_xpath))).click()

    def enter_user_name(self,username):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, Selectors.text_box_username_xpath))).send_keys(username)

    def click_reset_button(self):
        self.driver.find_element(By.XPATH, Selectors.Reset_button_xpath).click()





