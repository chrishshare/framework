# -*- coding:utf8 -*-
from utils.initDriverUtil import InitDriverUtil
from utils.logUtil import InitLogging
import unittest


class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = InitDriverUtil().select_driver()
        cls.logger = InitLogging()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

