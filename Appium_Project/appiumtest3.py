import unittest
from appium import webdriver as AppiumWebdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver as SeleniumWebdriver
from selenium.webdriver.chrome.service import Service
from Appium_Project.SeleniumFunctions import SeleniumFunctions
from Appium_Project.AppiumFunctions import AppiumFunctions
from time import sleep
from selenium.webdriver.common.keys import Keys



appium_server_url_local = 'http://localhost:4723/wd/hub'
capabilities = dict(
    platformName="Android",
    deviceName="Pixel7a",
    udid="emulator-5554",
    appPackage= 'com.google.android.contacts',
    appActivity='com.android.contacts.activities.PeopleActivity',
    platformVersion="35"
)


class addNespressoToContact(unittest.TestCase):

    def setUp(self) -> None:
        ##########Appium Setup##########
        self.driver_appium = AppiumWebdriver.Remote(appium_server_url_local, capabilities)
        self.driver_appium.implicitly_wait(10)
        self.AppiumFunctions=AppiumFunctions(self.driver_appium)
        # service_chrome = Service(r"C:\Users\97253\Desktop\chromedriver-win64\chromedriver.exe")
        # driver_selenium = SeleniumWebdriver.Chrome(service=service_chrome)
        # driver_selenium.implicitly_wait(10)
        # driver_selenium.get("https://www.nespresso.com/il/he/")
        # driver_selenium.maximize_window()
        # self.SeleniumFunctions=SeleniumFunctions(driver_selenium)
        # self.phoneNumber=self.SeleniumFunctions.PhoneNumber()

    def tearDown(self, driver_selenium=None) -> None:
        if self.driver_appium:
            self.driver_appium.quit()

        # Teardown for Selenium
        if driver_selenium:
            driver_selenium.quit()

    def testAddToContact(self):
        ContactNameGiven="Michal"
        self.AppiumFunctions.ContactsTab().click()
        self.AppiumFunctions.CreateContact().click()
        self.AppiumFunctions.EnterCompanyName().click()
        self.AppiumFunctions.EnterCompanyName().send_keys(ContactNameGiven)
        self.AppiumFunctions.EnterPhoneNumberToContact().click()
        self.AppiumFunctions.EnterPhoneNumberToContact().send_keys("0509089531")
        self.AppiumFunctions.SaveContact().click()
        sleep(2)
        self.driver_appium.back()
        ContactName=self.AppiumFunctions.ContactNameTitle()
        self.assertEqual(ContactNameGiven, ContactName)
        sleep(1)
        self.driver_appium.back()
        sleep(1)
        self.assertIsInstance(self.AppiumFunctions.ContactList(), AppiumWebdriver.WebElement)


