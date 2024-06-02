from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_data.testdata import Inputs,Selectors
from POM_pages.Login_page import Login


class Test_001_reset_link:

    def test_check_rst_success_or_not(self,setup):
        self.driver = setup
        self.driver.get(Inputs.base_url)
        self.loginpage = Login(self.driver)
        self.loginpage.click_forget_pswd()
        self.loginpage.enter_user_name(Inputs.username)
        self.loginpage.click_reset_button()
        wait = WebDriverWait(setup,10)
        reset_pswd_link_element = wait.until(EC.visibility_of_element_located((By.XPATH, Selectors.Reset_pswd_link_sent_element)))
        print(reset_pswd_link_element.text)
        exp_text = "Reset Password link sent successfully"
        assert exp_text == reset_pswd_link_element.text



