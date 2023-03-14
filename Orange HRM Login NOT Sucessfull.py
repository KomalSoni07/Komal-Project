# Orange HRM Login not Sucessfully:

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Komal:
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    username = 'Admin'
    password = 'admin123'
    username_locator = 'username'
    username_input = 'username'
    password_locator = 'password'
    password_input = 'password'
    submitbox_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    
    def Browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
    
    def login(self):
        sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        username_input.send_keys("incorrect_username")
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        password_input.send_keys("incorrect_password")
        self.driver.find_element(by=By.XPATH, value=self.submitbox_locator).click()
        password_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        error_message = driver.find_element_by_class_Komal("Invalid details")
        assert error_message.is_displayed()
        
Komal().Browsing()

Komal().login()

