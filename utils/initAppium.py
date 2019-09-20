from appium import webdriver
from utils.yamlParser import YamlParser
from getrootdir import root_path
import os


class InitAppium:
    def __init__(self):
        """
        init appium config yaml file
        """
        self._appium_cf = YamlParser().parser_common_conf(cf='appiumConfig.yaml')

    def _get_available_device(self):
        """
        get avaliable device
        :return:
        """
        device_list = self._appium_cf.get('device')

        # {'device1': {'avaliable': True, 'deviceName': 'devicesn', 'platformVersion': '9.0.1'},
        #                 'device2': {'avaliable': False, 'deviceName': 'devicesn', 'platformVersion': '9.0.1'}}
        for key, value in device_list.items():
            if value.get('available'):
                del value['available']
                return value

    def init_appium_webdriver(self):
        """
        1. get deviceconfig file
        2. get devcieconfig.yaml to a dict
        3. judge which device is set to can use, and get length
        4. new thread pools
        5. init webdriver
        :return:
        """
        desired_caps = {}
        # appilcation settings
        desired_caps.update(self._appium_cf.get('appInfo'))
        # appium common settings
        desired_caps.update(self._appium_cf.get('appium_config'))
        desired_caps.update(self._get_available_device())

        # init webdriver
        driver = webdriver.Remote(self._appium_cf.get('remoteurl'), desired_caps)
        return driver


if __name__ == '__main__':
    InitAppium().init_appium_webdriver()
