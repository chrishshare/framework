# -*- coding: UTF8 -*-
from utils.logUtil import InitLogging
from utils.yamlParser import YamlParser
from utils.initDriverUtil import InitDriverUtil
from selenium.webdriver.support.wait import WebDriverWait
import operator


class SeleniumUtil:
    def __init__(self, driver):
        self._driver = driver
        self._yml = YamlParser()
        self._logger = InitLogging().init_logging()

    def _find_element(self, elcf, elnode):
        """
        查找元素
        :param elcf: 元素所在的yaml配置文件
        :param elnode: 元素节点名称
        :return:
        """
        location = self._yml.parser_elements_from_yaml(cf=elcf, element=elnode)
        by, value = location.get('定位方式'), location.get('定位值')
        self._logger.info('[{node}]的定位方式为:{by},定位值为:{value}'.format(node=elnode, by=by, value=value))

        # 定位元素
        element = self._driver.find_element(by=by, value=value)
        return element

    def operate_element(self, elcf, elnode, dtyml=None, dtnode=None):
        """
        元素操作
        dtyml/dtnode都为None时，内部默认将该操作当做点击事件进行处理
        :param elcf: 元素所在的yaml配置文件
        :param elnode: 元素节点名称
        :param dtyml: 测试数据所在的yaml配置文件
        :param dtnode: 测试数据节点名称
        :return:
        """
        element = self._find_element(elcf=elcf, elnode=elnode)

        # 获取测试数据信息
        data = self._yml.parser_data_from_yaml(cf=dtyml, data=dtnode)
        optype, opvalue = data.get('操作'), data.get('值')

        if dtyml is None and dtnode is None:
            # 元素点击(click)
            element.click()
        elif operator.eq(optype, '输入'):
            # 元素输入(input)
            element.clear()
            element.send_keys(opvalue)
        else:
            self._logger.error('暂不支持的操作方式')





