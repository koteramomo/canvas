import requests
import unittest
import configparser
from conf import config
# class getMsg(conf.config):
#     def login_data(self):
#         # url1 = conf.config.setConfig.base_url()
#         # data1 = conf.conf.config.setConfig.user_data()
#         # return url1,data1
#     def get_token(self):
#         usermsg = conf.config.setConfig.user_data(1)
#         res_login1 = requests.post(loginRequest.login_url(1), usermsg)

class commonUse(config.urlConfig,unittest.TestCase):
    def login_suc(self):
        get_data = config.userConfig.user_data(1)
        get_url = config.urlConfig.login_url(1)
        r = requests.post(get_url, get_data)
        print(r.json())
        get_token = r.json()['token']
        try:
            self.assertIn('token', r.json(), msg='登录失败')
            print('预登陆成功，开始测试')
            return get_token
        except:
            print('登录失败，中止运行')


