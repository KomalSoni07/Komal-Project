#Edit Employee details in PIM

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

    new_employee_button = driver.find_element_xpath('//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a')
    new_employee_button.click()
    
# locate the employee to edit and click on their name
    employee_name_link = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input]')
    employee_name_link.click()

# locate the Edit button and click on it
    edit_button = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]/i')
    edit_button.click()

# update the employee information
    last_name_input = driver.find_element_by_name("last_name")
    last_name_input.clear()
    last_name_input.send_keys("Smith")
    save_button = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button')
    save_button.click()

# wait for success message to appear
    sleep(3)

# check if success message is displayed
    success_message = driver.find_element_by_xpath("//div[contains(text(), 'Employee details updated successfully')]")
    assert success_message.is_displayed()


# close the driver
Komal().Browsing()

Komal().login()