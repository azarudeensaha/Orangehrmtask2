from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)


class OrangeHrm:

    def __init__(self):
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.driver = webdriver.Chrome(options=options)
        self.username = "Admin"
        self.invalid_password = "invalidpassword"
        self.username_loc_name_tag = "username"
        self.password_loc_name_tag = "password"
        self.forgot_pass="//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"
        self.forgot_username_loc = '//input[@name="username"]'
        self.reset_button='//button[@type="submit"]'

        #browse page function
    def browse(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        actions = ActionChains(self.driver)
        sleep(5)

        #forget password verfication
    def forget_pass_link(self):
        password_forget_link = self.driver.find_element(By.XPATH , self.forgot_pass)
        password_forget_link.click()
        sleep(5)
        forget_link_username= self.driver.find_element(By.XPATH , self.forgot_username_loc)
        forget_link_username.send_keys(self.username)
        sleep(3)
        reset_password=self.driver.find_element(By.XPATH ,self.reset_button)
        reset_password.click()
        sleep(3)

obj = OrangeHrm()
obj.browse()
obj.forget_pass_link()