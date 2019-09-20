# -*- coding: UTF8 -*-
from utils.appiumUtil import ApppiumUtil
import unittest
from utils.selectDriver import SelectDriver
import time


class Demo(unittest.TestCase):
    def test_demo(self):
        driver = SelectDriver().select_driver()
        driver.implicitly_wait(300)
        element1 = driver.find_element_by_id(id_='com.baidu.searchbox:id/baidu_searchbox')
        element1.click()
        element2 = driver.find_element_by_id(id_='com.baidu.searchbox:id/SearchTextInput')
        element2.send_keys('测试')
        # com.baidu.searchbox:id/home_operation_enter
        element3 = driver.find_element_by_id(id_='com.baidu.searchbox:id/home_operation_enter')
        element3.click()
        time.sleep(10)


