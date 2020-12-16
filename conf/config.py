import requests,unittest

class setConfig:
    def base_url(self):
        url = 'https://iov-asset-protection.prepub.souche-inc.com/'
        # print("请求url为： ", url)
        return url
    def user_data(self):
        pw = input("输入密码：")
        np = {"userAccount":"17376509487","password":pw}
        # print("用户名&密码为：", np)
        return np

class commonUsed:
    def case_endpoint(self):
        a = '*****'