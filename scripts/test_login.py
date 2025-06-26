import unittest
from parameterized import parameterized

from page import page_login
from page.page_login import PageLogin
from base.get_driver import GetDriver
from tools.read_json import read_json
from time import sleep

global_error_info = 0


def get_data_login():
    datas = read_json("login.json")
    arrs = []
    for data in datas.values():
        arrs.append((data['username'], data['password'], data['success'], data['expect_result']))
    return arrs


# 测试登录
class Test_Login(unittest.TestCase):
    driver = None

    # 初始化方法
    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver()
        cls.login = PageLogin(cls.driver)

    # 结束方法
    @classmethod
    def tearDownClass(cls):
        page_login.global_variable_login = 0
        GetDriver.quit_driver()

    @parameterized.expand(get_data_login())
    def test_login(self, username, password, success=None, expect_result=None):
        '''
        测试登录功能，包括用户名、密码及协议的验证
        '''
        global global_error_info

        # 执行登录操作
        self.login.page_login(username, password, self.driver)

        if success:
            try:
                # 判断是否登录成功
                self.assertTrue(self.login.page_is_login_success())
                # 点击退出
                self.login.page_click_logout()

                # 判断是否退出成功
                self.assertTrue(self.login.page_is_logout_success())
                # 为下一次错误做准备
                global_error_info = 0
                self.login.page_click_login()
                self.login.page_click_pwd_login()
            except Exception:
                self.login.base_screenshot()  # 截图以记录错误
        else:
            #获取错误信息
            msg = self.login.page_get_error_info_before()
            try:
                # 进行断言，判断预期结果和真实结果是否相同
                self.assertEqual(msg, expect_result)
            except AssertionError:
                self.login.base_screenshot()  # 截图以记录错误
                raise

        # 刷新页面，主要就是为了刷新已经填写的协议
        self.driver.refresh()
        self.login.page_click_pwd_login()