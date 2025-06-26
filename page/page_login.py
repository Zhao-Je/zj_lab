from selenium.webdriver.support.wait import WebDriverWait

import page
from base.base import Base
from selenium.webdriver.common.by import By
from time import sleep

global_variable_login = 0


class PageLogin(Base):
    global flag
    # 切换到登录界面
    def page_click_please_login(self):
        self.base_click(page.login_please_login)

    # 切换主窗口到登录界面
    def page_change_window(self, driver):
        self.base_change_window(driver)

    # 点击 登录按钮
    def page_click_login(self):
        self.base_click(page.login_login)

    # 点击 密码登录
    def page_click_pwd_login(self):
        self.base_click(page.login_click_pwd_login)

    # 输入账号
    def page_input_account(self, username):
        self.base_input(page.login_input_account, username)

    # 输入密码
    def page_input_password(self, password):
        self.base_input(page.login_input_password, password)

    # 点击协议
    def page_click_protocol(self):
        self.base_click(page.login_click_protocol)

    # 登录
    def page_click_login_button(self):
        self.base_click(page.login_click_login_button)

    # 判断是否登录成功
    def page_is_login_success(self):
        return self.base_if_exist(page.login_logout)

    # 判断是否退出成功
    def page_is_logout_success(self):
        return self.base_if_exist(page.login_login)

    # 安全退出
    def page_click_logout(self):
        self.base_click(page.login_logout)

    # 在登录前获取异常信息
    def page_get_error_info_before(self):
        # 判断是否输入用户名
        if self.base_is_input_empty(page.login_input_account):
            # flag=1
            # return flag
            return self.base_get_text(page.login_phone_lack)
        # 判断是否输入密码
        elif self.base_is_input_empty(page.login_input_password):
            # flag = 2
            # return flag
            return self.base_get_text(page.login_pwd_lack)
        elif not self.base_is_checkbox_checked(page.login_click_protocol):
            # flag = 3
            # return flag
            return self.base_get_text(page.login_protocol_fail)
        # self.page_moving_vertify_code()
        # self.base_move_to_empty_space()
        # 判断密码格式
        elif len(self.driver.find_element(*page.login_input_password).get_attribute('value')) < 4:
            # flag = 4
            # return flag
            # self.page_moving_vertify_code()
            # self.base_move_to_empty_space()
            return self.base_get_text(page.login_passwd_fail)  # 密码格式错误提示

        # 判断用户名或密码错误
        else:
            return self.base_get_text(page.login_account_or_pwd_error)
        # else:
        #     # flag = 5
        #     # return flag
        #     self.page_moving_vertify_code()
        #     self.base_move_to_empty_space()
        #     return self.base_get_text(page.login_account_or_pwd_error)

    def page_is_verify_code(self):
        return self.base_if_exist(page.login_moving_btn)


    # 移动滑块
    def page_moving_vertify_code(self):
        self.base_move(page.login_moving_btn, page.login_moving_area)

    # 登录业务
    def page_login(self, username, password, driver):
        global global_variable_login
        if global_variable_login == 0:
            global_variable_login = 1
            self.page_click_please_login()
            self.page_change_window(driver)
            self.page_click_login()
            self.page_click_pwd_login()

        self.page_input_account(username)
        self.page_input_password(password)
        self.page_click_protocol()
        self.page_click_login_button()
        # 判断是否需要滑动验证
        vertify_code_flag = self.base_is_input_empty(page.login_input_account) or self.base_is_input_empty(
                page.login_input_password) or (not self.base_is_checkbox_checked(page.login_click_protocol))
        if not vertify_code_flag:
            self.page_moving_vertify_code()
            self.base_move_to_empty_space()

