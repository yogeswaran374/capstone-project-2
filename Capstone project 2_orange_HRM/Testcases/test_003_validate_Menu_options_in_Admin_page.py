from selenium import webdriver
from POM_pages.Admin_module import Check_Admin_module
from Test_data.testdata import Inputs,Selectors
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_003_Admin_page_Menu_Options:


    def test_validate_Admin_page_menu_options(self,setup):
        self.driver = setup
        self.driver.get(Inputs.base_url)
        self.driver.maximize_window()
        self.login = Check_Admin_module(self.driver)
        self.login.login_with_username_pswd(Inputs.username, Inputs.password)
        self.login.click_Admin()
        wait = WebDriverWait(setup, 10)
        Menu_options_elements = wait.until(EC.visibility_of_element_located((By.XPATH, Selectors.Menu_options)))
        Menu = Menu_options_elements.text
        exp_list_in_Menu = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory", "Maintenance", "Claim", "Buzz"]
        list_in_Menu = []

        for elements in exp_list_in_Menu:
            if elements in Menu:
                list_in_Menu.append(elements)
        assert exp_list_in_Menu == list_in_Menu







