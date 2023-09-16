from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

class OrangeHrm_Adminpage_validate:
    def __init__(self):
        self.url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        self.driver = webdriver.Chrome(options=options)
        self.username = "Admin"
        self.password = "admin123"
        self.username_loc_name_tag = "username"
        self.password_loc_name_tag = "password"
        self.logging_out_menu = '//i[@class="oxd-icon bi-caret-down-fill oxd-userdropdown-icon"]'
        self.logging_out = "//a[text()='Logout']"
        self.adminpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span'
        self.driver.implicitly_wait(10)

    def browse(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        actions = ActionChains(self.driver)


    def input_credentials(self):
        #username find with name

        username_webelement = self.driver.find_element(By.NAME, self.username_loc_name_tag)
        username_webelement.send_keys(self.username)

        #password find with name

        password_webelement = self.driver.find_element(By.NAME, self.password_loc_name_tag)
        password_webelement.send_keys(self.password)

        # login  find with web xpath
        login_path_xpath = '//button[@type="submit"]'
        login_button_webelement = self.driver.find_element(By.XPATH, login_path_xpath)
        login_button_webelement.click()
        title_1 = self.driver.title
        print(title_1)


    def admin_page(self):
        #admin page evaluvate with xpath

        adminpage =self.driver.find_element(By.XPATH,self.adminpath)
        adminpage.click()

obj = OrangeHrm_Adminpage_validate()
obj.browse()
obj.input_credentials()
obj.admin_page()