
import requests
import unittest


class userConfig:
    def user_data(self):
        pw = input("输入密码：")
        user_kotera = {"userAccount": "17376509487", "password": pw}
        return user_kotera


class urlConfig:
    def base_url(self):
        global host
        host = 'https://iov-asset-protection.prepub.souche-inc.com/'
        return host

    def login_url(self):
        host = urlConfig.base_url(1)
        endpoint = 'login.json'
        url_login = ''.join([host, endpoint])  # 登录接口路径
        return url_login

    def list_url(self):
        endpoint = 'api/asset/listPageQueryTaskByStatus.json'
        url_list = ''.join([host, endpoint])
        return url_list


class reqHeader:
    def fill_header(self):
        header = {

        }


class commonUsed:
    def case_endpoint(self):
        a = '*****'


'''

[host]
host=https://iov-asset-protection.prepub.souche-inc.com/

[url]
login_url=login.json
list_url=api/asset/listPageQueryTaskByStatus.json


[user]
userAccount=17376509487
password=pw

'''
