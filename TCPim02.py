# Importing Data and Locator details from respective files:
from Data import data
from Locator import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# importing Exceptions
from selenium.common.exceptions import NoSuchElementException
# importing keys
from selenium.webdriver.common.keys import Keys
# importing Actions Chains
from selenium.webdriver import ActionChains


class PIMmoduleTwo:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #self.wait = WebDriverWait(self.driver, 15)
        self.action = ActionChains(self.driver)
    def boot(self):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        # Implicit wait
        self.driver.implicitly_wait(15)

    def quit(self):
        self.driver.quit()

    def editEmployee(self):

        try:
            self.boot()
            locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator,data.WebData().username_TCLogin01)
            locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator,data.WebData().password_TCLogin01)
            locator.WebLocators().clickBtn(self.driver, locator.WebLocators().loginBtnLocator)

            # PIM module:
            locator.WebLocators().clickBtn(self.driver,locator.WebLocators().pimLocator)
            locator.WebLocators().clickBtn(self.driver,locator.WebLocators().editOptionLocator)
            self.driver.find_element(by=By.XPATH, value=locator.WebLocators().middleNameLocator).click()

            self.action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
            self.action.send_keys(Keys.DELETE).perform()
            locator.WebLocators().enterText(self.driver, locator.WebLocators().middleNameLocator, data.WebData().editMiddleName)
            locator.WebLocators().clickBtn(self.driver,locator.WebLocators().savePersonalDetailsBtnLocator)

            print("Successful addition of employee details")

        except NoSuchElementException as e:
            print(e)

        finally:
            self.quit()

obj = PIMmoduleTwo()
obj.editEmployee()