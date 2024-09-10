from appium import webdriver as appiumwebdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import random
from random import randint


class AppiumFunctions:
    def __init__(self, driver: appiumwebdriver.Remote):
        self.driver_appium = driver

    def PhoneDialBtn(self):
        """
        Locate the phone dial button element in the dialer app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/dialpad_fab')

    def NumbersTypeIn(self):
        """
        Locate the number input field in the dialer app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/digits')

    def CallBtn(self):
        """
        Locate the call button element in the dialer app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/dialpad_voice_call_button')

    def EndCallBtn(self):
        """
        Locate the end call button element in the dialer app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/incall_end_call')

    def CallGUI(self):
        """
        Locate the in-call user interface container in the dialer app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/incall_ui_container')

    def MuteText(self):
        """
        Locate the mute button element in the dialer app.
        """
        return self.driver_appium.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.google.android.dialer:id/entry_label" and @text="Mute"]')

    def EnterMessagesApp(self):
        """
        Locate the Messages app icon element.
        """
        return self.driver_appium.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Messages')

    def EnterMessages(self):
        """
        Locate the start chat button element in the Messages app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Start chat')

    def MessageHistory(self):
        """
        Locate the message history element in the Messages app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='message_list')

    def EnterPhoneNumber(self, number):
        """
        Enter a phone number into the appropriate input field in the dialer or contacts app.

        Args:
            number (str): The phone number to enter.
        """
        wait = WebDriverWait(self.driver_appium, 10)  # Wait for up to 10 seconds
        input_field = wait.until(
            EC.visibility_of_element_located((AppiumBy.CLASS_NAME, 'android.widget.EditText')))
        input_field.clear()  # Clear any pre-existing text
        input_field.send_keys(number)  # Input the phone number
        self.driver_appium.find_element(by=AppiumBy.XPATH, value='//android.view.View[@resource-id="ContactSuggestionList"]/android.view.View').click()

    def textTab(self):
        """
        Locate the text input field in the Messages app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ID, value='com.google.android.apps.messaging:id/compose_message_text')

    def sendMSG(self):
        """
        Locate the send SMS button element in the Messages app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Send SMS')

    def textBubble(self):
        """
        Locate the first text bubble element in the message list.
        """
        return self.driver_appium.find_element(by=AppiumBy.XPATH, value='//android.view.View[@resource-id="message_list"]/android.view.View[1]/android.view.View[2]')

    def ContactsTab(self):
        """
        Locate the Contacts tab element.
        """
        return self.driver_appium.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Contacts')

    def CreateContact(self):
        """
        Locate the Create Contact button element in the Contacts app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Create contact')

    def EnterCompanyName(self):
        """
        Locate the input field for entering a company name in the Contacts app.
        """
        return self.driver_appium.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Company"]')

    def EnterPhoneNumberToContact(self):
        """
        Locate the input field for entering a phone number in the Contacts app.
        """
        return self.driver_appium.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Phone"]')

    def SaveContact(self):
        """
        Locate the save contact button element in the Contacts app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ID, value='com.google.android.contacts:id/toolbar_button')

    def ContactList(self):
        """
        Locate the contact list element in the Contacts app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ID, value='android:id/list')

    def testFunction(self):
        """
        Locate all elements with a specific ID in the Contacts app.
        """
        return self.driver_appium.find_elements(by=AppiumBy.ID, value='android:id/list')

    def ContactNameTitle(self):
        """
        Locate the text of the contact name title element in the Contacts app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ID, value='com.google.android.contacts:id/large_title').text

    def threeDots(self):
        """
        Locate the 'More options' button element (three dots) in the Contacts app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='More options')

    def select(self):
        """
        Locate the 'Select' option in the Contacts app.
        """
        return self.driver_appium.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.google.android.contacts:id/title" and @text="Select"]')

    def ContactName(self, name):
        """
        Locate a contact name element by accessibility ID in the Contacts app.

        Args:
            name (str): The name of the contact to locate.
        """
        return self.driver_appium.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=name)

    def DeleteContactBtn(self):
        """
        Locate the Delete button element in the Contacts app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Delete')

    def ConfirmDeletion(self):
        """
        Locate the confirmation button element for deleting a contact in the Contacts app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ID, value='android:id/button1')

    def SearchBar(self):
        """
        Locate the search bar element in the Contacts app.
        """
        return self.driver_appium.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="com.google.android.contacts:id/open_search_bar"]')

    def SearchBar2(self):
        """
        Locate the secondary search bar element in the Contacts app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ID, value='com.google.android.contacts:id/open_search_view_edit_text')

    def NoResults(self):
        """
        Locate the 'No results' text element in the Contacts app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ID, value='android:id/text1').text

    def googleMapsSearchBar(self):
        """
        Locate the search bar element in the Google Maps app.
        """
        return self.driver_appium.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Search here"]')

    def SkipBtn(self):
        """
        Locate the 'Skip' button element in the Google Maps app.
        """
        return self.driver_appium.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="SKIP"]')

    def googleMapsSearchBar2(self):
        """
        Locate the search bar element for selecting a start location in the Google Maps app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Choose start location')

    def googleMapsTextBox(self):
        """
        Locate the text box element for inputting a location in the Google Maps app.
        """
        return self.driver_appium.find_element(by=AppiumBy.ID, value='com.google.android.apps.maps:id/search_omnibox_edit_text')

    def googleMapsSelectLocation(self):
        """
        Locate the element to select a location in the Google Maps app.
        """
        return self.driver_appium.find_element(by=AppiumBy.XPATH, value='//android.widget.LinearLayout[@resource-id="com.google.android.apps.maps:id/compass_container"]/android.widget.LinearLayout')

    def googleMapsDirectionsBtn(self):
        """
        Locate the directions button element in the Google Maps app.
        """
        return self.driver_appium.find_element(by=AppiumBy.XPATH, value='(//android.support.v7.widget.RecyclerView[@resource-id="com.google.android.apps.maps:id/recycler_view"])[1]/android.widget.LinearLayout[1]')

    def googleMapsPreviewRoute(self):
        """
        Locate the preview route element in the Google Maps app.
        """
        return self.driver_appium.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Preview driving navigation"]')

    def googleMapsDirectionsArrow(self):
        """
        Locate the directions arrow element in the Google Maps app.
        """
        return self.driver_appium.find_element(by=AppiumBy.XPATH, value='//android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ImageView')

    def googleSearchBarHomepage(self):
        return self.driver_appium.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='Google search')

    def googleSearchBarText(self):
        return self.driver_appium.find_element(by=AppiumBy.XPATH,value='com.google.android.apps.nexuslauncher:id/input')