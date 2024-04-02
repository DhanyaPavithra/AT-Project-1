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
# Explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIMmoduleOne:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #self.wait = WebDriverWait(self.driver, 15)
        self.action = ActionChains(self.driver)
    def boot(self):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def quit(self):
        self.driver.quit()

    def addEmployee(self):

        try:
            self.boot()
            # Login Credentials
            locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator,data.WebData().username_TCLogin01)
            locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator,data.WebData().password_TCLogin01)
            locator.WebLocators().clickBtn(self.driver, locator.WebLocators().loginBtnLocator)

            # PIM module:
            locator.WebLocators().clickBtn(self.driver,locator.WebLocators().pimLocator)
            locator.WebLocators().clickBtn(self.driver, locator.WebLocators().addEmployeeLocator)
            locator.WebLocators().enterText(self.driver,locator.WebLocators().firstNameLocator,data.WebData().firstName)
            locator.WebLocators().enterText(self.driver, locator.WebLocators().middleNameLocator,data.WebData().middleName)
            locator.WebLocators().enterText(self.driver, locator.WebLocators().lastNameLocator,data.WebData().lastName)

            self.driver.find_element(by=By.XPATH,value=locator.WebLocators().employeeIDLocator).click()

            self.action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
            self.action.send_keys(Keys.DELETE).perform()

            locator.WebLocators().enterText(self.driver,locator.WebLocators().employeeIDLocator,data.WebData().employeeID)

            locator.WebLocators().clickBtn(self.driver,locator.WebLocators().saveBtnLocator)

            # Personal details:

            locator.WebLocators().enterText(self.driver,locator.WebLocators().otherIDLocator, data.WebData().otherID)
            locator.WebLocators().enterText(self.driver,locator.WebLocators().driverLicenceNumLocator, data.WebData().driverLicenseNum)
            locator.WebLocators().enterText(self.driver,locator.WebLocators().licenseExpirydateLocator, data.WebData().licenseExpiryDate)
            WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[1]'))).click()
            WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[1]')))
            WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'))).click()
            locator.WebLocators().enterText(self.driver,locator.WebLocators().DOBLocator, data.WebData().DOB)
            locator.WebLocators().clickRadioBtn(self.driver,locator.WebLocators().femaleRadioBtnLocator)
            locator.WebLocators().clickBtn(self.driver,locator.WebLocators().savePersonalDetailsBtnLocator)

            print("Employee added successfully")

        except NoSuchElementException as e:
            print(e)

        finally:
            self.driver.quit()


obj = PIMmoduleOne()
obj.addEmployee()

