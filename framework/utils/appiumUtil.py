# -*- coding: UTF8 -*-
from framework.utils import InitDriverUtil


class ApppiumUtil:
    def __init__(self, driver):
        self._driver = InitDriverUtil().select_driver()

    def switch_to_webview(self):
        """
        从原生应用切换到webview
        :return: None
        """
        context = self._driver.contexts
        for cont in context:
            if cont.contains("WEBVIEW"):
                self._driver.switch_to.context(cont)
