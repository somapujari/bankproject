from selenium.webdriver.common.by import By


class Login:
    username__inp_xpath = (By.XPATH, "//input[@name='username']")
    password_inp_xpath = (By.XPATH, "//input[@name='password']")
    login_btn_xpath = (By.XPATH, "//input[@value='Log In']")

    def __init__(self, driver):
        self.driver = driver

    def username_enter(self, username):
        self.driver.find_element(*Login.username__inp_xpath).clear()
        self.driver.find_element(*Login.username__inp_xpath).send_keys(username)

    def password_enter(self, password):
        self.driver.find_element(*Login.password_inp_xpath).clear()
        self.driver.find_element(*Login.password_inp_xpath).send_keys(password)

    def click_on_login(self):
        self.driver.find_element(*Login.login_btn_xpath).click()
