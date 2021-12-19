import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    enter_email_text_box_id = (By.ID, 'com.code2lead.kwad:id/Et4')
    enter_password_text_box_id = (By.ID, 'com.code2lead.kwad:id/Et5')
    login_button_id = (By.ID, 'com.code2lead.kwad:id/Btn3')
    enter_admin_text_box_id = (By.ID, 'com.code2lead.kwad:id/Edt_admin')

    def get_email_text_box(self):
        return self.driver.find_element(*LoginPage.enter_email_text_box_id)

    def get_password_text_box(self):
        return self.driver.find_element(*LoginPage.enter_password_text_box_id)

    def get_login_button(self):
        return self.driver.find_element(*LoginPage.login_button_id)

    def get_admin_text_box(self):
        return self.driver.find_element(*LoginPage.enter_admin_text_box_id)

    def verify_admin_page(self):
        element = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((LoginPage.enter_admin_text_box_id)))
        assert 'Enter Admin' in element.text
