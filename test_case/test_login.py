import requests,unittest
import conf.config,common

class loginRequest(conf.config.urlConfig,unittest.TestCase):
    # 调参数
    # case1：正确用户名+正确密码
    def test_case1(self):
        global get_url
        get_data = conf.config.userConfig.user_data(1)
        get_url = conf.config.urlConfig.login_url(1)
        res_login1 = requests.post(get_url,get_data)
        # print('response:',res_login1.json())
        try:
            self.assertIn('token', res_login1.text, msg='登录失败')
            print('login case1 passed')
        except:
            print('login case1 fail')
        # print(result)

    # case2：正确用户名+错误密码
    def test_case2(self):
        res_login2 = requests.post(get_url,'a123456')

        try:
            self.assertNotIn('token', res_login2.text, msg='登录失败')
            print('login case2 passed')
        except:
            print('login case2 fail')

    # case3：错误用户名+错误密码
    def test_case3(self):
        res_login3 = requests.post(get_url, 'a123456')
        try:
            self.assertNotIn('token',res_login3.text, '登录失败')
            print('login case3 passed')
        except:
            print('login case3 fail')



