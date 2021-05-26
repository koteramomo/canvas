import sys
import requests
import json
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


class commonUse(config.urlConfig, unittest.TestCase):
    def login_suc(self):
        get_data = config.userConfig.user_data(1)
        get_url = config.urlConfig.login_url(1)
        r = requests.post(get_url, get_data)
        jr = json.loads(r.text)
        print(type(jr))
        token = commonUse.find_dict('token', jr)
        return token
        # try:
        #     self.assertIsNotNone(jr.text)
        #     print('预登陆成功，开始测试')
        #
        # #     return token
        # except:
        #     print('登录失败，中止运行')
        #     pass

    # 在一个字典中按键查值
    def find_dict(target, dictData, notFound='没找到'):
        queue = [dictData]
        while len(queue) > 0:
            data = queue.pop()
            for key, value in data.items():
                if key == target:
                    return value
                elif type(value) == dict:
                    queue.append(value)
        return notFound

    # 有多个同名键在字典里时查询

    def find_all(target, dictData, notFound=['无结果']):
        queue = [dictData]
        result = []
        while len(queue) > 0:
            data = queue.pop()
            for key, value in data.items():
                if key == target:
                    result.append(value)
                elif type(value) == dict:
                    queue.append(value)
        if not result:
            result = notFound
        return result

    def get_header(self):
        token = commonUse.login_suc(1)
        header = {'_security_token': token}
        return header
