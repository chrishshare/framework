# -*- coding:utf8 -*-
import unittest
import time
from utils.seleniumUtil import SeleniumUtil
from testcases.baseCase import BaseCase


class Demo(BaseCase):
    def test_demo(self):
        selenium = SeleniumUtil(self.driver)
        selenium.operate_element(elcf='commonElements.yaml', elnode='搜索输入框', dtnode='搜索关键字', dtyml='demo.yaml')
        selenium.operate_element(elcf='commonElements.yaml', elnode='搜索输入框', dtnode='搜索关键字', dtyml='demo.yaml')
        time.sleep(5)