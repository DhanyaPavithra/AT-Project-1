# Importing Data and Locator details from respective files:

from Data import data
from Locator import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# importing exceptions
from selenium.common.exceptions import NoSuchElementException

# importing explicit waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login02:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        """
        To boot the webpage with the url

        """
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def quit(self):
        """
        To quit the webpage
        """
        self.driver.quit()

    def LoginPage(self):
        """
        function to Login the webpage
        """
        try:

            self.boot()
            locator.WebLocators().enterText(self.driver,locator.WebLocators().usernameLocator,data.WebData().username_TCLogin02)
            locator.WebLocators().enterText(self.driver,locator.WebLocators().passwordLocator,data.WebData().password_TCLogin02)
            locator.WebLocators().clickBtn(self.driver,locator.WebLocators().loginBtnLocator)

            if self.driver.current_url == data.WebData().dashboardURL:
                print("The user is logged in successfully")
            else:
                error_message = WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.XPATH, locator.WebLocators().errorMsgLocator))).text
                print(error_message)

        except NoSuchElementException as e:
            print(e)

        finally:
            self.quit()

obj = Login02()
obj.LoginPage()




