import random
import string
import time

import allure

from pageobjects.regiseter import Register
from utility.customlogs import LogGen


class Test_Register:
    url = 'https://parabank.parasoft.com/parabank/index.htm'
    username = 'soma'
    password = 'soma@123'
    logger = LogGen.loggen()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_register(self, setup):
        self.logger.info('test reggister started ')
        self.driver = setup
        self.logger.info(f'opening url = {self.url}')
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.rg = Register(self.driver)
        self.rg.register_click()
        self.logger.info('entering name')
        self.rg.first_name_enter('soma')
        self.logger.info('enter lastname')
        self.rg.last_name_enter('pujari')
        self.logger.info('enter address')
        self.rg.address_enter('pune')
        self.logger.info('enter city ')
        self.rg.city_enter('pune')
        self.logger.info('enter state')
        self.rg.state_enter('maharashtra')
        self.logger.info('enter zipcode')
        self.rg.zip_enter('426455')
        self.logger.info('enter phone_number ')
        self.rg.phone_number_enter('8888888888')
        self.rg.ssn_enter('123456789')
        # self.username = self.random_username_generat()
        self.logger.info(f'enter username ={self.username}')
        self.rg.username_enter(self.username)
        self.logger.info('enter password')
        self.rg.password_enter('soma@123')
        self.rg.conform_pass_enter('soma@123')
        self.logger.info('click on register ')
        self.rg.register_submit()
        self.logger.info('verifying title')
        act_title = self.driver.title
        if act_title == 'ParaBank | Customer Created':
            assert True
            self.logger.info('test register passed')
            self.driver.save_screenshot(r'.\screenshots\registerpass.png')
        else:
            allure.attach(self.driver.get_screenshot_as_file('./screenshots/regeistterfail.png'))
            self.logger.info('test register failed ')
            self.driver.save_screenshot(r'.\screenshots\registerfail.png')
            assert False
        self.logger.info('test_register completed')

    def random_username_generat(self, size=6, char=string.ascii_lowercase+string.digits):
        username = ''.join(random.choice(char) for i in range(size))
        return username


from pageobjects.login import Login
from utility.customlogs import LogGen


class Test_Login:
    logger = LogGen.loggen()
    url = 'https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC'

    def test_login(self, setup):
        self.logger.info('test_login is started')
        self.driver = setup
        self.logger.info(f'url opening = {self.url} ')
        self.driver.get(self.url)
        self.logger.info('verifying title')
        assert self.driver.title == 'ParaBank | Welcome | Online Banking'
        self.driver.maximize_window()
        self.lg = Login(self.driver)
        self.logger.info('entering username')
        self.lg.username_enter('soma')
        self.logger.info('entering password')
        self.lg.password_enter('soma@123')
        self.logger.info('clicking log in button ')
        self.lg.click_on_login()
        self.logger.info('verifying title')
        act_title = self.driver.title
        if act_title == 'ParaBank | Accounts Overview':
            assert True
            self.logger.info('test login passed ')
            self.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\bankproject\screenshots\testloginppass.png')
        else:
            self.logger.info('test login failed')
            self.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\bankproject\screenshots\testloginpfail.png')
            assert False
        self.logger.info('test login completed')

    def test_03(self,):
        assert True

    def test_04(self):
        assert True
