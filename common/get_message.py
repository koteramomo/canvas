import requests,conf.config

class getMsg(conf.config):
    def login_data(self):
        # url1 = conf.config.setConfig.base_url()
        # data1 = conf.conf.config.setConfig.user_data()
        # return url1,data1
    def get_token(self):
        usermsg = conf.config.setConfig.user_data(1)
        res_login1 = requests.post(loginRequest.login_url(1), usermsg)
