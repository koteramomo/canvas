import requests,unittest
import conf.config,common

class loginRequest(conf.config.setConfig,unittest.TestCase):
    # 登录接口路径
    def login_url(self):
        host = conf.config.setConfig.base_url(1)
        endpoint = 'login.json'
        url_login = ''.join([host, endpoint])
        return url_login

    # case1：正确用户名+正确密码
    def test_case1(self):
        correct_data = conf.config.setConfig.user_data(1)
        res_login1 = requests.post(loginRequest.login_url(1),correct_data)
        print('response:',res_login1.json())
        self.assertIn('token', res_login1.text, '登录失败')
        # print(result)

    # case2：正确用户名+错误密码
    def test_case2(self):
        res_login2 = requests.post(loginRequest.login_url(1),'a123456')
        self.assertNotIn('token', res_login2.text, '登录失败')

    # case3：错误用户名+错误密码
    def test_case3(self):
        res_login3 = requests.post(loginRequest.login_url(1), 'a123456')
        self.assertNotIn('token',res_login3.text, '登录失败')




