from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_data.testdata import Inputs,Selectors


class Check_Admin_module:


    def __init__(self,driver):
        self.driver = driver

    def login_with_username_pswd(self,username,password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, Selectors.text_box_username_xpath))).send_keys(username)
        self.driver.find_element(By.XPATH, Selectors.text_box_pswd_xpath).send_keys(password)
        self.driver.find_element(By.XPATH, Selectors.login_button_xpath).click()

    def click_Admin(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, Selectors.Admin_element))).click()

