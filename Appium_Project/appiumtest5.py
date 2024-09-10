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
    appPackage= 'com.google.android.apps.maps',
    appActivity='com.google.android.maps.MapsActivity',
    platformVersion="35"
)


class getDirections(unittest.TestCase):

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

    def testDirections(self):
        self.AppiumFunctions.SkipBtn().click()
        self.AppiumFunctions.googleMapsSearchBar().click()
        self.AppiumFunctions.googleMapsTextBox().send_keys("Nespresso, Petah Tikva")
        self.AppiumFunctions.googleMapsSelectLocation().click()
        self.AppiumFunctions.googleMapsDirectionsBtn().click()
        self.AppiumFunctions.googleMapsSearchBar2().click()
        self.AppiumFunctions.googleMapsTextBox().send_keys("Shalom Tsalah 2, Petah Tikva")
        self.AppiumFunctions.googleMapsSelectLocation().click()
        self.AppiumFunctions.googleMapsPreviewRoute().click()
        self.assertIsInstance(self.AppiumFunctions.googleMapsDirectionsArrow(),AppiumWebdriver.WebElement)
