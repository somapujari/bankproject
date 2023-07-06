
from selenium.webdriver.common.by import By


class Register:
    register_lnk_xpath = (By.XPATH, "//a[normalize-space()='Register']")
    first_name_inp_id = (By.ID, 'customer.firstName')
    last_name_inp_id = (By.ID, 'customer.lastName')
    address_inp_id = (By.ID, 'customer.address.street')
    city_inp_id = (By.ID,'customer.address.city')
    state_inp_id = (By.ID,'customer.address.state')
    zip_inp_id = (By.ID, 'customer.address.zipCode')
    phone_inp_id = (By.ID, 'customer.phoneNumber')
    ssn_inp_id = (By.ID, "customer.ssn")
    username_inp_id = (By.ID, 'customer.username')
    password_inp_id = (By.ID, 'customer.password')
    conform_pass_inp_id = (By.ID, 'repeatedPassword')
    register_btn_xpath = (By.XPATH, "//input[@value='Register']")

    def __init__(self, driver):
        self.driver = driver

    def register_click(self):
        self.driver.find_element(*Register.register_lnk_xpath).click()

    def first_name_enter(self, first_name):
        self.driver.find_element(*Register.first_name_inp_id).send_keys(first_name)

    def last_name_enter(self, last_name):
        self.driver.find_element(*Register.last_name_inp_id).send_keys(last_name)

    def address_enter(self, address):
        self.driver.find_element(*Register.address_inp_id).send_keys(address)

    def city_enter(self, city):
        self.driver.find_element(*Register.city_inp_id).send_keys(city)

    def state_enter(self, state):
        self.driver.find_element(*Register.state_inp_id).send_keys(state)

    def zip_enter(self, zipcode):
        self.driver.find_element(*Register.zip_inp_id).send_keys(zipcode)

    def phone_number_enter(self, phone):
        self.driver.find_element(*Register.phone_inp_id).send_keys(phone)

    def ssn_enter(self, ssn):
        self.driver.find_element(*Register.ssn_inp_id).send_keys(ssn)

    def username_enter(self,username):
        self.driver.find_element(*Register.username_inp_id).send_keys(username)

    def password_enter(self, password):
        self.driver.find_element(*Register.password_inp_id).send_keys(password)

    def conform_pass_enter(self, password):
        self.driver.find_element(*Register.conform_pass_inp_id).send_keys(password)

    def register_submit(self):
        self.driver.find_element(*Register.register_btn_xpath).click()






