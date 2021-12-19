import time

import pytest

from pageObjects.homePage import HomePage
from testData import loginTestData
from testData.loginTestData import LoginData
from utilities.baseClass import BaseClass


class TestDemo1(BaseClass):
    def test_open_contact_form(self):
        on_home_page = HomePage(self.driver)
        on_contact_us_form = on_home_page.click_on_contact_us_form()
        time.sleep(2)
        on_contact_us_form.verify_contact_page()

    def test_login_fail_method(self, get_data):
        on_home_page = HomePage(self.driver)
        on_login_page = on_home_page.click_on_login()
        time.sleep(2)
        on_login_page.get_password_text_box().send_keys(get_data["password"])
        on_login_page.get_email_text_box().send_keys(get_data["email"])
        on_login_page.get_login_button().click()
        on_login_page.verify_admin_page()

    @pytest.fixture(params=LoginData.data())
    def get_data(self, request):
        return request.param
