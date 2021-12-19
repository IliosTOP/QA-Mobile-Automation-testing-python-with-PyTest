from selenium.webdriver.common.by import By

from pageObjects.contactUsForm import ContactUsForm
from pageObjects.loginPage import LoginPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # here I use id primarily because of convenience
    enter_some_value_button_id = (By.ID, 'com.code2lead.kwad:id/EnterValue')
    contact_us_form_button_id = (By.ID, 'com.code2lead.kwad:id/ContactUs')
    scrollView_button_id = (By.ID, 'com.code2lead.kwad:id/ScrollView')
    tab_activity_button_id = (By.ID, 'com.code2lead.kwad:id/TabView')
    zoom_button_id = (By.ID, 'com.code2lead.kwad:id/Zoom')
    login_button_id = (By.ID, 'com.code2lead.kwad:id/Login')
    long_click_button_id = (By.ID, 'com.code2lead.kwad:id/LongClick')
    time_button_id = (By.ID, 'com.code2lead.kwad:id/Time')

    def get_enter_value(self):
        return self.driver.find_element(*HomePage.enter_some_value_button_id)

    def click_on_contact_us_form(self):
        self.driver.find_element(*HomePage.contact_us_form_button_id).click()
        on_contact_us_form = ContactUsForm(self.driver)
        return on_contact_us_form


    def get_scrollView(self):
        return self.driver.find_element(*HomePage.scrollView_button_id)

    def get_tab_activity(self):
        return self.driver.find_element(*HomePage.tab_activity_button_id)

    def get_zoom(self):
        return self.driver.find_element(*HomePage.zoom_button_id)

    def click_on_login(self):
        self.driver.find_element(*HomePage.login_button_id).click()
        on_login_page = LoginPage(self.driver)
        return on_login_page

    def get_long_click(self):
        return self.driver.find_element(*HomePage.long_click_button_id)

    def get_time(self):
        return self.driver.find_element(*HomePage.time_button_id)
