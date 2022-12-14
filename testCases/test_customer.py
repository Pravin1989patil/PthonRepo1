import time

from pageObjects.CustomerPage import CustomerPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class Test_002_Customer:
    baseURL = ReadConfig.getApplicationURl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getUserPassword()

    def test_CustomerPageTitle(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()
        self.cp = CustomerPage(self.driver)
        self.cp.clickOnCustomerTab()
        self.cp.clickOnCustomerLink()
        self.cp.clickOnAddCustomerButton()
        customer_page_title = self.driver.title
        if customer_page_title == "Add a new customer / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_CustomerPageTitle.png")
            self.driver.close()
            assert False

    def test_AddCustomer(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()
        self.cp = CustomerPage(self.driver)
        self.cp.clickOnCustomerTab()
        self.cp.clickOnCustomerLink()
        self.cp.clickOnAddCustomerButton()
        time.sleep(2)
        self.cp.setUserEmail("pravin179patil@y.com")
        time.sleep(2)
        self.cp.setUserPassword("test123")
        time.sleep(2)
        self.cp.setUserGender()
        time.sleep(2)
        self.cp.setUserDOB("12/12/2012")
        time.sleep(2)
        self.cp.setCompanyName("tekizma")
        time.sleep(2)
        self.cp.setTaxExemptCheckbox()
        time.sleep(2)
        # self.cp.setUserRoles()
        time.sleep(2)
        self.cp.setVendorManager()
        time.sleep(2)
        self.cp.setAdminComments("test comments")
        time.sleep(2)
        self.cp.clickOnSaveButton()
        if self.cp.getSuccessMessage():
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_AddCustomer.png")
            self.driver.close()
            assert False
