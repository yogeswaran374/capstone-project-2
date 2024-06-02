from selenium import webdriver
from POM_pages.Admin_module import Check_Admin_module
from Test_data.testdata import Inputs,Selectors
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_002_Admin_module_testcases:

    def test_current_title(self,setup):
        self.driver = setup
        self.driver.get(Inputs.base_url)
        self.driver.maximize_window()
        self.login = Check_Admin_module(self.driver)
        self.login.login_with_username_pswd(Inputs.username,Inputs.password)
        self.login.click_Admin()
        exp_title = "OrangeHRM"
        assert exp_title == self.driver.title, "current page is in Admin module"


    def test_validate_Admin_page(self,setup):
        self.driver = setup
        self.driver.get(Inputs.base_url)
        self.driver.maximize_window()
        self.login = Check_Admin_module(self.driver)
        self.login.login_with_username_pswd(Inputs.username, Inputs.password)
        self.login.click_Admin()
        wait = WebDriverWait(setup, 10)
        headers_elements = wait.until(EC.visibility_of_element_located((By.XPATH, Selectors.Admin_page_Headers_elements)))
        headers = headers_elements.text
        exp_list_in_headers = ["User Management", "Job", "Organization", "Qualifications", "Nationalities", "Corporate Branding", "Configuration"]
        list_in_headers = []

        for elements in exp_list_in_headers:
            if elements in headers:
                list_in_headers.append(elements)
        assert exp_list_in_headers == list_in_headers







