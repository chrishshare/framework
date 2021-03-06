from selenium import webdriver
from utils.yamlParser import YamlParser
import os
from pythonlog.utils.logUtil import init_logging
from getrootdir import root_path
import operator
from selenium.webdriver.remote.file_detector import LocalFileDetector



class InitDriverUtil:
    """
    初始化驱动程序，web项目同时输入地址
    @CREATED: siyzhou@163.com
    @CREATED_DATE: 2019-11-30
    @MODIFIED_DATE:
    """
    def __init__(self):
        self._logger = init_logging()
        self._conf = YamlParser().parser_common_conf(cf='projectConfig.yaml')
        self._project_root = root_path + os.sep
        self._driver_root_path = self._project_root + os.sep + 'drivers' + os.sep

    def select_driver(self):
        """
        选择驱动类型
        :return:
        """
        project_type = self._conf.get('projectType')
        if 'web' == project_type:
            return self._init_web_driver()
        elif 'app' == project_type:
            return self._init_appium_driver()
        else:
            self._logger.error("当前仅支持app、web两种类型的项目！")

    def _init_web_driver(self):
        """
        初始化web浏览器
        :return: driver
        """
        driver_version = self._conf.get('browser')
        distribute = self._conf.get('seleniumGrid')
        driver = ''
        # 分布式开关开时，远程驱动浏览器，分布式开关关时本地驱动浏览器
        if not distribute.get('switch'):
            # 本地驱动chrome浏览器
            if operator.contains(driver_version.lower(), 'chrome'):
                driver_path = self._driver_root_path + 'chrome' + os.sep + self._conf.get('webbrowser').get(driver_version)
                driver = webdriver.Chrome(executable_path=driver_path)
            # 本地驱动firefox浏览器
            elif operator.contains(driver_version.lower(), 'firefox'):
                driver_path = self._driver_root_path + 'firefox' + os.sep + self._conf.get('webbrowser').get(driver_version)
                driver = webdriver.Firefox(executable_path=driver_path)
            # 本地驱动ie浏览器
            elif operator.contains(driver_version.lower(), 'ie'):
                driver_path = self._driver_root_path + 'ie' + os.sep + self._conf.get('webbrowser').get(driver_version)
                driver = webdriver.Ie(executable_path=driver_path)
            # 本地驱动edge浏览器
            elif operator.contains(driver_version.lower(), 'edge'):
                driver_path = self._driver_root_path + 'edge' + os.sep + self._conf.get('webbrowser').get(driver_version)
                driver = webdriver.Edge(executable_path=driver_path)
            else:
                raise self._logger.error('您选择的浏览器类型赞不支持')
        elif distribute.get('switch'):
            # 远程驱动chrome浏览器
            if operator.contains(driver_version.lower(), 'chrome'):
                driver_path = '/opt/selenium/chromedriver-86.0.4240.22'
                chrome_desired = {
                    "browserName": "chrome",
                    "platform": "LINUX",
                    "cssSelectorsEnabled": True,
                    "javascriptEnabled": True,
                    "binary": driver_path,
                }
                driver = webdriver.Remote(command_executor=distribute.get('hubUrl'), desired_capabilities=chrome_desired)
            # 远程驱动firefox浏览器，暂不支持
            elif operator.contains(driver_version.lower(), 'firefox'):
                driver_path = self._driver_root_path + 'firefox' + os.sep + self._conf.get('webbrowser').get(
                    driver_version)
                fox_desired = {
                    "browserName": "firefox",
                    "platform": "WINDOWS",
                    "cssSelectorsEnabled": True,
                    "javascriptEnabled": True,
                    "firefox_binary": driver_path,

                }
                driver = webdriver.Remote(command_executor=distribute.get('hubUrl'), desired_capabilities=fox_desired)
            # 远程本地驱动ie浏览器
            elif operator.contains(driver_version.lower(), 'ie'):
                driver_path = self._driver_root_path + 'ie' + os.sep + self._conf.get('webbrowser').get(driver_version)
                ie_desired = {
                    "browserName": "internet explorer",
                    "platform": "WINDOWS",
                    "cssSelectorsEnabled": True,
                    "javascriptEnabled": True,
                    "binary": driver_path,
                }
                driver = webdriver.Remote(command_executor=distribute.get('hubUrl'), desired_capabilities=ie_desired)
            # 远程驱动edge浏览器，暂不支持
            elif operator.contains(driver_version.lower(), 'edge'):
                driver_path = self._driver_root_path + 'edge' + os.sep + self._conf.get('webbrowser').get(
                    driver_version)
                edge_desired = {
                    "browserName": "MicrosoftEdge",
                    "platform": "WINDOWS",
                    "cssSelectorsEnabled": True,
                    "javascriptEnabled": True,
                    "binary": driver_path,
                }
                driver = webdriver.Remote(command_executor=distribute.get('hubUrl'), desired_capabilities=edge_desired)
            else:
                self._logger.error('您选择的浏览器类型赞不支持')
            driver.file_detector = LocalFileDetector()
        # 浏览器最大化
        driver.maximize_window()

        # 项目名称
        project = self._conf.get('project')

        # 项目url
        url = self._conf.get(project).get('url')

        # 输入地址到浏览器地址栏
        driver.get(url=url)
        driver.implicitly_wait(self._conf.get(project).get('timeout'))

        return driver

    def _init_appium_driver(self):
        """
        初始化appium驱动
        :return: driver
        """
        desired_caps = {}

        # appilcation settings
        project = self._conf.get('project')
        desired_caps.update(self._conf.get(project).get('appInfo'))

        # appium common settings
        desired_caps.update(self._conf.get('appium_config'))

        # 获取设备名称
        device_name = self._conf.get(project).get('useDevice')

        # 设备信息
        device_info = self._conf.get(device_name)
        desired_caps.update(device_info)

        # init webdriver
        driver = webdriver.Remote(self._conf.get('remoteurl'), desired_caps)
        return driver


if __name__ == '__main__':
    # InitDriverUtil().init_web_driver()
    InitDriverUtil()._init_appium_driver()
