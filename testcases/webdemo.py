# -*- coding:utf8 -*-
import unittest
from utils.initDriverUtil import InitDriverUtil
import time
from utils.yamlParser import YamlParser


class Demo(unittest.TestCase):
    def test_demo(self):
        driver = InitDriverUtil().select_driver()
        element1 = driver.find_element_by_id(id_='com.baidu.searchbox:id/baidu_searchbox')
        element1.click()
        element2 = driver.find_element_by_id(id_='com.baidu.searchbox:id/SearchTextInput')
        testdata = YamlParser().parser_test_data_conf('demo.yaml')
        element2.send_keys(testdata.get('搜索关键字'))
        # com.baidu.searchbox:id/home_operation_enter
        element3 = driver.find_element_by_id(id_='com.baidu.searchbox:id/home_operation_enter')
        element3.click()
        time.sleep(10)