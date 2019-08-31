# -*- coding: UTF8 -*-
from utils.initAppium import InitAppium
from utils.initSelenium import InitSelenium
from utils.yamlParser import YamlParser


class SelectDriver:
    def __init__(self):
        self._project_type = YamlParser().parser_common_conf('projectconfig.yaml').get('projecttype')

    def select_driver(self):
        """
        根据项目类型选择对应的驱动方式
        :return: driver
        """
        driver = ''
        if 'app' == self._project_type:
            driver = InitAppium().init_appium_webdriver()
        elif 'web' == self._project_type:
            driver = InitSelenium().init_selenium_webdriver()
        else:
            pass
        return driver


if __name__ == '__main__':
    SelectDriver().select_driver()
