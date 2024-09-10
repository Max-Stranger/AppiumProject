from appium import webdriver as AppiumWebdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver as SeleniumWebdriver
from selenium.webdriver.chrome.service import Service


class SeleniumFunctions:
    def __init__(self, driver: SeleniumWebdriver.Chrome):
        self.driver_selenium = driver

    def PhoneNumber(self):
        return self.driver_selenium.find_element(By.XPATH,"//*[@id='ul_ad-3']/li/span/table/tbody/tr[3]/td[3]/p/span[3]/span").text.replace("-","")
