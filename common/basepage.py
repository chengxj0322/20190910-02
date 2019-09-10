# Author:xinxin


import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
from appium.webdriver.common.mobileby import MobileBy

from common.dir_config import screenshot_dir

class BasePage:

    # 包含了PageObjects当中，用到所有的selenium底层方法。
    # 还可以包含通用的一些元素操作，如alert,iframe,windows...
    # 还可以自己额外封装一些web相关的断言
    # 实现日志记录、实现失败截图

    def __init__(self,driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, loc, timeout=20, frequency=0.5, doc=""):
            star = datetime.datetime.now()
            try:
                WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
            except:
                logging.exception("等待{}元素出现，失败！".format(loc))
                self.save_img(doc)
                # raise
            else:
                end = datetime.datetime.now()
                duration = end - star
                logging.info("等待{}元素可见，成功。等待了{}".format(loc, duration))
                return True

    # 等待元素出现
    def wait_eleExists(self, loc, timeout=20, frequency=0.5, doc=""):
            start = datetime.datetime.now()
            try:
                WebDriverWait(self.driver, timeout, frequency).until(EC.presence_of_all_elements_located(loc))
            except:
                logging.exception('等待{}元素出现失败'.format(loc))
                self.save_img(doc)
                raise
            else:
                end = datetime.datetime.now()
                duration = end - start
                logging.info('等待{}元素出现成功，等待了{}'.format(loc, duration))

     # 查找元素
    def get_element(self, loc, doc=""):
            try:
                ele = self.driver.find_element(*loc)
            except:
                logging.exception("查找{}元素，失败！".format(loc))
                self.save_img(doc)
            else:
                logging.info("查找{}元素成功！".format(loc))
                return ele

    # 获取元素文本内容
    def get_element_text(self, loc, timeout=30, frequency=0.5, doc=""):
            self.wait_eleVisible(loc, timeout=30, frequency=0.5, doc="")
            ele = self.get_element(loc, doc="")
            # 获取属性
            try:
                text = ele.text
            except:
                # 日志
                logging.exception("获取元素文本值失败")
                # 截图
                self.save_web_screenshot(doc)
                raise
            else:
                logging.info("获取元素 {} 的文件值为:{}".format(loc, text))
                return text

     # 点击操作
    def click(self, loc, timeout=30, frequency=0.5, doc=""):
            self.wait_eleVisible(loc, timeout=30, frequency=0.5, doc="")
            ele = self.get_element(loc, doc="")
            try:
                ele.click()
            except:
                logging.exception("点击{}元素，失败！".format(loc))
                self.save_img(doc)
                raise
            else:
                logging.info("点击{}元素成功！".format(loc))

    # 给元素赋值
    def input_text(self, loc, value, timeout=30, frequency=0.5, doc=""):
            self.wait_eleVisible(loc, timeout=30, frequency=0.5, doc="")
            ele = self.get_element(loc, doc="")
            try:
                ele.send_keys(value)
            except:
                logging.exception("向{}元素输入{}，失败！".format(loc, value))
                self.save_img(doc)
                raise
            else:
                logging.info("向{}元素输入{}，成功！".format(loc, value))

    # 保存截图
    def save_img(self, doc=""):
            cur_time = time.strftime("%Y-%m-%d %H_%M_%S")
            file = screenshot_dir + '/{}_{}.png'.format(doc, cur_time)
            try:
                # self.driver.save_screenshot(file)
                self.driver.save_screenshot(file)
            except:
                logging.exception("保存截图失败！")
                raise
            else:
                logging.info("保存截图成功！，路径为{}".format(file))


    # 获取屏幕的大小
    def get_device_size(self):
        try:
            device_size = self.driver.get_window_size()
        except:
            pass
        else:
            return device_size

    # 左滑右滑上下滑 up down left right
    def swipe_screen(self,direction,driver):
        """
        函数功能说明
        :param direction:滑动方向。up：向上滑；down:向下滑；left:向左滑；right:向右滑
        :return:
        """
        size = self.get_device_size()
        if direction.lower == "up" or "down":
            start_x = size["width"] * 0.5
            start_y = size["height"] * 0.1
            end_x = size["width"] * 0.5
            end_y = size["height"] * 0.9
            if direction.lower == "up" :
                driver.swipe(start_x, start_y, end_x, end_y, 260)
            else:
                driver.swipe(start_x, end_y, end_x, start_y, 260)
        elif direction.lower == "left" or "right":
            start_x = size["width"] * 0.9
            start_y = size["height"] * 0.5
            end_x = size["width"] * 0.1
            end_y = size["height"] * 0.5
            if direction.lower == "left":
                driver.swipe(start_x, start_y, end_x, end_y, 260)
            else:
                driver.swipe(end_x, start_y, start_x, end_y, 260)
        else:
            print('请输入正确指令！')


    def get_toast_msg(self,loc,doc=""):
        try:
            # self.wait_eleExists(loc)
            WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(loc))
            print('找到toast了！！')
            text = self.driver.find_element(loc).text()
        except:
            logging.info('查找包含{}的toast失败'.format(loc))
            raise
        else:
            logging.info('查找包含{}的toast成功'.format(loc))
            return text

