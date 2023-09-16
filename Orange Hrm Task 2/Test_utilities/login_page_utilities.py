from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


from Test_data import credentials
from Test_Locaters.login_page import LoginPageLocators


class LoginPageActions:

    def __init__(self):
        self.loginlocators = LoginPageLocators()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(credentials.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def username_credential(self):

       #user name given via find element by name

        username_webelement = self.driver.find_element(By.NAME, self.loginlocators.username_locator_name_tag)
        username_webelement.clear()
        username_webelement.send_keys(credentials.username)

    def password_credential(self):
        # Password given via find element by name
        password_webelement = self.driver.find_element(By.NAME, self.loginlocators.password_locator_name_tag)
        password_webelement.clear()
        password_webelement.send_keys(credentials.password)

    def click_login(self):
        login_button_webelement = self.driver.find_element(By.XPATH, self.loginlocators.login_button)
        login_button_webelement.click()

    def login_to_orangehrm(self):
        self.username_credential()
        self.password_credential()
        self.click_login()
        print(self.driver.title)

    def title_of_page(self):
        return self.driver.title

    def admin_page(self):
        adminpage =self.driver.find_element(By.XPATH,self.adminpath)
        adminpage.click()

