# -*- coding: UTF8 -*-
from utils.logUtil import InitLogging
from utils.yamlParser import YamlParser
from utils.initDriverUtil import InitDriverUtil
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumUtil:
    def __init__(self):
        self._driver = InitDriverUtil().select_driver()
        self._yml = YamlParser()

    def fw_find_element(self, cf, el):
        location = self._yml.parser_elements_from_yaml(cf=cf, element=el)
        element = self._driver.find_element(by=location.get('定位方式'), value='定位表达式')
        return element




