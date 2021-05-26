import common.import_all
import requests
import json


class test_QueryWareHouse():
    global url_warehouse
    url_warehouse =

    def test_case1():
        warehouseName = "广州车务专员"
        res1 = requests.get(warehouseName)
        print(res1.json)
