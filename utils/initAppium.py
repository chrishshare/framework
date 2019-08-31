from appium import webdriver
from utils.yamlParser import parser_yaml_to_dict
from getrootdir import root_path
import os


class InitAppium:
    def __init__(self):
        """
        init appium config yaml file
        """
        self._yaml_dict = parser_yaml_to_dict(root_path + os.sep + 'baseconf' + os.sep + 'appiumConfig.yaml')

    def _get_avaliable_device(self):
        """
        get avaliable device
        :return:
        """
        device_list = self._yaml_dict.get('device')

        # {'device1': {'avaliable': True, 'deviceName': 'devicesn', 'platformVersion': '9.0.1'},
        #                 'device2': {'avaliable': False, 'deviceName': 'devicesn', 'platformVersion': '9.0.1'}}
        for key, value in device_list.items():
            if value.get('avaliable'):
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
        desired_caps.update(self._yaml_dict.get('appInfo'))
        # appium common settings
        desired_caps.update(self._yaml_dict.get('appium_config'))
        desired_caps.update(self._get_avaliable_device())

        # init webdriver
        driver = webdriver.Remote(self._yaml_dict.get('remoteurl'), desired_caps)
        return driver


if __name__ == '__main__':
    InitAppium().init_webdriver()
