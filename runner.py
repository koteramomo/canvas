# coding=UTF-8
import unittest
from HTMLTestRunner import HTMLTestRunner
from test_case.test_login import loginRequest

#方法1 直接调unittest默认方法
if __name__ == '__main__':
    test_dir = './'  # 当前路径
    filepath = r'/Users/dasouche/Desktop/canvas/test_result.html'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login.py' )
    # print(discover)
    fp = open(filepath, 'wb')
    # runner = HTMLTestRunner(stream=fp, title='test', description='执行结果')
    runner = unittest.TextTestRunner()
    runner.run(discover)
    fp.close()
# #方法2 实例化套件testsuite
# if __name__ == '__main__':
#      # 实例化测试套件
#      suite = unittest.TestSuite()
#      # 添加测试用例 - 方式一
#      suite.addTest(loginRequest('test_case1'))
#      # 实例化TextTestRunner类
#      # runner = unittest.TextTestRunner()
#      filepath = r'/Users/dasouche/Desktop/canvas/iii.html'
#      fp = open( filepath, 'wb' )
#      runner = HTMLTestRunner(stream=fp, title='test', description='执行结果')
#      # 运行测试套件
#      runner.run(suite)
#      fp.close()


