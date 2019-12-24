# -*- coding: UTF8 -*-
from utils.logUtil import InitLogging
from utils.yamlParser import YamlParser
from utils.initDriverUtil import InitDriverUtil
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumUtil:
    def __init__(self):
        self._driver = InitDriverUtil().select_driver()

    # def is_element_exists(self):
    #     element = WebDriverWait(driver=self._driver, timeout=20, poll_frequency=0.5).until()


