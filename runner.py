import test_case.test_login,conf,common
import unittest,HTMLTestRunner
#coding=utf-8

# class running(test_case.test_login.loginRequest):
#     def login(self):
#        # global discover
#        test_case.test_login.loginRequest.test_login(1)
#
# if __name__ == '__main__':
#     # 定义报告存放路径
#     # filename = './report/' + 'result.html'
#     # fp = open(filename, 'wb')
#     # runner = HTMLTestRunner(stream=fp, title='加法测试报告', description='用例执行情况： ')
#     # runner.run(discover)
#     unittest.main()
# discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
import unittest
from HTMLTestRunner import HTMLTestRunner
from test_case.test_login import loginRequest
# coding utf-8

# def report():
suite = unittest.TestSuite()  # 创建测试套件，将测试用例添加至套件中
suite.addTest( loginRequest( 'test_case1' ) )

if __name__ == '__main__':
    test_dir = './test_case'  # 当前路径
    filepath = r'/Users/dasouche/Desktop/canvas/test_result.html'
    fp = open(filepath, 'wb')
    runner = HTMLTestRunner(stream=fp, title='test', description='执行结果')
    runner.run(suite)
    fp.close()