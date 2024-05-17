from login_manager import LoginManager
from driver_manager import DriverManager
from reply_vacancy_manager import VacancyManager

driver = DriverManager().driver

login_manager = LoginManager(driver=driver)

login_manager.login()

front_end = VacancyManager(driver=driver, category="Front End")

front_end.vacancy_manager()

back_end = VacancyManager(driver=driver, category="Node.js")

back_end.vacancy_manager()

python = VacancyManager(driver=driver, category="Python")

python.vacancy_manager()
