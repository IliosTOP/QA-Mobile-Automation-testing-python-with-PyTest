from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactUsForm:
    def __init__(self, driver):
        self.driver = driver

    enter_email_id = (By.ID, 'com.code2lead.kwad:id/Et2')
    contact_us_form_text = 'Contact Us form'

    def verify_contact_page(self):
        element = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((ContactUsForm.enter_email_id)))
        assert element.text == 'Enter Name'
