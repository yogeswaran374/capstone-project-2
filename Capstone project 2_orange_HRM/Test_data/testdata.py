

class Inputs:
    username = "Admin"
    password = "admin123"
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

class Selectors:

    #selectors for forgot password
    forget_password_element_xpath = '//p[text()="Forgot your password? "]'
    text_box_username_xpath = '//input[@name="username"]'
    Reset_button_xpath = '//button[@type="submit"]'
    Reset_pswd_link_sent_element = '//h6[@class="oxd-text oxd-text--h6 orangehrm-forgot-password-title"]'

    # selectors for login with username and password
    text_box_username_xpath = '//input[@name="username"]'
    text_box_pswd_xpath = '//input[@name="password"]'
    login_button_xpath = '//button[@type="submit"]'

    # selectors for Admin element
    Admin_element = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span'

    Admin_page_Headers_elements = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul'

    #selectors of Menu options element
    Menu_options = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul'

