import test_case.test_login,conf,common
import unittest,HTMLTestRunner

class running(test_case.test_login.loginRequest):
    def login(self):
       global discover
       discover = test_case.test_login.loginRequest.test_post(1)

if __name__ == '__main__':
    # 定义报告存放路径
    # filename = './report/' + 'result.html'
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner(stream=fp, title='加法测试报告', description='用例执行情况： ')
    # runner.run(discover)
    unittest.main()