import pytest
'''
一使用fixture函数需要两步
1.定义fixture函数
2.如何调用
二python 三大器
生成器 yield  生成器就是特殊的迭代器
边计算边遍历,节省了内存
迭代器  能用for ..in...循环遍历  自己写:__next__,__iter__
装饰器@pytest.fixture(scope='function',autouse=True)
@符号
作用：给在不改变原来函数功能的前提下，增加额外的功能
体现代码的复用性
'''
# 调用方式一
# 定义
# 作用域:默认scope是函数级别
@pytest.fixture(scope='function',autouse=True)
def login():
    print('输入账号，密码，登录')
    # return 100
    # 1.返回值-初始化的时候执行的 2.yield 100之后就执行作用域范围的测试用例
    # 3.作用域范围的测试用例结束之后，开始执行print('要进行清场了')
    # python语法的科普：函数里面有yield关键字  生成器
    yield 100
    print('要进行清场了')




# 使用fixture
#1.直接把被装饰的函数的名字直接当作参数传入测试用例里面
def test_1(login):
    print('用例1：登录之后，点击购物车')
    print(login)


#
# def test_2(login):
#     print('用例2：登录之后，点击修改个人资料')
# # 2.
# @pytest.mark.usefixtures('login')
# def test_3(login):
#     print('用例3：登录之后，点击修改地址')
#
#
# def test_4():
#     print('用例4：登录之后，点击999999999')