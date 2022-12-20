import time

import pytest
from allure_commons.model2 import Attachment

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig

# from utilities.customLogger import LogGen
import allure


@allure.severity(allure.severity_level.MINOR)
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getUserPassword()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(3)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="HomePageTitle", attachment_type=Attachment.PNG)
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_login_test(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()
        page_title = self.driver.title
        if page_title == "Dashboard / nopCommerce administration":
            self.lp.clickLogoutLink()
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_login_test_failed.png")
            self.driver.close()
            assert False
