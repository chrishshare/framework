# -*- coding:utf8 -*-
from framework.utils import InitDriverUtil
from pythonlog.utils.logUtil import init_logging
import unittest


class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = InitDriverUtil().select_driver()
        cls.logger = init_logging()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

