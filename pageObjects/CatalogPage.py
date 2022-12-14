from selenium.webdriver.common.by import By


class CatalogPage:
    link_catalog_xpath = "//i[@class='nav-icon fas fa-book']"
    link_product_list_xpath = "//a[@href='/Admin/Product/List']"
    link_add_product_xpath = "//a[@href='/Admin/Product/Create']"
    textbox_product_name_id = "Name"
    textbox_product_description_id = "ShortDescription"
    frame_fulldesc_id = "FullDescription_ifr"
    frame_body_id = "tinymce"
    textbox_sku_name = "Sku"
    dropdown_category_id = "SelectedCategoryIds_taglist"
    button_save_name = "save"
    message_success_xpath = "//button[@type='button' and @data-dismiss='alert']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCatalogTab(self):
        self.driver.find_element(By.XPATH, self.link_catalog_xpath).click()

    def clickOnProductsLink(self):
        self.driver.find_element(By.XPATH, self.link_product_list_xpath).click()

    def clickOnAddProductButton(self):
        self.driver.find_element(By.XPATH, self.link_add_product_xpath).click()

    def setProductName(self, productname):
        self.driver.find_element(By.ID, self.textbox_product_name_id).send_keys(productname)

    def setProductDescription(self, description):
        self.driver.find_element(By.ID, self.textbox_product_description_id).send_keys(description)

    def setFullDescription(self, fulldescription):
        self.driver.switch_to.frame(self.driver.find_element(By.ID, self.frame_fulldesc_id))
        self.driver.find_element(By.ID, self.frame_body_id).send_keys(fulldescription)
        self.driver.switch_to.default_content()

    def setSKU(self, sku):
        self.driver.find_element(By.NAME, self.textbox_sku_name).send_keys(sku)

    def clickOnSaveButton(self):
        self.driver.find_element(By.NAME, self.button_save_name).click()

    def getSuccessMessage(self):
        result = self.driver.find_elements(By.XPATH, self.message_success_xpath)
        if len(result) == 0:
            return False
        else:
            return True
