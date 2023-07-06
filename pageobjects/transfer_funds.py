from selenium.webdriver.common.by import By

from utility.readproperty import ReadConfig


class TransferFunds:
    transfer_lnk_xpath = (By.XPATH, "//a[contains(text(),'Transfer Funds')]")
    amount_inp_xpath = (By.ID, "amount")
    from_acc_sel_xpath = (By.XPATH, "//select[@id='fromAccountId']")
    from_acc_num_xpath = (By.XPATH, "//select[@id='fromAccountId']/option[1]")
    to_account_sel_xpath = (By.XPATH, "//select[@id='toAccountId']")
    to_acc_num_xpath = (By.XPATH, "//select[@id='toAccountId']/option[1]")
    transfer_btn_xpath = (By.XPATH, "//input[@value='Transfer']")
    body_contains_xpath = (By.XPATH, '//body')
    def __init__(self, driver):
        self.driver = driver

    def transfer_link_click(self):
        self.driver.find_element(*TransferFunds.transfer_lnk_xpath).click()

    def amount_enter(self, amount):
        self.driver.find_element(*TransferFunds.amount_inp_xpath).clear()
        self.driver.find_element(*TransferFunds.amount_inp_xpath).send_keys(amount)

    def from_account_enter(self):
        self.driver.find_element(*TransferFunds.from_acc_sel_xpath).click()
        # self.driver.find_element(*TransferFunds.from_acc_num_xpath).click()

    def to_account_enter(self):
        self.driver.find_element(*TransferFunds.to_account_sel_xpath).click()
        # self.driver.find_element(*TransferFunds.to_acc_num_xpath).click()

    def transfer_click(self):
        self.driver.find_element(*TransferFunds.transfer_btn_xpath).click()

    #  has been transferred from account #
