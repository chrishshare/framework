from selenium import webdriver
from utils.yamlParser import YamlParser
from getrootdir import root_path
import os
from getrootdir import root_path
from utils.logUtil import InitLogging


class InitSelenium:
    def __init__(self):
        self._driver_root_path = root_path + os.sep + 'browserdriver' + os.sep
        self._logger = InitLogging().init_logging()
        self._selenium_cf = YamlParser().parser_common_conf(cf='seleniumConfig.yaml')

    def init_selenium_webdriver(self):
        driver = ''
        if 'chrome' == self._selenium_cf.get('browser'):
            driver = webdriver.Chrome(executable_path=self._driver_root_path + self._selenium_cf.get('chrome'))
        elif 'firefox' == self._selenium_cf.get('browser'):
            driver = webdriver.Firefox(executable_path=self._driver_root_path + self._selenium_cf.get('firefox'))

        elif 'ie64' in self._selenium_cf.get('browser'):
            driver = webdriver.Ie(executable_path=self._driver_root_path + self._selenium_cf.get('ie64'))
        elif 'ie32' in self._selenium_cf.get('browser'):
            driver = webdriver.Ie(executable_path=self._driver_root_path + self._selenium_cf.get('ie32'))
        else:
            self._logger.error('输入的浏览器目前尚未支持')
        #     浏览器窗口最大化
        driver.maximize_window()
        return driver


if __name__ == '__main__':
    InitSelenium().init_selenium_webdriver().get('https://www.baidu.com')
