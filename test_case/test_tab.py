import requests,unittest
import conf.config,common

class tabListRequest():
    def test_url(self):
        host = conf.config.setConfig.base_url(1)
        endpoint = '/api/asset/listPageQueryTaskByStatus.json?'
        tab_list = (
            "statusListStr=200,300,400,600,500,700,800,900,1000,1100&pageSize=15&currentPage=1",  # 全部
            # "cs2 = 'statusListStr=200&pageSize=15&currentPage=1'",  # 待分配
            # "cs3 = 'statusListStr=300&pageSize=15&currentPage=1'",  #待执行
            # "cs4 = 'statusListStr=400,600,500,700&pageSize=15&currentPage=1'"   #执行中
            # "cs5 = 'statusListStr=800,900,1000,1100&pageSize=15&currentPage=1'"   #已结束
        )
        url_tab = ''.join([host, endpoint,tab_list[0]])
        print(url_tab)

