# Author:xinxin
# import pytest
import unittest
from ddt import ddt,data
from pageobjects.indexpage import IndexPage
from appium import webdriver
from TestCases import conftest
import time
from TestDatas import login_data as ld
# @pytest.mark.usefixtures("start")
@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # 你要在哪个系统上对哪个app进行操作！！
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "6.0.1"
        desired_caps["deviceName"] = "Android Emulator"
        desired_caps["appPackage"] = "com.lemon.lemonban"
        desired_caps["appActivity"] = "com.lemon.lemonban.activity.WelcomeActivity"
        desired_caps["noReset"] = True
        # 与appium服务进行连接，并告诉appium我要干嘛。
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(10)
        # return cls.driver
    def tearDown(self):
        pass



    def test_login_sucess(self):
        IndexPage(self.driver).login(ld.sucess['username'],ld.sucess['pwd'])
        time.sleep(3)
        # result = IndexPage(start).get_login_toast_msg(ld.sucess['check'])
        result = IndexPage(self.driver).get_login_toast_msg()
        assert result == '登陆成功'

