import unittest
from HTMLTestRunner import HTMLTestRunner

class testCase(unittest.TestCase):
    # 测试case
    def test_01(self):
        print("test01")
    def test_03(self):
        print("test03")
    def test_04(self):
        print("test04")
    def test_05(self):
        print("test05")

if __name__ == '__main__':
    test_dir = './'  # 当前路径
    filepath = r'/Users/dasouche/Desktop/canvas/test_result.html'
    fp = open( filepath, 'wb' )
    discover = unittest.defaultTestLoader.discover( test_dir, pattern='demo.py' )
    runner = HTMLTestRunner(stream=fp, title='test', description='执行结果')
    runner.run(discover)
    fp.close()
# if __name__ == '__main__':
#      # 实例化测试套件
#      suite = unittest.TestSuite()
#      # 实例化第二个测试套件
#      suite1 = unittest.TestSuite()
#      # 添加测试用例 - 方式一
#      suite.addTest(testCase('test_03'))
#      suite.addTest(testCase('test_01'))
#      suite1.addTest(testCase('test_03'))
#      suite1.addTest(testCase('test_01'))
#     # 添加测试用例 - 方式二
#      testcase = (testCase('test_05'), testCase('test_04'))
#      suite.addTests(testcase)
#     # 测试套件添加测试套件
#      suite.addTest(suite1)
#      # 实例化TextTestRunner类
#      # runner = unittest.TextTestRunner()
#      filepath = r'/Users/dasouche/Desktop/canvas/test_result.html'
#      fp = open( filepath, 'wb' )
#      runner = HTMLTestRunner(stream=fp, title='test', description='执行结果')
#      # 运行测试套件
#      runner.run(suite)
#      fp.close()
