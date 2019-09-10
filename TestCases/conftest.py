# Author:xinxin
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time
from pagelocators import indexpagelocators as ip
import pytest

# from selenium import webdriver
@pytest.fixture()
def start():
    # 你要在哪个系统上对哪个app进行操作！！
    desired_caps = {}
    desired_caps["platformName"] = "Android"
    desired_caps["platformVersion"] = "6.0.1"
    desired_caps["deviceName"] = "Android Emulator"
    desired_caps["appPackage"] = "com.lemon.lemonban"
    desired_caps["appActivity"] = "com.lemon.lemonban.activity.WelcomeActivity"
    desired_caps["noReset"] = True
    # 与appium服务进行连接，并告诉appium我要干嘛。
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    time.sleep(10)
    yield driver
