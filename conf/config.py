import requests,unittest

class userConfig:
    def user_data(self):
        pw = input("输入密码：")
        user_kotera = {"userAccount":"17376509487","password":pw}
        return user_kotera

class urlConfig:
    def base_url(self):
        url = 'https://iov-asset-protection.prepub.souche-inc.com/'
        return url

    def login_url(self):
        host = urlConfig.base_url(1)
        endpoint = 'login.json'
        url_login = ''.join([host, endpoint]) # 登录接口路径
        return url_login


class commonUsed:
    def case_endpoint(self):
        a = '*****'