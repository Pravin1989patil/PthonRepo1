import time

from pageObjects.LoginPage import LoginPage
from pageObjects.CatalogPage import CatalogPage
from utilities.readProperties import ReadConfig


class Test_003_Customer:
    baseURL = ReadConfig.getApplicationURl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getUserPassword()

    def test_AddProduct(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()

        self.pp=CatalogPage(self.driver)
        self.pp.clickOnCatalogTab()
        self.pp.clickOnProductsLink()
        self.pp.clickOnAddProductButton()
        self.pp.setProductName("Soap9")
        time.sleep(2)
        self.pp.setProductDescription("test")
        time.sleep(2)
        self.pp.setFullDescription("this is test description")
        time.sleep(2)
        self.pp.setSKU("123")
        time.sleep(5)
        self.pp.clickOnSaveButton()
        time.sleep(2)
        result = self.pp.getSuccessMessage()
        print(result)
        if result:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_AddProduct.png")
            self.driver.close()
            assert False


