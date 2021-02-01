import time
from pageAction.login_action import Login

def test_login(getdriver):
    # todo 想办法搞一下driver
    # driver就是getdriver的返回值
    driver=getdriver
    login = Login(driver)
    # 成功登录
    login.login_success()
    time.sleep(1)
    # 点击我的
    login.after_login_click_me()
    time.sleep(1)
    assert '嘟嘟' in driver.page_source
