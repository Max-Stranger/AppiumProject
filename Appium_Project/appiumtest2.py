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
    appPackage= 'com.google.android.apps.nexuslauncher',
    appActivity='com.google.android.apps.nexuslauncher.NexusLauncherActivity',
    platformVersion="35"
)


class textNespresso(unittest.TestCase):

    def setUp(self) -> None:
        ##########Appium Setup##########
        self.driver_appium = AppiumWebdriver.Remote(appium_server_url_local, capabilities)
        self.driver_appium.implicitly_wait(10)
        self.AppiumFunctions=AppiumFunctions(self.driver_appium)
        service_chrome = Service(r"C:\Users\97253\Desktop\chromedriver-win64\chromedriver.exe")
        driver_selenium = SeleniumWebdriver.Chrome(service=service_chrome)
        driver_selenium.implicitly_wait(10)
        driver_selenium.get("https://www.nespresso.com/il/he/")
        driver_selenium.maximize_window()
        self.SeleniumFunctions=SeleniumFunctions(driver_selenium)
        self.phoneNumber=self.SeleniumFunctions.PhoneNumber()

    def tearDown(self, driver_selenium=None) -> None:
        if self.driver_appium:
            self.driver_appium.quit()

        # Teardown for Selenium
        if driver_selenium:
            driver_selenium.quit()

    def test_TextNespresso(self):
        self.AppiumFunctions.EnterMessagesApp().click()
        self.AppiumFunctions.EnterMessages().click()
        sleep(3)
        self.AppiumFunctions.EnterPhoneNumber(self.phoneNumber)
        self.AppiumFunctions.textTab().send_keys("I like your coffee, i would like to order more.")
        self.AppiumFunctions.sendMSG().click()
        self.assertEqual(type(self.AppiumFunctions.textBubble()),AppiumWebdriver.WebElement)


