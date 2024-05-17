import os
from time import sleep
from selenium.webdriver.common.by import By

ACCOUNT_EMAIL = os.environ.get("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.environ.get("ACCOUNT_PASSWORD")


class LoginManager:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.get("https://dou.ua")

        sleep(3)

        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-link"]')
        login_button.click()

        sleep(3)

        login_with_email_btn = self.driver.find_element(
            By.XPATH, '//*[@id="_loginByMail"]'
        )
        login_with_email_btn.click()

        sleep(3)

        email_input = self.driver.find_element(
            By.XPATH,
            '//*[@id="_loginDialog"]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/input',
        )
        email_input.send_keys(ACCOUNT_EMAIL)

        sleep(2)

        password_input = self.driver.find_element(
            By.XPATH,
            '//*[@id="_loginDialog"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/div[2]/div[1]/input',
        )

        password_input.send_keys(ACCOUNT_PASSWORD)

        sleep(2)

        submit_button = self.driver.find_element(
            By.XPATH,
            '//*[@id="_loginDialog"]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/button',
        )
        submit_button.click()

        sleep(5)
