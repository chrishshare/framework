# -*- coding:utf8 -*-
import unittest
import time
from utils.seleniumUtil import SeleniumUtil


class Demo1(unittest.TestCase):
    def test_demo1(self):
        selenium = SeleniumUtil()
        selenium.operate_element(elcf='commonElements.yaml', elnode='搜索输入框', dtnode='搜索关键字', dtyml='demo.yaml')
        selenium.operate_element(elcf='commonElements.yaml', elnode='搜索输入框', dtnode='搜索关键字', dtyml='demo.yaml')
        time.sleep(5)
