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
    appPackage= 'com.google.android.dialer',
    appActivity='com.google.android.dialer.extensions.GoogleDialtactsActivity',
    platformVersion="35"
)


class callNespresso(unittest.TestCase):

    def setUp(self) -> None:
        ##########Appium Setup##########
        self.driver_appium = AppiumWebdriver.Remote(appium_server_url_local, capabilities)
        self.driver_appium.implicitly_wait(10)
        self.AppiumFunctions=AppiumFunctions(self.driver_appium)

    def tearDown(self, driver_selenium=None) -> None:
        if self.driver_appium:
            self.driver_appium.quit()

        # Teardown for Selenium
        if driver_selenium:
            driver_selenium.quit()


    def test_callNespresso(self):
        #########Dialing in the improved phone number & calling#########
        service_chrome = Service(r"C:\Users\97253\Desktop\chromedriver-win64\chromedriver.exe")
        driver_selenium = SeleniumWebdriver.Chrome(service=service_chrome)
        driver_selenium.get("https://www.nespresso.com/il/he/")
        driver_selenium.maximize_window()
        self.SeleniumFunctions=SeleniumFunctions(driver_selenium)
        driver_selenium.implicitly_wait(10)
        self.PhoneNumber=self.SeleniumFunctions.PhoneNumber()
        self.AppiumFunctions.PhoneDialBtn().click()
        self.AppiumFunctions.NumbersTypeIn().send_keys(self.PhoneNumber)
        self.AppiumFunctions.CallBtn().click()
        self.assertEqual(type(self.AppiumFunctions.EndCallBtn()),AppiumWebdriver.WebElement)
        sleep(5)
        self.AppiumFunctions.EndCallBtn().click()









