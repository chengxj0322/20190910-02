# Author:xinxin
from appium.webdriver.common.mobileby import MobileBy
#我要借款
borrow_loc = (MobileBy.ID,'com.xxzb.fenwoo:id/layout_borrow_money')
#我的柠檬
my_lemon_loc = (MobileBy.ID,'com.lemon.lemonban:id/navigation_my')
#点击头像登录
click_to_login_loc = (MobileBy.ID,'com.lemon.lemonban:id/fragment_my_lemon_avatar_layout')
#用户名
username_loc = (MobileBy.ID,'com.lemon.lemonban:id/et_mobile')
#密码
pwd_loc = (MobileBy.ID,'com.lemon.lemonban:id/et_password')
#登录按钮
btn_login_loc = (MobileBy.ID,'com.lemon.lemonban:id/btn_login')
#登录成功提示语
# toast_loc = (MobileBy.XPATH,'//*[contains(@text,"手机号码或密码")]')
toast_loc = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("手机号码或密码不能为空")')
#//*[contains(@text,"{}".format(str)]