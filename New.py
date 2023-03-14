#Adding of the new employee in PIM Module:
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
    
    #navigate to new employee page
    new_employee_button = driver.find_element_xpath('//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a')
    new_employee_button.click()
    
    #enter new employee information
    first_name_input = driver.find_element_by_name("first_name")
    first_name_input.send_keys("John")
    last_name_input = driver.find_element_by_name("last_name")
    last_name_input.send_keys("Doe")
    employee_id_input = driver.find_element_by_name("employee_id")
    employee_id_input.send_keys("1234")
    save_button = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]/text()')
    save_button.click()
    
Komal().Browsing()

Komal().login()