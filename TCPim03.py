# Importing Data and Locator details from respective files:
from Data import data
from Locator import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# importing Exceptions
from selenium.common.exceptions import NoSuchElementException

# importing Actions Chains
from selenium.webdriver import ActionChains


class PIMmoduleThree:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #self.wait = WebDriverWait(self.driver, 15)
        self.action = ActionChains(self.driver)
    def boot(self):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        # Implicit waits
        self.driver.implicitly_wait(15)

    def quit(self):
        self.driver.quit()

    def deleteEmployee(self):

        try:
            self.boot()
            locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator,data.WebData().username_TCLogin01)
            locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator,data.WebData().password_TCLogin01)
            locator.WebLocators().clickBtn(self.driver, locator.WebLocators().loginBtnLocator)

            # PIM module:
            locator.WebLocators().clickBtn(self.driver,locator.WebLocators().pimLocator)
            locator.WebLocators().clickBtn(self.driver,locator.WebLocators().deleteEmployeeLocator)
            locator.WebLocators().clickBtn(self.driver,locator.WebLocators().deleteconfirmationLocator)

            print("Successfully deleted")

        except NoSuchElementException as e:
            print(e)

        finally:
            self.driver.quit()


obj = PIMmoduleThree()
obj.deleteEmployee()