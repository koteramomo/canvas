import requests,unittest
import conf.config
from conf import config
from common import get_message

class loginRequest(config.userConfig,get_message.commonUse):
    # 调参数
    # case1：正确用户名+正确密码
    # def test_case1(self):
    #     global get_url
    #     get_data = conf.config.userConfig.user_data(1)
    #     get_url = conf.config.urlConfig.login_url(1)
    #     res_login1 = requests.post(get_url,get_data)
    #     print('response:',res_login1.json())
    #     try:
    #         self.assertIn('token', res_login1.text, msg='登录失败')
    #         print('login case1 passed')
    #     except:
    #         print('login case1 fail')
    #     # print(result)

    # case2：正确用户名+错误密码
    def test_case2(self):
        get_token = get_message.commonUse.login_suc(1)
        print(get_token)
        # url_list = conf.config.urlConfig.list_url( 1 )
        # print(url_list)
        # dfp = {
        #     "statusListStr":"200",
        #     "pageSize":"15",
        #     "currentPage":"1"
        # }
        # r = requests.get(url_list, params=dfp)

        # r = requests.get(url="https://iov-asset-protection.prepub.souche-inc.com/api/asset/listPageQueryTaskByStatus.jsonstatusListStr=200&pageSize=15&currentPage=1")



        # print(r,r.json(),r.text)



        # endpoint = '/api/asset/listPageQueryTaskByStatus.json?'
        # args1 = {
        #     'statusListStr': '200'
        # }
        # tab_list = (
        #     "statusListStr=200,300,400,600,500,700,800,900,1000,1100&pageSize=15&currentPage=1",  # 全部
        #     "cs2 = 'statusListStr=200&pageSize=15&currentPage=1'",  # 待分配
        #     "cs3 = 'statusListStr=300&pageSize=15&currentPage=1'",  # 待执行
        #     "cs4 = 'statusListStr=400,600,500,700&pageSize=15&currentPage=1'"  # 执行中
        #     "cs5 = 'statusListStr=800,900,1000,1100&pageSize=15&currentPage=1'"  # 已结束
        # )

        # print( res_list.json() )



