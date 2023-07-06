import time

import pytest
from utility.customlogs import LogGen
from pageobjects.transfer_funds import TransferFunds
from utility.readproperty import ReadConfig
from pageobjects.login import Login


class Test_TrFund:
    url = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    assertion_errors = []
    logger = LogGen.loggen()

    def soft_assert(self, condition, message):
        if not condition:
            self.assertion_errors.append(message)

    def test_transfer_fund_001(self, setup):
        self.logger.info('test_transfer_fund_001 started ')
        self.driver = setup
        self.logger.info(f'opening url = {self.url}')
        self.driver.get(self.url)

        self.driver.maximize_window()
        self.lg = Login(self.driver)
        self.logger.info('enter username')
        self.lg.username_enter('soma')
        self.logger.info('verifying login page title ')
        self.soft_assert(self.driver.title.__eq__('ParaBank | Welcome | Online Banking'), 'login title not matching')
        self.logger.info('entering password ')
        self.lg.password_enter('soma@123')
        self.logger.info('click login ')
        self.lg.click_on_login()
        act_title = self.driver.title
        self.logger.info('verifying login title ')
        self.soft_assert(act_title.__eq__('ParaBank | Accounts Overview'), 'title of account overview not matching')
        self.tr = TransferFunds(self.driver)
        self.logger.info('click on transfer link ')
        self.tr.transfer_link_click()
        time.sleep(1)
        self.logger.info('enter amount')
        self.tr.amount_enter(10)
        self.logger.info('from account selecting ')
        self.tr.from_account_enter()
        self.logger.info('to account selecting ')
        self.tr.to_account_enter()
        self.logger.info('click transfer ')
        self.tr.transfer_click()
        time.sleep(2)
        cont = self.driver.find_element(*TransferFunds.body_contains_xpath).text
        # print(cont)
        self.logger.info('verifying transfer')
        if cont.__contains__('has been transferred from account #'):
            self.soft_assert(True, 'Transfer  of amount successfully ')
            self.logger.info('test is passed ')
            self.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\bankproject\screenshots\trfunds_pass.png')
        else:
            self.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\bankproject\screenshots\trfunds_fail.png')
            self.soft_assert(False, ' Transfer amount  not successfully ')
            self.logger.info('test failed')
        if self.assertion_errors:
            print('soft assert failure')
            for error in self.assertion_errors:
                print(error)
            pytest.fail('soft assert fail')

        self.logger.info('test register completed')
