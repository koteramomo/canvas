import requests,unittest
from common import get_message
from conf import config

class tabListRequest(get_message.commonUse,config.urlConfig):
    def set_url(self):
        global url_list

        endpoint = '/api/asset/listPageQueryTaskByStatus.json?'
        args1 = {
            'statusListStr': '200'
        }


    def test_case1(self):
        # 查询全部list
        tab_list = (
            "statusListStr=200,300,400,600,500,700,800,900,1000,1100&pageSize=15&currentPage=1",  # 全部
            "cs2 = 'statusListStr=200&pageSize=15&currentPage=1'",  # 待分配
            "cs3 = 'statusListStr=300&pageSize=15&currentPage=1'",  # 待执行
            "cs4 = 'statusListStr=400,600,500,700&pageSize=15&currentPage=1'"  # 执行中
            "cs5 = 'statusListStr=800,900,1000,1100&pageSize=15&currentPage=1'"  # 已结束
        )
        #全部list地址
        path = config.urlConfig.list_url(1)
        url_list = ''.join([path,tab_list[0]])

        header = get_message.commonUse.get_header(1)
        res_list = requests.get(url=url_list,header = header)
        print( res_list.json() )



