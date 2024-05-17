import datetime
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


NOT_RELEVANT_VACANCY_TEXT = "⚠️ The vacancy has significantly higher requirements for work experience than indicated in your profile."

COVER_LETTER = "Hi,\n\npls check my attached CV and Portfolio portfolio-page-alpha-black.vercel.app\n\nthank you and have a great day\n\nwith bstgds\n\nY. Kolbaiev"


class VacancyManager:
    def __init__(self, driver, category):
        self.category = category
        self.driver = driver
        self.yesterday_vacancies = self.get_vacancies()

    def get_vacancies(self):
        print(f"Getting vacancies for {self.category}")

        self.driver.get(f"https://jobs.dou.ua/vacancies/?category={self.category}")

        sleep(3)

        yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime(
            "%d %B"
        )
        vacancies = self.driver.find_elements(By.CSS_SELECTOR, ".l-vacancy .date")
        yesterday_vacancies = []

        for vacancy in vacancies:
            if not vacancy.text:
                continue

            if yesterday == vacancy.text:
                yesterday_vacancies.append(vacancy)

        return yesterday_vacancies

    def vacancy_manager(self):
        for vacancy in self.yesterday_vacancies:
            sibling = vacancy.find_element(By.XPATH, "./following-sibling::div")
            link = sibling.find_element(By.TAG_NAME, "a")
            link.send_keys(Keys.CONTROL + Keys.RETURN)

            sleep(5)

            self.driver.switch_to.window(self.driver.window_handles[1])

            sleep(3)

            try:
                skip_vacancy = self.vacancy_not_relevant()

                if skip_vacancy:
                    continue
            except Exception:
                print("Vacancy is relevant")

            try:
                self.apply_for_vacancy()
            except Exception:
                self.vacancy_with_external_link()

        sleep(3)

        print(f"All ${self.category} vacancies processed successfully")

    def vacancy_not_relevant(self):
        not_relevant_vacancy = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div[2]/div/div[2]/div[1]/div/div[4]/div[3]',
        )

        if not_relevant_vacancy.text == NOT_RELEVANT_VACANCY_TEXT:
            print("Vacancy is not relevant")

            self.driver.close()

            sleep(1)

            self.driver.switch_to.window(self.driver.window_handles[0])

            return True

    def apply_for_vacancy(self):
        apply_button = self.driver.find_element(By.XPATH, '//*[@id="reply-btn-id"]')
        apply_button.click()

        sleep(3)

        cover_letter = self.driver.find_element(By.XPATH, '//*[@id="reply_descr"]')
        cover_letter.send_keys(COVER_LETTER)

        sleep(2)

        file_input = self.driver.find_element(By.XPATH, '//*[@id="reply_file"]')
        file_input.send_keys("D:/PYTHON/CODE/DAY102DOU_APPLICATION_BOT/data/C_V.pdf")

        sleep(2)

        submit_button = self.driver.find_element(
            By.XPATH, '//*[@id="replied-id"]/button'
        )
        submit_button.click()

        sleep(5)

        print("Application sent")

        self.driver.close()

        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[0])

    def vacancy_with_external_link(self):
        external_link = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div[4]/div/div[2]/div[1]/div/div[4]/div[4]/a',
        )

        print(
            f"Apply button leeds to external website. Link: {external_link.get_attribute('href')}"
        )
        self.driver.close()

        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[0])
