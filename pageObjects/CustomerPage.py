from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CustomerPage:
    link_customer_tab_xpath = "//i[@class='nav-icon far fa-user']"
    link_customer_list_xpath = "//a[@href='/Admin/Customer/List']"
    link_add_customer_xpath = "//a[@href='/Admin/Customer/Create']"
    textbox_email_name = "Email"
    textbox_password_name = "Password"
    textbox_firstname_name = "FirstName"
    checkbox_gender_xpath = "//input[@type='radio' and @value='M']"
    calendar_dateofbirth_name = "DateOfBirth"
    button_save_name = "save"
    textbox_company_name = "Company"
    checkbox_taxexempt_name = "IsTaxExempt"
    dropdown_roles_list = "// ul[ @ id = 'SelectedCustomerRoleIds_listbox'] // li"
    dropdown_vendor_id = "VendorId"
    textarea_admincomment_id = "AdminComment"
    message_success_xpath="//button[@type='button' and @class='close' and text()='×']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerTab(self):
        self.driver.find_element(By.XPATH, self.link_customer_tab_xpath).click()

    def clickOnCustomerLink(self):
        self.driver.find_element(By.XPATH, self.link_customer_list_xpath).click()

    def clickOnAddCustomerButton(self):
        self.driver.find_element(By.XPATH, self.link_add_customer_xpath).click()

    def setUserEmail(self, email):
        self.driver.find_element(By.NAME, self.textbox_email_name).send_keys(email)

    def setUserPassword(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    def setUserGender(self):
        self.driver.find_element(By.XPATH, self.checkbox_gender_xpath).click()

    def setUserDOB(self, dob):
        self.driver.find_element(By.NAME, self.calendar_dateofbirth_name).send_keys(dob)

    def setCompanyName(self, companyname):
        self.driver.find_element(By.NAME, self.textbox_company_name).send_keys(companyname)

    def setTaxExemptCheckbox(self):
        self.driver.find_element(By.NAME, self.checkbox_taxexempt_name).click()

    def setUserRoles(self):
        drpdwnList = self.driver.find_elements(By.XPATH, self.dropdown_roles_list)
        print(len(drpdwnList))
        for role in drpdwnList:
            if role.text() == "Guests":
                role.click()
                break

    def setVendorManager(self):
        drpdwn1 = Select(self.driver.find_element(By.ID, self.dropdown_vendor_id))
        drpdwn1.select_by_visible_text("Vendor 1")

    def setAdminComments(self, comments):
        self.driver.find_element(By.ID, self.textarea_admincomment_id).send_keys(comments)

    def clickOnSaveButton(self):
        self.driver.find_element(By.NAME, self.button_save_name).click()

    def getSuccessMessage(self):
        return self.driver.find_element(By.XPATH, self.message_success_xpath).is_displayed()
