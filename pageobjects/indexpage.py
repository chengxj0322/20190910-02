# Author:xinxin
from common.basepage import BasePage
from pagelocators import indexpagelocators as ip
import time
class IndexPage(BasePage):
    def login(self,username,pwd):
        self.wait_eleVisible(ip.my_lemon_loc,doc="等待首页的我的柠檬可见")
        self.click(ip.my_lemon_loc,doc="点击首页的我的柠檬")
        self.click(ip.click_to_login_loc,doc="点击头像登录")
        self.input_text(ip.username_loc,username,doc="输入用户名")
        self.input_text(ip.pwd_loc,pwd,doc='输入密码')
        self.click(ip.btn_login_loc,doc="点击登录按钮")
    def get_login_toast_msg(self):
        text=self.get_toast_msg(ip.toast_loc,doc="查看提示语")
        return text

