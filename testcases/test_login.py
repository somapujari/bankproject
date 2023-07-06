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


