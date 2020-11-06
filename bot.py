from selenium import webdriver
import os
from time import sleep


class InstagramBot:
    def __init__(self, username, password):
        """
        Initializes an instance of the InstagramBot class.
        Calls the login method to authenticate a user

        Args:
            username:str: The instagram username
            password:str: The instagram password

        Attributes:
                driver:Selenium.webdriver.Chrome: The chromedriver used to automate browser actions
        """

        self.username = username
        self.password = password

        # boot up an instance of chrome
        self.driver = webdriver.Chrome()
        self.login()
        self.base_url = "https://instagram.com"

    def login(self):
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()

    def nav_user(self, user):
        self.driver.get('{}/'

if __name__ == '__main__':
    ig_bot = InstagramBot('temp_username', 'temp_password')

