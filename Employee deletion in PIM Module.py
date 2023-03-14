Employee deletion in PIM Module

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
    password_locator = 'password'
    submitbox_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    
    def Browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
    
    def login(self):
        sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.submitbox_locator).click()

    def new_employee_button(self):
        new_employee_button = self.driver.find_element_xpath('//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a')
        new_employee_button.click()

#locate the employee to delete and click on their name
    def employee_name_link(self):
        employee_name_link = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[7]/div/div[3]/div')
        employee_name_link.click()

#locate the Delete button and click on it
    def delete_button(self):
        delete_button = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[7]/div/div[9]/div/button[1]/i')
        delete_button.click()

# wait for the confirmation dialog to appear and confirm deletion
    sleep(1)
    confirm_button = driver.switch_to.alert.accept()

# wait for success message to appear
    sleep(3)

# check if success message is displayed
    success_message = driver.find_element_by_xpath('[//*[@id="app"]/div[3]/div/div/div/div[3]/button[2],"Employee deleted successfully")]')
    assert success_message.is_displayed()

Komal().Browsing()

Komal().login()
